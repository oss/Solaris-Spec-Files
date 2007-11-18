Name:		glib2
Version:	2.14.3
Release:	2
License:	LGPL
Group:		System Environment/Libraries
Source:		glib-%{version}.tar.bz2
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
Summary:	A library of handy utility functions.
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	pkgconfig libiconv-devel
Requires:	expat

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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure \
	--prefix=/usr/local \
	--disable-gtk-doc \
	--with-libiconv=gnu \
	--disable-nls
gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

# Remove static libraries
rm -f $RPM_BUILD_ROOT/usr/local/lib/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so*
/usr/local/lib/charset.alias
/usr/local/share/locale/*
/usr/local/share/man/man1/*

%files devel
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/include/glib-2.0/*
/usr/local/lib/glib-2.0/*
/usr/local/lib/pkgconfig/*
/usr/local/share/aclocal/*
/usr/local/share/glib-2.0/*

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/*

%changelog
* Fri Oct 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.14.2-1
- Bump to 2.14.2
* Fri Sep 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.14.1-1
- Bump to 2.14.1
* Thu Aug 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.14.0-1
- Bumped to 2.14.0
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.13.6
- Bumped to 2.13.6
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.12.12
- Bumped to 2.12.12
* Wed Feb 14 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.12.9
- Bumped to 2.12.9

* Mon Aug 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.12.1
- Updated to 2.12.1

* Tue May 02 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.10.2-1
- Updated to 2.10.2

* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-4
- switched back to gcc because building gtk2 throws -Wl into the ld line
- and Sun's ld doesn't know what to do with it

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-3
- changed gcc to cc

* Tue May 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-2
- Added an unpackaged file to the %files list

* Mon May 23 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.4-1
- Upgraded to latest release
