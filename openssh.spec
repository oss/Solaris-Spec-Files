%include perl-header.spec

Name: openssh
Version: 3.2.3p1
Release: 2ru
Summary: Secure Shell - telnet alternative (and much more)
Group: Cryptography
License: BSD
Source: %{name}-%{version}.tar.gz
Patch0: %{name}-3.0.2p1.patch
Patch1: sshd-ctl.patch
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: perl > 5.0.0
BuildRequires: openssl patch make
%ifos solaris2.9
BuildRequires: vpkg-SUNWzlibx
%else
BuildRequires: zlib-devel prngd
%endif
# %if %{max_bits} == 64
# BuildRequires: vpkg-SUNWzlibx
# %endif
Requires: openssl
%ifos solaris2.9
Requires: vpkg-SUNWzlibx
%else
Requires: zlib
Requires: prngd
%endif

%description
OpenSSH is based on the last free version of Tatu Ylonen's sample
implementation with all patent-encumbered algorithms removed (to 
external libraries), all known security bugs fixed, new features 
reintroduced and many other clean-ups.  OpenSSH has been created by
Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt,
and Dug Song. It has a homepage at http://www.openssh.com/  (from README)

This version of openssh is patched to enable a non-setuid client.

%prep
%setup -q
PATH="/usr/local/gnu/bin:$PATH"
export PATH

%patch0 -p1
%patch1 -p1

%build
#%if %{max_bits} == 64
# no 64-bit Rutgers PAM, so we build 32 bits only.
# CC="/opt/SUNWspro/bin/cc -xarch=v9" \
#   ./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl/sparcv9 \
#   --with-pam --with-prngd-socket=/var/run/urandom
#./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
#  --with-prngd-socket=/var/run/urandom --disable-suid-ssh
#%else

%ifos solaris2.9
./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
   --disable-suid-ssh
%else
./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
  --with-prngd-socket=/var/run/urandom --disable-suid-ssh
%endif

/usr/local/gnu/bin/gmake

%install
rm -fr %{buildroot}
# We need to use Sun strip:
PATH="/usr/ccs/bin:/usr/local/gnu/bin:$PATH"
export PATH
mkdir -p %{buildroot}/etc/init.d
cp sshd-ctl %{buildroot}/etc/init.d/openssh
chmod 755 %{buildroot}/etc/init.d/openssh
gmake install DESTDIR=%{buildroot}
cp ssh_prng_cmds %{buildroot}/usr/local/etc/


# move config files to xxx.rpm so as not to stomp on existing config files
cd %{buildroot}/usr/local/etc
#mv ssh_config ssh_config.rpm
#mv ssh_prng_cmds ssh_prng_cmds.rpm
#mv sshd_config sshd_config.rpm

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/bin
%config(noreplace) /usr/local/etc
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

%ifnos solaris2.9
3) ssh requires prngd to be running with a socket in /var/run.  Run
        prngd /var/run/urandom
   as root. (NOTE: Only necessary on Solaris 2.8 and earlier.)
%endif
EOF

%changelog
* Thu Dec 13 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to OpenSSH 3.0.2p1
