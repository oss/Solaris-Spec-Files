Name:		liboil
Version:	0.3.16
Release:        1
License:	GPL
Group:		System Environment/Libraries
Source:		http://liboil.freedesktop.org/download/liboil-%{version}.tar.gz
URL:		http://liboil.freedesktop.org
Patch:		liboil-0.3.15-stdint.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes:	liboil-static

Summary:        A library of simple functions that are optimized for various CPUs

%description
Liboil is a library of simple functions that are optimized for various 
CPUs. These functions are generally loops implementing simple 
algorithms, such as converting an array of N integers to floating-point 
numbers or multiplying and summing an array of N numbers. Such functions 
are candidates for significant optimization using various techniques, 
especially by using extended instructions provided by modern CPUs 
(Altivec, MMX, SSE, etc.).

%package devel 
Group:		System Environment/Libraries
Requires: 	liboil = %{version}-%{release}
Summary:        liboil development files

%description devel
This package contains the files needed to build applications that use
liboil.

%package doc
Group:		System Environment/Libraries
Requires: 	liboil = %{version}-%{release}
Summary:        Additional liboil documentation

%description doc
This package contains the gtk-doc documentation for liboil.

%prep
%setup -q
cd examples/jpeg
%patch -p0
cd ../..

%build
PATH="/opt/SUNWspro/bin:/opt/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}	\
	--disable-static 	\
	--disable-nls

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS BUG-REPORTING COPYING NEWS README
%{_bindir}/*
%{_libdir}/*so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc 
%defattr(-, root, root)
%docdir %{_datadir}/gtk-doc/html/liboil/
%{_datadir}/gtk-doc/html/liboil/

%changelog
* Tue May 26 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.3.16-1
- Updated to version 0.3.16
- No longer build static libraries
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.3.15-1
- updated
- added doc and static packages
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.3.8-1
- Initial Rutgers release
