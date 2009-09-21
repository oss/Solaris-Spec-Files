%define aprver 1

Summary:	Apache Portable Runtime
Name:		apr
Version:	1.3.8
Release:        1
License:	Apache
Group:		System Environment/Utilities
Source:		http://apache.g5searchmarketing.com/apr/apr-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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
Summary:	APR development files
Group:		System Environment/Libraries
Requires:	apr = %{version}-%{release}

%description devel
This package contains files needed for building applications that use APR.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}					\
	--with-installbuilddir=%{_libdir}/apr-%{aprver}/build	\
	--disable-static					\
	--disable-nls

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root , root)
%doc NOTICE LICENSE CHANGES
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/*config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.exp
%{_libdir}/apr-%{aprver}/
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Sep 21 2009 Dan Gopstein <dgop@nbcs.rutgers.edu> - 1.3.8-1
- Updated to version 1.3.8
* Tue Jun 18 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.5-1
- Updated to version 1.3.5
- No longer build static libraries
- Put .la file in devel package
* Tue Aug 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.3.3-1
- Switched to gmake, added doc entry, removed libapr-1.la, updated to 1.3.3
* Thu Jun 05 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.3.0-1
- Updated to 1.3.0
* Wed Jan 02 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.12-1
- Updated to 1.2.12
* Fri Nov 02 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.11-1
- Updated to 1.2.11
* Wed Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.9-2
- Updated to 1.2.9
* Wed Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.7-1
- Updated to 1.2.8
* Wed Oct 11 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.7-1
- Initial Rutgers release
