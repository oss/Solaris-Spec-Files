Summary:	library for high-performance 2D graphics
Name:		libart_lgpl
Version:	2.3.17
Release:        1
Copyright:	LGPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Libart is a 2D drawing library: its goal is to be a high-quality 
vector-based 2D library with antialiasing and alpha composition.

Libart is a high-performance rendering library that provides a rich 
imaging model. Libart's imaging model is a superset of PostScript, and 
it adds support for antialiasing and alpha compositing (transparency).

Libart is used as the core rendering engine for both the GNOME canvas 
and the GNOME printing system. It uses sophisticated techniques such as 
microtile arrays and sorted vector paths to maximize performance.

Libart provides a wealth of vector path-manipulation operations, affine 
transformations, antialiased and alpha-composited vector path 
rendering, and functions for manipulating Bézier paths.

Applications for Libart are numerous and cross many disciplines. A 
brief sampling follows:

    * Interactive graphics applications, using libart's sorted vector 
paths and microtiles to optimize incremental redisplay.
    * Dynamic generation of web graphics, for example charts or 
personalized buttons.
    * Rendering maps and other GIS (Geographic Information Systems) 
data, both for Web delivery and personal computer applications.
    * Presentation of biomedical and industrial data on embedded 
displays.
    * SVG viewers and editors for desktop and web graphics. 

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*so*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Wed May 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.3.17-1
- Initial Rutgers release
