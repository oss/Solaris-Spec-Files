Summary:	a library of simple functions that are optimized for various CPUs
Name:		liboil
Version:	cvs04052006
Release:        1
Copyright:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
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

%prep
%setup -q

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

%changelog
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.3.8-1
- Initial Rutgers release
