Summary:	Apache Portable Runtime
Name:		apr-util
Version:	1.3.4
Release:        2
License:	Apache
Group:		System/Utilities
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	sqlite, sqlite-devel, sqlite-lib, libiconv, expat, db4 >= 4.7.25, apr
BuildRequires:	sqlite, sqlite-devel, sqlite-lib, libiconv-devel, expat-devel, db4-devel >= 4.7.25, apr-devel

%description
The mission of the Apache Portable Runtime (APR) project is to create and 
maintain software libraries that provide a predictable and consistent 
interface to underlying platform-specific implementations. The primary 
goal is to provide an API to which software developers may code and be 
assured of predictable if not identical behaviour regardless of the 
platform on which their software is built, relieving them of the need to 
code special-case conditions to work around or take advantage of 
platform-specific deficiencies or features.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls --with-apr=/usr/local --with-expat=/usr/local --with-iconv=/usr/local --with-ldap=ldap --with-ldap-lib=/usr/local/lib --with-ldap-include=/usr/local/include --with-berkeley-db=/usr/local --with-gdbm=/usr/local

gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libaprutil-1.la
rm -f %{buildroot}%{_libdir}/apr-util-1/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README* NOTICE LICENSE CHANGES
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/apr-util-1/*.so

%files devel
%defattr(-,root,root)
%{_libdir}/aprutil.exp
%{_libdir}/*.a
%{_libdir}/apr-util-1/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.4-2
- Respin against BDB 4.7
* Tue Aug 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.4-1
- Added doc entry, updated to 1.3.4
* Thu Jun 05 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.0-1
- Updated to version 1.3.0
* Wed Jan 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.2.12-1
- Updated to the latest version, removed apr-util-expatfix.patch 
* Mon Aug 20 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.8-4
- Updated to the latest version.
* Wed Oct 11 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.7-1
- Initial Rutgers release
