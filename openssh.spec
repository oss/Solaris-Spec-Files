Name: openssh
Version: 3.8.1p1
Release: 1evil
Summary: Secure Shell - telnet alternative (and much more)
Group: Cryptography
License: BSD
Source0: %{name}-%{version}.tar.gz
Source1: auth-pam-password.patch
Patch0: sshd-ctl.patch
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: openssl patch make tcp_wrappers perl > 5.0.0
%ifos solaris2.9
 %ifarch sparc64
BuildRequires: vpkg-SUNWzlibx
 %else
BuildRequires: vpkg-SUNWzlib
 %endif
%else
BuildRequires: zlib-devel prngd
%endif
Requires: openssl >= 0.9.7-6debug
%ifos solaris2.9
 %ifarch sparc64
Requires: vpkg-SUNWzlibx
 %else
Requires: vpkg-SUNWzlib
 %endif
%else
Requires: zlib
Requires: prngd
%endif
BuildConflicts: openssl-static

%description
OpenSSH is based on the last free version of Tatu Ylonen's sample
implementation with all patent-encumbered algorithms removed (to 
external libraries), all known security bugs fixed, new features 
reintroduced and many other clean-ups.  OpenSSH has been created by
Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt,
and Dug Song. It has a homepage at http://www.openssh.com/  (from README)

This version of openssh is configured to enable a non-setuid client.

An evil Rutgers "sshd_password" with PAM password support is included.
The OpenSSH project maintains keyboard-interactive/PAM support, found in
"sshd." sshd_password is only recommended if you have older clients that
do not support keyboard-interactive, as it is locally maintained and not
subject to the same level of peer review. Also please note that config
files are not necessarily compatible between sshd and sshd_password. See
sshd(8) -f option.

%prep
%setup -q
PATH="/usr/local/gnu/bin:$PATH"
export PATH

%patch0 -p1

%build

%define common_configure_options --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --disable-suid-ssh --with-tcp-wrappers --without-zlib-version-check

# This whole construct is fairly evil.

CC="cc"
CFLAGS="-KPIC -xO5 -xdepend -dalign -xlibmil -xunroll=5"
LDFLAGS='-L/usr/local/lib -R/usr/local/lib -lpam'
CPPFLAGS='-I/usr/local/include -DCUSTOM_SYS_AUTH_PASSWD'
export CC CFLAGS LDFLAGS CPPFLAGS

### phase 1: patch, then build WITHOUT pam

/usr/local/gnu/bin/patch -p1 < %{SOURCE1}

### Once patches, we must build without pam!

%ifos solaris2.9
./configure %{common_configure_options} \
--without-prngd --without-rand-helper --without-pam
%else
./configure %{common_configure_options} \
--with-prngd-socket=/var/run/urandom --without-pam
%endif

/usr/local/gnu/bin/gmake sshd 

# Save the sshd!
cp sshd sshd_password

# Clean up to try again.
gmake distclean

### phase 2: UNpatch, then build WITH pam

# Remove the patch.
/usr/local/gnu/bin/patch --reverse -p1 < %{SOURCE1}

# fix FLAGS back to sanity.
LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
CPPFLAGS='-I/usr/local/include'
export CC CFLAGS LDFLAGS CPPFLAGS

# Lather, rinse, repeat, with pam.
%ifos solaris2.9
./configure %{common_configure_options} \
--without-prngd --without-rand-helper --with-pam
%else
./configure %{common_configure_options} \
--with-prngd-socket=/var/run/urandom --with-pam
%endif

gmake 

%install
rm -fr %{buildroot}
# We need to use Sun strip:
PATH="/usr/ccs/bin:/usr/local/gnu/bin:$PATH"
export PATH
mkdir -p %{buildroot}/etc/init.d
cp sshd-ctl %{buildroot}/etc/init.d/openssh
chmod 755 %{buildroot}/etc/init.d/openssh
gmake install DESTDIR=%{buildroot}
cp sshd_password %{buildroot}/usr/local/sbin
chmod 755 %{buildroot}/usr/local/sbin/sshd_password
sed "s/#X11Forwarding no/X11Forwarding yes/" %{buildroot}/usr/local/etc/sshd_config > %{buildroot}/usr/local/etc/sshd_config2
mv %{buildroot}/usr/local/etc/sshd_config2 %{buildroot}/usr/local/etc/sshd_config
%ifnos solaris2.9
cp ssh_prng_cmds %{buildroot}/usr/local/etc/
%endif

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/bin
%config(noreplace) /usr/local/etc/*
/usr/local/libexec
/usr/local/man
/usr/local/sbin
/usr/local/share
%config /etc/init.d/openssh

%post
cat <<EOF
OpenSSH Notes:

1) Keys are required for this machine to act as a host.
   To generate new keys, do this:
        cd /usr/local/bin
        ./ssh-keygen -t rsa1 -f /usr/local/etc/ssh_host_key -N ""
        ./ssh-keygen -t rsa -f /usr/local/etc/ssh_host_rsa_key -N ""
        ./ssh-keygen -t dsa -f /usr/local/etc/ssh_host_dsa_key -N ""

2) If you have an existing configuration the files have not been
   overwritten--look above for RPM warning messages to this effect.
   If this is a fresh install, default configuration files have been
   put down in /usr/local/etc and are active.

3) @@@ IF YOU ARE INSTALLING OPENSSH 3.4 FOR THE FIRST TIME YOU @@@
   @@@    MUST MAKE CHANGE TO ENABLE PRIVILEGE SEPERATION       @@@

	create user 'sshd'

   @@@     SSHD WILL NOT START UNLESS THESE CHANGES ARE MADE    @@@

4) The OpenSSH maintainers would like to remind you that a security hole
in a dependent library may result in a security hole in OpenSSH.
In particular, check for Sun patches for zlib and any other libraries that
openssh links against. The OpenSSH maintainers also say:

WARNING:
If PATH is defined in /etc/default/login, ensure the path to scp is included,
otherwise scp will not work.

5) If you are having trouble with older clients, read the full package
description.

%ifnos solaris2.9
6) ssh requires prngd to be running with a socket in /var/run.  Run
        prngd /var/run/urandom
   as root. (NOTE: Only necessary on Solaris 2.8 and earlier.)
%endif
EOF
