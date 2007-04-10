%include perl-header.spec
 

Name: openssh
Version: 4.6p1
Release: 2
Summary: Secure Shell - telnet alternative (and much more)
Group: Cryptography
License: BSD
URL: http://www.openssh.org/
Packager: Eric Rivas <kc2hmv@nbcs.rutgers.edu>
Distribution: RU-Solaris
Vendor: NBCS-OSS
Source: %{name}-%{version}.tar.gz
Patch0: sshd-ctl.patch
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: perl > 5.0.0
BuildRequires: openssl patch make tcp_wrappers
%ifos solaris2.9
 %ifarch sparc64
BuildRequires: vpkg-SUNWzlibx
 %else
BuildRequires: vpkg-SUNWzlib
 %endif
%else
BuildRequires: zlib-devel prngd
%endif
Requires: openssl >= 0.9.8
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
OpenSSH is based on the last free version of Tatu Ylonens sample
implementation with all patent-encumbered algorithms removed (to 
external libraries), all known security bugs fixed, new features 
reintroduced and many other clean-ups.  OpenSSH has been created by
Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt,
and Dug Song. It has a homepage at http://www.openssh.com/  (from README)

This version of openssh is patched to enable a non-setuid client.

%prep
%setup -q

%patch0 -p1

%build

CC="/opt/SUNWspro/bin/cc"
CXX="/opt/SUNWspro/bin/CC"
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/ssl/bin"
#PATH="/usr/local/gnu/bin:$PATH"
#CFLAGS="-KPIC -xO5 -xdepend -dalign -xlibmil -xunroll=5"
LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
CPPFLAGS='-I/usr/local/include'
export CC LDFLAGS CPPFLAGS PATH

%ifos solaris2.9
./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
  --without-prngd --without-rand-helper --disable-suid-ssh --with-tcp-wrappers \
--without-zlib-version-check
%else
./configure --prefix=/usr/local --with-ssl-dir=/usr/local/ssl --with-pam \
  --with-prngd-socket=/var/run/urandom --disable-suid-ssh --with-tcp-wrappers \
--without-zlib-version-check
%endif

make


%install
rm -fr %{buildroot}
# We need to use Sun strip:
mkdir -p %{buildroot}/etc/init.d
cp sshd-ctl %{buildroot}/etc/init.d/openssh
chmod 755 %{buildroot}/etc/init.d/openssh

make install DESTDIR=%{buildroot}

sed "s/#X11Forwarding no/X11Forwarding yes/" %{buildroot}/usr/local/etc/sshd_config > %{buildroot}/usr/local/etc/sshd_config2
mv %{buildroot}/usr/local/etc/sshd_config2 %{buildroot}/usr/local/etc/sshd_config

sed "s/#UsePAM no/UsePAM yes/" %{buildroot}/usr/local/etc/sshd_config > %{buildroot}/usr/local/etc/sshd_config.modified
mv %{buildroot}/usr/local/etc/sshd_config.modified %{buildroot}/usr/local/etc/sshd_config

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
/usr/local/sbin
/usr/local/share/man/man1/*
/usr/local/share/man/man5/*
/usr/local/share/man/man8/*
/usr/local/share/Ssh.bin
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

3) @@@ IF YOU ARE INSTALLING OPENSSH FOR THE FIRST TIME YOU @@@
   @@@  MUST MAKE CHANGE TO ENABLE PRIVILEGE SEPERATION     @@@

	create user 'sshd'

   @@@   SSHD WILL NOT START UNLESS THESE CHANGES ARE MADE  @@@

4) The OpenSSH maintainers would like to remind you that a security hole
in a dependent library may result in a security hole in OpenSSH.
In particular, check for Sun patches for SUNWzlib if you have it installed,
as many OpenSSH programs link against /usr/lib/libz.so.

%ifnos solaris2.9
5) ssh requires prngd to be running with a socket in /var/run.  Run
        prngd /var/run/urandom
   as root. (NOTE: Only necessary on Solaris 2.8 and earlier.)
%endif
EOF

%changelog
* Tue Dec 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.5p1-2
 - Bumped for openssl 0.9.8
* Wed Nov  8 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 4.5p1-1
 - Upgraded to OpenSSH 4.5p1
* Thu Sep 28 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 4.4p1
* Thu Jul  3 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 4.3p2
* Thu Feb  9 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 4.3p1
* Tue Sep  6 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 4.2p1
* Fri Jun 17 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 4.1p1
* Thu Apr 21 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 4.0p1
* Thu Dec 13 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
 - Upgraded to OpenSSH 3.0.2p1
