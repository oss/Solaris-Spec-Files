Summary:	gd library
Name:		gd
Version:	2.0.34
Release:	1
Source:		gd-%{version}.tar.bz2
URL:		http://www.libgd.org
Copyright:	BSD-style
Group:		Graphics/Libraries
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Patch0:		gd-2.0.33-freetype.patch
Patch3:		gd-2.0.34-multilib.patch
Patch4:		gd-loop.patch
Patch5:		gd-2.0.34-sparc64.patch
Patch6:		gd-2.0.33-overflow.patch
Patch7:		gd-2.0.33-AALineThick.patch
Patch8:		gd-2.0.33-BoxBound.patch
Requires:	freetype2 libpng3 xpm zlib libjpeg
BuildRequires:	pkgconfig libjpeg-devel libpng3-devel xpm zlib-devel
BuildRequires:	fontconfig-devel freetype2-devel 

%description

gd is a graphics library. It allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from other
images, and flood fills, and write out the result as a PNG or JPEG file.
This is particularly useful in World Wide Web applications, where PNG and
JPEG are two of the formats accepted for inline images by most browsers.

The gd package contains binaries for manipulating "gd" files and examples
of libgd programs. It is probably of little use without "gd-devel", which
will allow you to develop your own programs that utilize the library.

%package devel
Summary:	gd development headers and libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel

This package contains all supplementary files (headers, etc.) you need to
develop your own programs using the gd library.

%prep
%setup -q
%patch0 -p1 -b .freetype
%patch3 -p1 -b .mlib
%patch4 -p1 -b .loop
%patch6 -p1 -b .overflow
%patch5 -p1 -b .sparc64 
%patch7 -p1 -b .AALineThick
%patch8 -p1 -b .bb

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

#make CFLAGS='-O -DHAVE_LIBPNG -DHAVE_LIBJPEG -DHAVE_LIBXPM \
#-DHAVE_LIBFREETYPE' LIBS='-lgd -lpng -lz -ljpeg -lfreetype \
#-lm -R/usr/local/lib' INCLUDEDIRS='-I. -I/usr/local/include/freetype2 \
#-I/usr/include/X11 -I/usr/X11R6/include/X11 -I/usr/local/include'

./configure --prefix="/usr/local"

make

%install
rm -rf %{buildroot}
#mkdir -p $RPM_BUILD_ROOT/usr/local/lib
#mkdir -p $RPM_BUILD_ROOT/usr/local/include
#mkdir -p $RPM_BUILD_ROOT/usr/local/bin
#make install INSTALL_LIB=$RPM_BUILD_ROOT/usr/local/lib \
#INSTALL_INCLUDE=$RPM_BUILD_ROOT/usr/local/include \
#INSTALL_BIN=$RPM_BUILD_ROOT/usr/local/bin

make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/libgd.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README-JPEG.TXT index.html entities.html
%{_libdir}/*.so.*
%{_bindir}/*
%exclude %{_bindir}/gdlib-config

%files devel
%defattr(-,root,root,-)
%doc index.html
%{_bindir}/gdlib-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/gdlib.pc

%changelog
* Thu Aug 23 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.34-1
- Bump to 2.0.34
