Summary: gd library
Name: gd
Version: 1.8.4
Release: 7
Source: gd-%{version}.tar.gz
URL: http://www.boutell.com/gd/
Copyright: Other public
Group: Graphics/Libraries
BuildRoot: /var/tmp/%{name}-root
Requires: freetype2 libpng3 xpm zlib libjpeg
BuildRequires: libpng3-devel xpm zlib-devel freetype2-devel

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
Summary: gd development headers and libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel

This package contains all supplementary files (headers, etc.) you need to
develop your own programs using the gd library.

%prep
%setup -q

%build
make CFLAGS='-O -DHAVE_LIBPNG -DHAVE_LIBJPEG -DHAVE_LIBXPM \
-DHAVE_LIBFREETYPE' LIBS='-lgd -lpng -lz -ljpeg -lfreetype \
-lm -R/usr/local/lib' INCLUDEDIRS='-I. -I/usr/local/include/freetype2 \
-I/usr/include/X11 -I/usr/X11R6/include/X11 -I/usr/local/include'

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
make install INSTALL_LIB=$RPM_BUILD_ROOT/usr/local/lib \
INSTALL_INCLUDE=$RPM_BUILD_ROOT/usr/local/include \
INSTALL_BIN=$RPM_BUILD_ROOT/usr/local/bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*

%files devel
%defattr(-,bin,bin)
/usr/local/lib/*
/usr/local/include/*
