%define im_ver 5.5.7_11

Summary: Image manipulation library
Name: ImageMagick
Version: %{im_ver}
Release: 2
Group: Development/Libraries
Copyright: Freely distributable
Source: ImageMagick-%{im_ver}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: gs libpng3 libjpeg62 tiff bzip2
BuildRequires: libpng3-devel libjpeg62-devel tiff gs bzip2 perl 

%description
ImageMagick is an image mainpulation library.

%package devel
Summary: ImageMagick header files and static libraries
Group: Development/Libraries
Requires: ImageMagick = %{im_ver}

%description devel
ImageMagick-devel contains the ImageMagick headers and static libraries.

%prep
%setup -q -n ImageMagick-5.5.7

%build
#LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
#   LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
#   CPP="/usr/local/bin/gcc -E" \
#   CPPFLAGS="-I/usr/local/include" ./configure --prefix=/usr/local \
#   --enable-static --enable-shared --with-ttf --without-perl
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
   LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
   CPP="/usr/local/bin/gcc -E" \
   CPPFLAGS="-I/usr/local/include" ./configure --prefix=/usr/local \
   --enable-static --with-ttf --without-perl
gmake -j7

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
rm %{buildroot}/usr/local/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/share/ImageMagick-5.5.7
/usr/local/lib/ImageMagick*
/usr/local/bin/*
/usr/local/lib/pkgconfig/ImageMagick*
/usr/local/man/man1/*

%files devel
%defattr(-,bin,bin)
/usr/local/lib/*.a
/usr/local/include/magick
/usr/local/include/Magick*
/usr/local/man/man4/*
/usr/local/man/man5/*
