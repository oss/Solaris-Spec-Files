	%define im_ver 6.3.4_10

Summary: Image manipulation library
Name: ImageMagick
Version: %{im_ver}
Release: 2
Group: Development/Libraries
Copyright: Freely distributable
Source: ImageMagick-%{im_ver}.tar.bz2
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Kevin Mulvey <kmulvey@nbcs.rutgers.edu>
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
%setup -q -n ImageMagick-6.3.4

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
   --mandir=/usr/local/man --enable-static --with-ttf --without-perl
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
/usr/local/share/ImageMagick-6.3.4
/usr/local/lib/ImageMagick*
/usr/local/lib/*
/usr/local/bin/*
/usr/local/lib/pkgconfig/ImageMagick*
/usr/local/man/*
/usr/local/share/doc/*

%files devel
%defattr(-,bin,bin)
/usr/local/include/magick
/usr/local/include/Magick++/*
/usr/local/include/Magick++.h
/usr/local/man/*
/usr/local/include/wand/*

%changelog
* Wed Jun 20 2007 Kevin Mulvey <kmulvey@nbcs.rutgers.edu> - 6.3.4-10
- Updated to 6.3.4
