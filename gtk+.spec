Name: gtk+
Version: 1.2.10
Copyright: LGPL
Group: X11/Libraries
Summary: The Gimp Toolkit
Release: 2
Source: gtk+-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: glib >= %{version}
BuildRequires: glib >= %{version}
Conflicts: vpkg-SFWgtk

%description
The X libraries originally written for the Gimp, which are now used by
several other programs as well.

%package devel
Summary: GIMP Toolkit and GIMP Drawing Kit
Group: X11/Libraries
Requires: gtk+

%description devel
Static libraries and header files for the GIMP's X libraries, which are
available as public libraries.  GLIB includes generally useful data
structures, GDK is a drawing toolkit which provides a thin layer over
Xlib to help automate things like dealing with different color depths,
and GTK is a widget set for creating user interfaces.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/gdk.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/gtk.info
fi

%preun devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gdk.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gtk.info
fi

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
/usr/local/lib/locale/*/LC_MESSAGES/gtk+.mo
/usr/local/lib/lib*.so*
/usr/local/share/themes/Default/gtk/gtkrc
/usr/local/lib/pkgconfig

%files devel
%defattr(-, root, root)
/usr/local/lib/lib*a
/usr/local/bin/gtk-config
/usr/local/include/gtk-1.2
/usr/local/etc/gtk
/usr/local/share/aclocal/gtk.m4
/usr/local/info/*info*
/usr/local/man/man1/gtk-config.1
