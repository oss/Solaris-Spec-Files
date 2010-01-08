%define apru_version 1

Name:		apr-util
Version:	1.3.9
Release:        2
Group:		System Environment/Libraries
License:	Apache
URL:		http://apr.apache.org
Source:		http://www.hightechimpact.com/Apache/apr/apr-util-%{version}.tar.gz
Patch0:		%{name}-%{version}-db48_support.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	sqlite-devel, libiconv-devel, expat-devel, apr-devel
BuildRequires:	freetds-devel, freetds-lib, gdbm
BuildRequires:	db4-devel >= 4.7.25, openldap-devel >= 2.4.16

Requires:	db4 >= 4.7.25, openldap >= 2.4.16

Summary:	Apache Portable Runtime Utility library

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
Group:		System Environment/Libraries
Requires: 	apr-util = %{version}-%{release}

Summary:	apr-util devlopment files

%description devel
This package contains files needed for building applications that use apr-util.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

autoconf
./configure \
	--prefix=%{_prefix}	\
	--with-apr=%{_prefix}	\
	--with-ldap 		\
	--with-berkeley-db=%{_prefix}	\
	--with-gdbm		\
	--with-sqlite3		\
	--without-sqlite2	\
	--with-freetds		

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

# Remove unpackaged files, static libraries
rm -f %{buildroot}%{_libdir}/apr-util-%{apru_version}/*.la
find %{buildroot} -name '*.a' -exec rm -f '{}' \;

# Remove the reference to the static libaprutil from the .la file
sed -i '/^old_library/s,libapr.*\.a,,' %{buildroot}%{_libdir}/libapr*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root , root)
%doc README* NOTICE LICENSE CHANGES
%{_libdir}/*.so.*
%{_libdir}/apr-util-%{apru_version}/

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_bindir}/*config
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/aprutil.exp
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 07 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 1.3.9-2
- Fixed to compile against db4.8 (had to patch autoconf files)
* Mon Sep 18 2009 Dan Gopstein <dgop@nbcs.rutgers.edu> - 1.3.9-1
- Updated to version 1.3.9
* Fri Jun 19 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.7-1
- Updated to version 1.3.7
- Fixed a few things
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
