Summary: A flexible, stable and highly-configurable FTP Server.
Name: proftpd
Version: 1.2.8p
Release: 2
Group: System Environment/Daemons
Copyright: GPL
URL: http://www.proftpd.org/
Source: ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
Source1: proftpd.conf
Source2: proftpd.init
Source3: proftpd-xinetd
Source4: proftpd.logrotate
Source5: welcome.msg
#Patch0: proftpd-1.2.6-userinstall.patch
Patch0: proftpd-1.2.8-mkstemp.patch
Buildroot: %{_tmppath}/%{name}-root
Provides: ftpserver

%description
ProFTPD is an enhanced FTP server with a focus toward simplicity, security,
and ease of configuration. It features a very Apache-like configuration
syntax, and a highly customizable server infrastructure, including support for
multiple 'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This package defaults to the standalone behaviour of ProFTPD, but all the
needed scripts to have it run by xinetd instead are included.

%prep
%setup -q -n proftpd-1.2.8
%patch0 -p1 
#%patch1 -p0 -b .nsl

%build
#CFLAGS="" CXXFLAGS="" FFLAGS=""
LD_RUN_PATH="/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/ssl/include" CC=/opt/SUNWspro/bin/cc \
install_user=`/usr/local/gnu/bin/id -un` \
install_group=`/usr/local/gnu/bin/id -gn` \
./configure --with-modules=mod_pam --with-modules=mod_tls --prefix=/usr/local
#./configure --prefix=/usr/local
make

%install
rm -rf %{buildroot}
echo exec gmake install
gmake install prefix="$RPM_BUILD_ROOT/usr/local" \
 rundir=%{buildroot}%{_localstatedir}/run/proftpd
install -D -m 644 contrib/dist/rpm/ftp.pamd %{buildroot}%{_sysconfdir}/pam.d/ftp
#install -D -m 640 %{SOURCE1} %{buildroot}%{_sysconfdir}/proftpd.conf
#install -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/rc.d/init.d/proftpd
#install -D -m 640 %{SOURCE3} %{buildroot}%{_sysconfdir}/xinetd.d/proftpd
#install -D -m 640 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/proftpd
#install -D -m 644 %{SOURCE5} %{buildroot}/var/ftp/welcome.msg
#mkdir -p %{buildroot}/var/ftp/pub
#touch %{buildroot}%{_sysconfdir}/ftpusers

%post
cat<<EOF
ProFTPd is not configured. Configure before use.
Instructions for configuring TLS: /usr/local/doc/proftpd-%{version}/README.TLS
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING CREDITS ChangeLog NEWS READ*
%doc doc/* sample-configurations
%doc contrib/README.ratio contrib/mod_wrap.html
%dir %{_localstatedir}/run/proftpd
%config(noreplace) %{_sysconfdir}/proftpd.conf
#%config(noreplace) %{_sysconfdir}/xinetd.d/proftpd
#%config %{_sysconfdir}/ftpusers
#%config %{_sysconfdir}/pam.d/ftp
#%config %{_sysconfdir}/logrotate.d/proftpd
#%{_sysconfdir}/rc.d/init.d/proftpd
%{_mandir}/*/*
%{_bindir}/*
%{_sbindir}/*
#/var/ftp

%changelog
* Fri Dec 14 2001 Edward S. Marshall <esm@logic.net>
- Update to 1.2.4
- Borrowed some information from the "official" ProFTPD spec file.
- Updated ProFTPD download URL.

* Wed Apr 25 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.2rc2.

* Mon Apr  1 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.2rc1.

* Tue Mar 20 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added a DenyFilter to prevent a recently discovered DOS attack.
  This is only useful for fresh installs since the config file is not
  overwritten.

* Fri Mar  2 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Upgraded to 1.2.1.
- New init script (added condrestart).

* Tue Feb 27 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Upgraded to 1.2.0 final.

* Tue Feb  6 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Upgraded to 1.2.0rc3 (at last a new version!)
- Modified the spec file to support transparent upgrades

* Wed Nov  8 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Upgraded to the latest CVS to fix the "no PORT command" bug
- Fixed the ftpuser creation script
- Modified the default config file to easily change to an anonymous
  server

* Sun Oct 15 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
  [proftpd-1.2.0rc2-2]
- Updated the spec file and build process for RedHat 7.0
- Added xinetd support
- Added logrotate.d support

* Fri Jul 28 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
  [proftpd-1.2.0rc2-1]
- Upgraded to 1.2.0rc2

- Upgraded to 1.2.0rc1
* Sat Jul 22 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
  [proftpd-1.2.0rc1-1]
- Upgraded to 1.2.0rc1
- Re-did the whole spec file (it's hopefully cleaner now)
- Made a patch to be able to build the RPM as an other user than root
- Added default pam support (but without /etc/shells check)
- Rewrote the rc.d script (mostly exit levels and ftpshut stuff)
- Modified the default configuration file to not display a version number
- Changed the package to standalone in one single RPM easily changeable
  to inetd (for not-so-newbie users)
- Fixed the ftpusers generating shell script (missing "nu"s for me...)
- Removed mod_ratio (usually used with databases modules anyway)
- Removed the prefix (relocations a rarely used on non-X packages)
- Gzipped the man pages

* Thu Oct 03 1999 O.Elliyasa <osman@Cable.EU.org>
- Multi package creation.
  Created core, standalone, inetd (&doc) package creations.
  Added startup script for init.d
  Need to make the "standalone & inetd" packages being created as "noarch"
- Added URL.
- Added prefix to make the package relocatable.

* Wed Sep 08 1999 O.Elliyasa <osman@Cable.EU.org>
- Corrected inetd.conf line addition/change logic.

* Sat Jul 24 1999 MacGyver <macgyver@tos.net>
- Initial import of spec.

