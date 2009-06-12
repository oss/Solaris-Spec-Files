%define libexpat_version 1.5.2

Name: 		expat
Version: 	2.0.1
Release: 	2
Group:          System Environment/Libraries
License: 	MIT/X
URL: 		http://expat.sourceforge.net
Source: 	http://download.sourceforge.net/expat/expat-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:        XML 1.0 parser

%description
Expat is an XML 1.0 parser written in C by James Clark.  It aims to be
fully conforming. It is currently not a validating XML parser.

%package devel  
Group:		System Environment/Libraries
Requires: 	expat = %{version}-%{release}

Summary:	Expat development files

%description devel
This package contains files needed for building applications that 
use Expat.

%package static
Group:		System Environment/Libraries
Requires:	expat-devel = %{version}-%{release}

Summary:        Expat static libraries

%description static
This package contains the Expat static libraries.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=%{_prefix}
gmake -j3

rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

cd %{buildroot}%{_libdir}
ln -s libexpat.so.%{libexpat_version} libexpat.so.0
ln -s libexpat.so.%{libexpat_version} libexpat.so.0.5.0
ln -s libexpat.so.%{libexpat_version} libexpat.so.0.1.0
cd $RPM_BUILD_DIR/%{name}-%{version}

%ifarch sparc64
CFLAGS="-xtarget=ultra -xarch=v9" CXXFLAGS=${CFLAGS}
CPPFLAGS="-I/usr/local/include/sparcv9"
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" 
export CFLAGS CXXFLAGS CPPFLAGS LDFLAGS

gmake clean
./configure
gmake -j3
%endif

%install
%ifarch sparc64

%{__install} -d %{buildroot}%{_bindir}/sparcv9
%{__install} -d %{buildroot}%{_libdir}/sparcv9

%{__install} -m 0755 xmlwf/.libs/xmlwf %{buildroot}%{_bindir}/sparcv9/
%{__install} -m 0755 .libs/libexpat.so* %{buildroot}%{_libdir}/sparcv9/
%{__install} -m 0644 .libs/libexpat.a %{buildroot}%{_libdir}/sparcv9/
%{__install} -m 0755 .libs/libexpat.la %{buildroot}%{_libdir}/sparcv9/

cd %{buildroot}%{_libdir}/sparcv9
ln -s libexpat.so.%{libexpat_version} libexpat.so.0
ln -s libexpat.so.%{libexpat_version} libexpat.so.0.5.0
ln -s libexpat.so.%{libexpat_version} libexpat.so.0.1.0
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING Changes README 
%doc doc/reference.html doc/style.css
%{_bindir}/xmlwf
%{_libdir}/*.so.*
%{_mandir}/man1/*
%ifarch sparc64
%{_bindir}/sparcv9/*
%{_libdir}/sparcv9/*.so.*
%endif

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%ifarch sparc64
%{_libdir}/sparcv9/*.so
%{_libdir}/sparcv9/*.la
%endif

%files static
%defattr(-, root, root)
%{_libdir}/*.a
%{_libdir}/sparcv9/*.a

%changelog
* Fri Jun 12 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.0.1-2
- Moved .la files to devel package
- Cleaned things up somewhat
* Thu Aug 23 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.1-1
- Updated to 2.0.1
* Tue Aug 22 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0-1
- Fixed up spec file, switched to Sun CC, enabled backwards compatibility with 1.95
