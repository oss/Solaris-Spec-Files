%define name    jdresolve
%define	version	0.6.1
%define release 2
%define prefix  /usr/local

Summary: jdresolve resolves IP addresses into hostnames 

Name: %{name}
Version: %{version}
Release: %{release}

Copyright: GPL
Group: Development/Languages
Source: http://www.jdrowell.com/files/%{name}-%{version}.tar.bz2
Url: http://www.jdrowell.com/Linux/Projects/jdresolve
Packager: John D. Rowell <me@jdrowell.com>

BuildRoot: /var/tmp/%{name}-root
Requires: perl >= 5.004, perl-Net-DNS >= 0.12

%description

%changelog
* Wed Jun 28 2000 John D. Rowell <me@jdrowell.com>
- version 0.6.1
- Fixed "oops" assertion bug
- Improved performance
- New "-p"/"--progress" option

* Sat Jun 17 2000 John D. Rowell <me@jdrowell.com>
- version 0.6.0
- Improved performance (lines/s)
- Better line caching algorithm
- Reduced memory footprint
- The code is now fully commented
- A new ./configure script (locates Perl, Net::DNS, etc)
  ...more... (see CHANGELOG)

* Thu Aug 26 1999 John D. Rowell <me@jdrowell.com>
- version 0.5.2
- fixed memory leak when the --database option was not in use
- fixed warning messages when the --recursive option was not in use

* Mon Aug 16 1999 John D. Rowell <me@jdrowell.com>
- version 0.5.1
- fixed warning messages on FreeBSD
- added jdresolve-mergedb and jdresolve-unresolved utils

* Wed Jul 27 1999 John D. Rowell <me@jdrowell.com>
- version 0.5
- Added database support (--database and jdresolve-dumpdb)

* Wed Jul 14 1999 John D. Rowell <me@jdrowell.com>
- First build (v0.4).


%prep

%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man1
sed "s/\/usr\/bin\/perl/\/usr\/bin\/env perl/" jdresolve > $RPM_BUILD_ROOT%{prefix}/bin/jdresolve
sed "s/\/usr\/bin\/perl/\/usr\/bin\/env perl/" rhost > $RPM_BUILD_ROOT%{prefix}/bin/rhost
#cp jdresolve rhost $RPM_BUILD_ROOT%{prefix}/bin
#gzip jdresolve.1
#gzip rhost.1
cp jdresolve.1.gz rhost.1.gz $RPM_BUILD_ROOT%{prefix}/man/man1
#make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG  COPYING  CREDITS  INSTALL  README  TODO
/usr/local/bin/jdresolve
/usr/local/bin/rhost
/usr/local/man/man1/jdresolve.1.gz
/usr/local/man/man1/rhost.1.gz


