Name:		glib2
Version:	2.22.1
Release:	1
License:	LGPL
Group:		System Environment/Libraries
Source:		http://ftp.gnome.org/pub/gnome/sources/glib/%{version}/glib-%{version}.tar.gz
Patch0:		glib2-2.22.1-macros.patch
URL:		http://www.gtk.org		
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	pkgconfig libiconv-devel

BuildConflicts:	gettext

Summary:        Library of handy utility functions

%description
GLib is the low-level core library that forms the basis
for projects such as GTK+ and GNOME. It provides data
structure handling for C, portability wrappers, and
interfaces for such runtime functionality as an event loop,
threads, dynamic loading, and an object system.

This package provides version 2 of GLib.

%package devel
Group:		System Environment/Libraries
Requires:       glib2 = %{version}-%{release}

Summary:        Headers for development with glib2

%description devel
This package includes the header files for glib2.

%package	doc
Group:		System Environment/Libraries
Requires:	glib2 = %{version}-%{release}

Summary:	Extra documentation for glib2

%description doc
This package contians extra documentation for the glib2 library.

%prep
%setup -q -n glib-%{version}
%{__sed} -i "/gtkdoc-rebase/d"			\
	docs/reference/glib/Makefile.in		\
	docs/reference/gobject/Makefile.in	\
	docs/reference/gio/Makefile.in

%patch0

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin/:${PATH}" 
CC="cc" CXX="CC" CFLAGS="-g -xs" 
CPPFLAGS="-I/usr/local/include" 
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CFLAGS CPPFLAGS LDFLAGS LD

# --disable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure \
	--prefix=%{_prefix}	\
	--mandir=%{_mandir}	\
	--disable-gtk-doc	\
	--with-libiconv=gnu	\
	--disable-nls

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

# Remove unwanted files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/charset.alias

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so*
%{_datadir}/locale/*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/glib-2.0/
%{_includedir}/gio-unix-2.0/
%{_libdir}/glib-2.0/
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%{_datadir}/glib-2.0/

%files doc
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/*

%changelog
* Tue Oct 06 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 2.22.1-1
- updated to  version 2.22.1
- Added patch to define CMSG_* macros (linux macros that aren't refined in solaris 9)

* Wed Jul 15 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.20.4-1
- Updated to version 2.20.4

* Fri May 22 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.20.0-1
- Updated to version 2.20.0

* Mon Sep 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.18.0-1
- Bumped to version 2.18.0

* Mon Jul 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.16.5-1
- bump, added %doc

* Fri Mar 21 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.16.1-1
- Updated to the latest version.

* Mon Nov 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.14.4-2
- Got rid of gettext

* Mon Nov 26 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.14.4-1
- Bump to 2.14.4

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
