Name: glib2
Version: 2.6.4
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: glib-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
Summary: A library of handy utility functions.
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: pkgconfig gettext

%description
GLib is the low-level core library that forms the basis for projects such as GTK+ and GNOME. It provides data structure handling for C, portability wrappers, and interfaces for such runtime functionality as an event loop, threads, dynamic loading, and an object system.

This package provides version 2 of GLib.

%package devel
Summary: The GIMP ToolKit (GTK+) and GIMP Drawing Kit (GDK) support library
Requires: %{name} %{buildrequires}
Group: Development
%description devel
The glib2-devel package includes the header files for version 2 of the GLib library.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation


%prep
%setup -q -n glib-%{version}

%build
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib"
CC="gcc"
PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

./configure --prefix=/usr/local --disable-nls --disable-rebuilds

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so*
/usr/local/share/locale/*

%files devel
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/include/glib-2.0/*
/usr/local/lib/glib-2.0/*
/usr/local/lib/pkgconfig/*
/usr/local/share/aclocal/*
/usr/local/share/glib-2.0/*
/usr/local/man/*

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/*

%changelog
* Mon May 23 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-1
- Upgraded to latest release
