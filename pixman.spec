Name:		pixman
Version:	0.15.16
Release:	1
Group:		System Environment/Libraries
License:	MIT
URL:            http://cairographics.org
Source:         http://cairographics.org/releases/pixman-%{version}.tar.gz
Patch:		pixman-0.15.16-timers.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	autoconf automake libtool-devel pkgconfig

Summary:        A pixel manipulation library

%description
The pixel manipulation library for X and cairo.

%package devel
Group:		System Environment/Libraries
Requires:	pixman = %{version}-%{release}

Summary:        Pixman development files

%description devel 
This package contains the files needed for building applications 
that use pixman. 

%prep
%setup -q
%patch -p0
autoreconf
 
%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure			\
	--prefix=%{_prefix} 	\
	--disable-static 	\
	--disable-timers	

gmake -j3 LIBTOOL="%{_bindir}/libtool"

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot} LIBTOOL="%{_bindir}/libtool"

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README AUTHORS COPYING 
%doc NEWS TODO ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root) 
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jul 15 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.15.16-1
- Updated to version 0.15.16
- Code for timer support uses gnu inline assembly, so disable timers

* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.13.2-1
- Updated to version 0.13.2
- No longer build static libraries
- Removed patch (no longer needed)

* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.11.4-1
- Initial release, needed for new version of cairo.
