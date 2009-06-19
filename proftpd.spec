Name:		proftpd
Version:	1.3.2
Release:	5
Group:		System Environment/Daemons
License:	GPL
URL:		http://www.proftpd.org/
Source0:	ftp://ftp.proftpd.org/distrib/source/proftpd-%{version}.tar.bz2
Source1:	proftpd.conf
Source2:	proftpd.init
Source3:	proftpd-xinetd
Source4:	proftpd.logrotate
Source5:	welcome.msg
Patch:		proftpd-1.3.2-oob.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Provides:	ftpserver

Summary:	A flexible, stable and highly-configurable FTP Server

%description
ProFTPD is an enhanced FTP server with a focus toward simplicity, security,
and ease of configuration. It features a very Apache-like configuration
syntax, and a highly customizable server infrastructure, including support for
multiple 'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This package defaults to the standalone behaviour of ProFTPD, but all the
needed scripts to have it run by xinetd instead are included.

%package devel
Summary:	ProFTPD development files
Group:		System Environment/Daemons
Requires:	proftpd = %{version}-%{release}

%description devel
This package contains files needed to build applications that use ProFTPD.

%prep
%setup -q 
%patch -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}	\
	--mandir=%{_mandir}	\
	--with-modules=mod_pam	\
	--with-modules=mod_tls	\
	--disable-ipv6		\
	--disable-nls

gmake -j3

%install
rm -rf %{buildroot}

gmake install \
	DESTDIR=%{buildroot} 			\
	rundir=%{_localstatedir}/run/proftpd	\
	INSTALL_USER=`%{__id} -un`      	\
	INSTALL_GROUP=`%{__id} -gn`     

%{__install} -D -m 640 %{SOURCE1} doc/proftpd.conf
%{__install} -D -m 755 %{SOURCE2} doc/proftpd.init
%{__install} -D -m 640 %{SOURCE3} doc/proftpd-xinetd
%{__install} -D -m 640 %{SOURCE4} doc/proftpd.logrotate
%{__install} -D -m 644 %{SOURCE5} doc/welcome.msg

%{__install} -d %{buildroot}%{_localstatedir}/proftpd

%post
cat << EOF

ProFTPD is not configured. It must be configured before use.

Instructions for configuring TLS are available at: 

	%{_docdir}/proftpd-%{version}/contrib/mod_tls.html

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)

%doc COPYING CREDITS ChangeLog NEWS READ*
%doc doc/* sample-configurations
%doc contrib/README.ratio contrib/dist/rpm/ftp.pamd

%config(noreplace) %{_sysconfdir}/proftpd.conf

%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*
%{_localstatedir}/proftpd/
%{_localstatedir}/run/proftpd/

%files devel
%defattr(-, root, root)
%{_includedir}/proftpd/
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jun 19 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.2-5
- Replaced patch with a working one
- Actually apply the patch...

* Thu Jun 18 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.2-4
- Added patch in attempt to fix "error setting SO_OOBINLINE" errors
- Cleaned up spec file somewhat

* Thu Jun 18 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3.2-3
- Disabled ipv6

* Fri May 01 2009 Dave Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.3.2-2
- Bumped release

* Thu Apr 30 2009 Dave Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.3.2-1
- Bump to 1.3.2
- build against openssl-0.9.8h for stable

* Mon Nov 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1
- Bump to 1.3.1

* Thu Dec 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
- Updated to 1.3.0a and changed for OpenSSL 0.9.8

* Thu Jun 08 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
- Updated to 1.3.0

* Thu Apr 06 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
- Updated to 1.3.0rc5

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

