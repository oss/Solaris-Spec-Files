%define im_ver 5.2.6

Summary: Image manipulation library
Name: ImageMagick
Version: %{im_ver}
Release: 2
Group: Development/Libraries
Copyright: Freely distributable
Source: ImageMagick-%{im_ver}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: gs libpng libjpeg tiff bzip2
BuildRequires: libpng libjpeg tiff gs bzip2 perl

%description
ImageMagick is an image mainpulation library.

%package devel
Summary: ImageMagick header files and static libraries
Group: Development/Libraries
Requires: ImageMagick = %{im_ver}

%description devel
ImageMagick-devel contains the ImageMagick headers and static libraries.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
   LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
   CPP="/usr/local/bin/gcc -E" \
   CPPFLAGS="-I/usr/local/include" ./configure --prefix=/usr/local \
   --enable-static --enable-shared --with-ttf --without-perl
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Copyright.txt
/usr/local/share/ImageMagick
/usr/local/lib/lib*.so*
/usr/local/lib/ImageMagick
/usr/local/bin/*

%files devel
%defattr(-,bin,bin)
/usr/local/lib/*a
/usr/local/include/magick
/usr/local/man/man1/*
/usr/local/man/man4/miff.4
/usr/local/man/man5/quantize.5
