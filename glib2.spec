Name: glib2
Version: 2.8.6
Release: 1
Copyright: LGPL
Group: System Environment/Libraries
Source: glib-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Summary: A library of handy utility functions.
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: pkgconfig gettext

%description
GLib is the low-level core library that forms the basis
for projects such as GTK+ and GNOME. It provides data
structure handling for C, portability wrappers, and
interfaces for such runtime functionality as an event loop,
threads, dynamic loading, and an object system.

This package provides version 2 of GLib.

%package devel
Summary: The GIMP ToolKit (GTK+) and GIMP Drawing Kit (GDK) support library
Requires: %{name} %{buildrequires}
Group: Development
%description devel
The glib2-devel package includes the header files for
version 2 of the GLib library.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation


%prep
%setup -q -n glib-%{version}

%build
#CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
#LDFLAGS=" -L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
#LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
#LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
#CC="gcc"
#PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
#export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure --prefix=/usr/local --disable-nls --disable-rebuilds --disable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so*

# Remove static libraries
rm -f $RPM_BUILD_ROOT/usr/local/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so*
/usr/local/lib/charset.alias
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
* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-4
- switched back to gcc because building gtk2 throws -Wl into the ld line
- and Sun's ld doesn't know what to do with it

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-3
- changed gcc to cc

* Tue May 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-2
- Added an unpackaged file to the %files list

* Mon May 23 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-1
- Upgraded to latest release
