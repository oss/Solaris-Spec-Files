Summary: libglade library
Name: libglade
Version: 0.15
Release: 2
Group: X11/Libraries
Copyright: LGPL
Source: libglade-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: libxml >= 1.8.10
Requires: gtk+ >= 1.2.8
Requires: gnome-libs >= 1.2.8
BuildRequires: libxml-devel >= 1.8.10
BuildRequires: gtk+-devel >= 1.2.8
BuildRequires: gnome-libs-devel >= 1.2.8

%description
This library allows you to load user interfaces in your program, which are
stored externally.  This allows alteration of the interface without
recompilation of the program.

The interfaces can also be edited with GLADE.

%package devel
Summary: Libraries, includes, etc to develop libglade applications
Group: X11/libraries
Requires: libglade gtk+-devel libxml-devel

%description devel
Libraries, include files, etc you can use to develop libglade applications.


%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
    LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure \
    --with-gtk-prefix=/usr/local --with-gnome=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc AUTHORS ChangeLog NEWS README COPYING
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
%doc test-libglade.c
%doc *.glade
%doc /usr/local/share/gnome/html/libglade/*
/usr/local/lib/lib*a
/usr/local/lib/libgladeConf.sh
/usr/local/include/glade
/usr/local/share/aclocal/libglade.m4
/usr/local/bin/*
