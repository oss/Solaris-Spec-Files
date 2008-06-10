Name:		gtk2
Version:	2.12.10
Release:	1
License:	LGPL
Group:		System Environment/Libraries
Source:		gtk+-%{version}.tar.gz
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
Summary:	The GIMP ToolKit (GTK+), a library for creating GUIs for X.
BuildRoot:	%{_tmppath}/gtk+-%{version}-root
BuildRequires:	atk-devel >= 1.19.6
BuildRequires:	cairo-devel >= 1.4.10
BuildRequires:	pango-devel >= 1.18.0
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	libtiff-devel >= 3.8.2
BuildRequires:	libjpeg-devel >= 6b-14
BuildRequires:	libpng3-devel >= 1.2.8
BuildRequires:	pkgconfig >= 0.22
BuildRequires:	fontconfig-devel >= 2.4.2
BuildRequires:	xrender-devel
Requires:	atk >= 1.19.6
Requires:	cairo >= 1.4.10
Requires:	pango >= 1.18.0
Requires:	glib2 >= 2.14.0
Requires:	libtiff >= 3.8.2
Requires:	libjpeg = 6b-14
Requires:	libpng3 >= 1.2.8
Requires:	fontconfig >= 2.4.2
Requires:	expat >= 2.0.1

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%package devel
Summary: Development tools for GTK+ applications.
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: pango-devel >= 1.18.0
Requires: atk-devel >= 1.19.6
Requires: glib2-devel >= 2.14.0
# Requires: X devel files
%description devel
The gtk+-devel package contains the header files and developer
docs for the GTK+ widget toolkit.

%package doc
Summary: %{name} extra documentation
Requires: %{name} = %{version}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q -n gtk+-%{version}


%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
#export PATH CC CXX CPPFLAGS LD LDFLAGS

# I use -DANSICPP here as a hack because Sun's X header file
# (/usr/include/X11/Xlibint.h) has a logical error in it
# A bug report was filed and a patch is, supposedly, on the way (2005.06.24)
#
# -xstrconst is for keeping keyboard label from appearing on all menu
# accelerators
CFLAGS="-DANSICPP -xstrconst"

export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure \
	--prefix=/usr/local \
	--disable-nls \
	--disable-rebuilds \
	--disable-gtk-doc
gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/
touch $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
touch $RPM_BUILD_ROOT/usr/local/etc/gtk-2.0/gtk.immodules
gmake install DESTDIR=$RPM_BUILD_ROOT
# cd $RPM_BUILD_ROOT/usr/local/share/themes
# mv Default Default-Gtk

# Remove static libraries
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.*/engines/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.*/loaders/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.*/immodules/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/gtk-2.0/2.*/printbackends/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/*.la

%post
echo Running gdk-pixbuf-query-loaders...
/usr/local/bin/gdk-pixbuf-query-loaders > /usr/local/etc/gtk-2.0/gdk-pixbuf.loaders
echo Running gtk-query-immodules-2.0...
/usr/local/bin/gtk-query-immodules-2.0 > /usr/local/etc/gtk-2.0/gtk.immodules
echo Setting up Default theme symlink...
rm -rf /usr/local/share/themes/Default
ln -sf /usr/local/share/themes/Default-Gtk /usr/local/share/themes/Default
echo ---------------------------------------------------------------
echo NOTE: Make sure to install the latest libjpeg package from OSS!
echo apt-get does not recognize the versioning and will ignore this requirement!
echo ---------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/etc/gtk-2.0/*
/usr/local/bin/*
/usr/local/lib/gtk-2.0/2.*/engines/*.so
/usr/local/lib/gtk-2.0/2.*/immodules/im-*.so
/usr/local/lib/gtk-2.0/2.*/loaders/libpixbufloader-*.so
/usr/local/lib/gtk-2.0/2.*/printbackends/*.so
/usr/local/lib/lib*.so*
/usr/local/share/man/man1/*
/usr/local/share/themes/*
/usr/local/share/locale/*/LC_MESSAGES/gtk20*.mo

%files devel
%defattr(-,root,root)
/usr/local/lib/gtk-2.0/include/gdkconfig.h
/usr/local/lib/pkgconfig/*.pc
/usr/local/include/gtk-2.0/*
/usr/local/include/gtk-unix-print-2.0/*
/usr/local/share/aclocal/gtk-2.0.m4

%files doc
%defattr(-,root,root)
/usr/local/share/gtk-2.0/demo/*
/usr/local/share/gtk-doc/html/gdk-pixbuf/*
/usr/local/share/gtk-doc/html/gdk/*
/usr/local/share/gtk-doc/html/gtk/

%changelog
* Mon Jun 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 2.12.10-1
- bumped to 2.12.10
* Fri Mar 21 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.12.9-1
- Bump to 2.12.9
* Fri Nov 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.12.2-1
- Bump to 2.12.2
* Fri Oct 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.12.1-1
- Bump to 2.12.1
* Thu Sep 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.12.0-3
- Sun gave us the wrong patch, grrr, respinning
* Wed Sep 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.12.0-2
- Respun with official null pointer patch from sun
* Fri Sep 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.12.0-1
- Bump to 2.12.0
* Thu Aug 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.11.6-1
- Bump to 2.11.6
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.11.4-2
- Fixed libtiff requirement
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.11.4
- Version bump to 2.11.4
* Sat May 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.10.12-1
- Bump
* Mon May 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.10.9-3
- Respin against new fontconfig and freetype2
* Mon May 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.10.9-2
- Required specific libjpeg versions so it ignores SUNW
* Wed Feb 14 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.10.9-1
- Bumped to latest version, updated all dependencies to latest versions
* Mon Aug 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.10.1-1
- Updated to new version, updated all dependencies to latest versions
* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.8.16-1
- Updated to new version, added expat as aq dependency
* Tue Feb 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.8.12-2
- Fixed "keyboard label" problem
* Sun Feb 26 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.8.12-1
- Updated to 2.8.12
* Tue Feb 21 2006 Leo Zhadanovksy <leozh@nbcs.rutgers.edu> - 2.6.10-1
- Updated to 2.6.10, along with dependencies
* Fri Jul 29 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-7
- Modified %files section b/c 2 header files were unpackaged
- Made the -doc package depend on %{name}=%{version}
- *** Fixed the Default/Default-Gtk symlink issue
- *** Ghosted some config files
* Thu Jul 28 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-6
- Added some missing requires
- Changed %defattr to the standard (-,root,root)
* Wed Jun 29 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-5
- Changed /usr/local/lib to /usr/local/bin in the PATH
* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-4
- gtk2 throws -Wl as a flag for ld and sun's ld doesn't like it
* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-3
- Changed gcc to cc
* Thu May 26 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 2.6.7-1
- Upgraded to latest release
