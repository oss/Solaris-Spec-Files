%include gnome-header.spec

%define realver 1.0.9
Summary: The Ice Window Manager
Name: icewm
Version: 1.0.9
Release: 1
Group: User Interface/X
Copyright: LGPL
Source: icewm-%{realver}-1.tar.bz2
Patch: icewm.patch
#Requires: %{imlib_pkg} 
Requires: libjpeg libpng tiff
BuildRoot: /var/tmp/%{name}-root
#BuildRequires: %{imlib_dev}
BuildRequires: libjpeg libpng tiff

%description
IceWM is a window manager for the X Window System. It is designed to
be small, fast, lightweight, and to emulate the look and feel of
Motif, OS/2 and Windows.

While it is very configurable, it is not pathologically so (a la
Enlightenment or FVWM). In short, IceWM provides a customizable look
with a relatively consistant feel.

%prep
%setup -q -n icewm-1.0.9
%patch -p1
cp install-sh po/install-sh

%build
CC="gcc %{gnome_ldflags} -L/usr/local/lib -R/usr/local/lib" \
  CXX="g++ %{gnome_ldflags} -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="%{gnome_ldflags} -L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" \
 ./configure --with-imlib=%{imlib_prefix}/bin --enable-i18n --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/*
/usr/local/bin/icewm
/usr/local/bin/icewmhint
/usr/local/bin/icewmbg
/usr/local/lib/X11/icewm
/usr/local/etc/X11/icewm
/usr/local/share/locale/*/LC_MESSAGES/*
