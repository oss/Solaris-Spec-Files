Summary: Gtk+ GUI builder
Name: glade
Version: 0.5.9
Release: 2
Group: X11/Libraries
Copyright: LGPL
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Glade is a GUI builder for Gtk.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local
make

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
cd po
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc AUTHORS COPYING ChangeLog NEWS README
/usr/local/lib/locale/*/LC_MESSAGES/*mo
/usr/local/bin/glade
/usr/local/share/pixmaps/*
/usr/local/share/gnome/apps/Development/glade.desktop
/usr/local/share/gnome/help/glade
/usr/local/share/glade
