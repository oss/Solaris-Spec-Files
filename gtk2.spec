Name: gtk2
Version: 2.6.7
Release: 4
Copyright: LGPL
Group: System Environment/Libraries
Source: gtk+-%{version}.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
Summary: The GIMP ToolKit (GTK+), a library for creating GUIs for X.
BuildRoot: %{_tmppath}/gtk+-%{version}-root
BuildRequires: atk-devel >= 1.0.1
BuildRequires: pango-devel >= 1.8.0
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: libtiff-devel >= 3.6.1
BuildRequires: libjpeg62-devel >= 6b
BuildRequires: libpng3-devel >= 1.2.8
BuildRequires: pkgconfig >= 0.15
Requires: glib2 >= 2.6.0
Requires: atk >= 1.0.1
Requires: pango >= 1.8.0

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%package devel
Summary: Development tools for GTK+ applications.
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: pango-devel >= 1.8.0
Requires: atk-devel >= 1.0.1
Requires: glib2-devel >= 2.6.0
# Requires: X devel files
%description devel
The gtk+-devel package contains the header files and developer
docs for the GTK+ widget toolkit.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q -n gtk+-%{version}

%build
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc"

# I use -DANSICPP here as a hack because Sun's X header file
# (/usr/include/X11/Xlibint.h) has a logical error in it
# A bug report was filed and a patch is, supposedly, on the way (2005.06.24)
CFLAGS="-DANSICPP"

PATH="/usr/local/lib:/usr/local/gnu/bin:/usr/sfw/bin:$PATH"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CFLAGS PATH

# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure --prefix=/usr/local --disable-nls --disable-rebuilds --disable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/
touch $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/gtk.immodules
make install DESTDIR=$RPM_BUILD_ROOT
# cd $RPM_BUILD_ROOT/usr/local/share/themes
# mv Default Default-Gtk

/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/*.so* \
$RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.4.*/immodules/im*.so \
$RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.4.*/loaders/libpixbufloader-*.so \
$RPM_BUILD_ROOT/usr/local/bin/*

# Remove static libraries
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.4.0/engines/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.4.0/loaders/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.4.0/immodules/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/*.la

%post
echo Running gdk-pixbuf-query-loaders...
/usr/local/bin/gdk-pixbuf-query-loaders > /usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
echo Running gtk-query-immodules-2.0...
/usr/local/bin/gtk-query-immodules-2.0 > /usr/local/etc/gtk-2.0/gtk.immodules
echo Setting up Default theme symlink...
ln -sf /usr/local/share/themes/Default-Gtk /usr/local/share/themes/Default

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/etc/gtk-2.0/*
/usr/local/bin/*
/usr/local/lib/gtk-2.0/2.4.0/engines/*.so
/usr/local/lib/gtk-2.0/2.4.0/immodules/im-*.so
/usr/local/lib/gtk-2.0/2.4.0/loaders/libpixbufloader-*.so
/usr/local/lib/lib*.so*
/usr/local/man/man1/*
/usr/local/share/themes/*
/usr/local/share/locale/*/LC_MESSAGES/gtk20*.mo

%files devel
%defattr(-,root,other)
/usr/local/lib/gtk-2.0/include/gdkconfig.h
/usr/local/lib/pkgconfig/*.pc
/usr/local/include/gtk-2.0/gdk-pixbuf/*
/usr/local/include/gtk-2.0/gdk/*
/usr/local/include/gtk-2.0/gtk/*
/usr/local/share/aclocal/gtk-2.0.m4

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-2.0/demo/*
/usr/local/share/gtk-doc/html/gdk-pixbuf/*
/usr/local/share/gtk-doc/html/gdk/*
/usr/local/share/gtk-doc/html/gtk/

%changelog
* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-4
- gtk2 throws -Wl as a flag for ld and sun's ld doesn't like it

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-3
- Changed gcc to cc

* Thu May 26 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-1
- Upgraded to latest release
