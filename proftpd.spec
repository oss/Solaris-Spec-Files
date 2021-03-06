Name:		proftpd
Version:	1.3.3e
Release:	6
Group:		System Environment/Daemons
License:	GPL
URL:		http://www.proftpd.org/
Source0:	ftp://ftp.proftpd.org/distrib/source/proftpd-%{version}.tar.bz2
Source1:	proftpd.conf
Source2:	proftpd.init
Source3:	proftpd-xinetd
Source4:	proftpd.logrotate
Source5:	welcome.msg

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  openssl = 0.9.8zf
Requires:       openssl = 0.9.8zf
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

%build
CFLAGS="-I/usr/local/ssl/include/"
export CFLAGS 
LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -zdefs"
export LDFLAGS 

# We are not using the default %%configure macro since we don't want
# -Bdirect in LDFLAGS. This confuses the linker and libsendfile.so doesn't
# link properly and the proftpd daemon does not work.

./configure \
        --prefix=%{_prefix} \
	--mandir=%{_mandir} \
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
%defattr(-, root, root, -)

%doc COPYING CREDITS ChangeLog NEWS READ*
%doc doc/* sample-configurations
%doc contrib/README.ratio contrib/dist/rpm/ftp.pamd

%config(noreplace) %{_sysconfdir}/proftpd.conf

%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*
%{_localstatedir}/proftpd/
#{_localstatedir}/run/proftpd/

%files devel
%defattr(-, root, root, -)
%{_includedir}/proftpd/
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Mar 23 2015 Aedan Dispenza <ad778@nbcs.rutgers.edu> - 1.3.3e-6
- Update to comply with openssl-0.9.8zf

* Wed Feb 18 2015 Aedan Dispenza <ad778@nbcs.rutgers.edu> - 1.3.3e-5
- Update to comply with openssl-0.9.8ze

* Mon Dec 01 2014 Aedan Dispenza <ad778@nbcs.rutgers.edu> - 1.3.3e-4
- Update to comply with openssl-0.9.8zc

* Mon Sep 29 2014 Aedan Dispenza <ad778@nbcs.rutgers.edu> - 1.3.3e-3
- Update to fix openssl errors

* Mon Aug 22 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 1.3.3e-2
- Respin (version or rpm2php error)

* Tue Aug 16 2011 Phillip Quiza <pquiza@nbcs.rutgers.edu> - 1.3.3e-1
- Updated to 1.3.3e
- Changed openssl requirement to 0.9.8r to resovle dependency requirements
  when updating openssl package

* Wed Dec 15 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.3.3c-2
- Add Requires on specific openssl version
- Don't pass -Bdirect to the linker. Otherwise the executable can't
  find libsendfile.so

* Fri Dec 10 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.3.3c-1
- Update to 1.3.3c

* Wed Oct 21 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.3.2c-1
- Update to 1.3.2c

* Wed Oct 21 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.3.2b-1
- Update to 1.3.2b
- Remove oob patch. It looks upstreamed.

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

