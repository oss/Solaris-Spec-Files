Summary: Gtk theme engines
Name: gtk-engines
Version: 0.10
Release: 2
Group: User Interface/X
Copyright: GPL
Source: gtk-engines-0.10.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: imlib >= 1.9.8, gtk+ >= 1.2.8
BuildRequires: imlib-devel
BuildRequires: gtk+-devel

%description
This package provides themes for gtk.  It is used by gnome.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
    ./configure --enable-static --enable-shared --enable-static \
     --with-imlib-prefix=/usr/local

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING README
/usr/local/share/themes/Pixmap
/usr/local/share/themes/Redmond95
/usr/local/share/themes/Notif
/usr/local/share/themes/Metal
/usr/local/lib/gtk/themes/engines/libpixmap.*
/usr/local/lib/gtk/themes/engines/libredmond95.*
/usr/local/lib/gtk/themes/engines/libnotif.*
/usr/local/lib/gtk/themes/engines/libmetal.*
