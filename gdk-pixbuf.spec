Summary: The GdkPixBuf image handling library
Name: gdk-pixbuf
Version: 0.8.0
Release: 3
Group: LGPL
Copyright: System Environment/Libraries
Source: gdk-pixbuf-0.8.0.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: gtk+ >= 1.2.8
Requires: glib >= 1.2.8
Requires: libjpeg
Requires: libpng
Requires: tiff
Requires: libglade
Requires: gnome-libs
BuildRequires: gtk+-devel >= 1.2.8
BuildRequires: libjpeg
BuildRequires: libpng
BuildRequires: tiff
BuildRequires: libglade-devel
BuildRequires: gnome-libs-devel

%description
The GdkPixBuf library provides a number of features, including :

- GdkPixbuf structure for representing images.
- Image loading facilities.
- Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.
- Fast scaling and compositing of pixbufs.
- Simple animation loading (ie. animated gifs)

In addition, this module also provides a little libgnomecanvaspixbuf
library, which contains a GNOME Canvas item to display pixbufs with
full affine transformations.

%package devel
Summary: Libraries and include files for developing GdkPixBuf applications.
Group: Development/Libraries
Requires: gdk-pixbuf = 0.8.0

%description devel
Libraries and include files for developing GdkPixBuf applications.


%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include" \
    LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
    --enable-shared --enable-static --with-glib-prefix=/usr/local \
    --with-gtk-prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING COPYING.LIB ChangeLog NEWS README TODO doc/*.txt
/usr/local/lib/lib*.so*
/usr/local/lib/gdk-pixbuf/loaders/lib*.so*

%files devel
%defattr(-,bin,bin)
%doc $RPM_BUILD_ROOT/usr/local/share/gnome/html/*
/usr/local/lib/*a
/usr/local/lib/*.sh
/usr/local/lib/gdk-pixbuf/loaders/lib*a
/usr/local/include/gdk-pixbuf
/usr/local/share/aclocal/gdk-pixbuf.m4
/usr/local/bin/*
