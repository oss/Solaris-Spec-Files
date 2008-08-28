Summary:	a library of simple functions that are optimized for various CPUs
Name:		liboil
Version:	0.3.15
Release:        1
Copyright:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-0.3.15-stdint.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Liboil is a library of simple functions that are optimized for various 
CPUs. These functions are generally loops implementing simple 
algorithms, such as converting an array of N integers to floating-point 
numbers or multiplying and summing an array of N numbers. Such functions 
are candidates for significant optimization using various techniques, 
especially by using extended instructions provided by modern CPUs 
(Altivec, MMX, SSE, etc.).

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%package static
Summary: Static libraries for %{name}
Group: Application/Libraries
Requires: %{name} = %{version}

%description static
This package contains the static libraries for building applications with %{name}

%package doc
Summary: %{name} documentation
Group: Application/Libraries
Requires: %{name} = %{version}

%description doc
This package consists of the %{name} documentation

%prep
%setup -q
cd examples/jpeg
%patch -p0
cd ../..

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

for i in `find . -name Makefile` ; do mv $i $i.wrong ; sed -e 's/-O2//g' $i.wrong > $i ; done

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f %{buildroot}/usr/local/lib/liboil-0.3.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files static
%defattr(-,bin,bin)
/usr/local/lib/liboil-0.3.a

%files doc 
%doc  AUTHORS BUG-REPORTING COPYING HACKING NEWS README 
%defattr(-,root,root)
/usr/local/share/gtk-doc/html/liboil/*

%changelog
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.3.15-1
- updated
- added doc and static packages
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.3.8-1
- Initial Rutgers release
