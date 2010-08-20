%define glib2_version 2.22.1
%define major 2.18
%define minor 5

Name:		gtk2
Version:	%{major}.%{minor}
Release:	3
License:	LGPL
Group:		System Environment/Libraries
Source:		ftp://ftp.gtk.org/pub/gtk/%{major}/gtk+-%{version}.tar.gz
URL:		http://www.gtk.org
Summary:	A library for creating GUIs for X
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	atk-devel cairo-devel pango-devel expat-devel 
BuildRequires:	libtiff-devel libjpeg-devel libpng3-devel
BuildRequires:	fontconfig-devel xrender-devel pkgconfig
BuildRequires:	glib2-devel = %{glib2_version}

Requires:	glib2 = %{glib2_version}
Requires:       atk >= 1.26.0
Requires:       xrender >= 0.8.3-7

Conflicts:	librsvg < 2.22.2-2
Conflicts:	gettext-devel

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%package devel
Summary: 	Development tools for GTK+ applications
Group: 		System Environment/Libraries
Requires: 	gtk2 = %{version}-%{release}
Requires:	cairo-devel pango-devel atk-devel
Requires:	glib2-devel = %{glib2_version}

%description devel
This package contains the header files and developer
docs for the GTK2 widget toolkit.

%package doc
Summary:	GTK2 extra documentation
Group:          System Environment/Libraries
Requires: 	gtk2 = %{version}-%{release}

%description doc
This package contains extra documentation for the GTK2 toolkit.

%prep
%setup -q -n gtk+-%{version}
%{__sed} -i '/gtkdoc-rebase/d' docs/reference/*/Makefile.in

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/openwin/include -I/usr/local/include" 
LDFLAGS="-L/usr/openwin/lib -R/usr/openwin/lib -L/usr/local/lib -R/usr/local/lib" 
# I use -DANSICPP here as a hack because Sun's X header file
# (/usr/include/X11/Xlibint.h) has a logical error in it
# A bug report was filed and a patch is, supposedly, on the way (2005.06.24)
#
# -xstrconst is for keeping keyboard label from appearing on all menu
# accelerators
CFLAGS="-DANSICPP -xstrconst"

export PATH CC CXX CPPFLAGS LDFLAGS CFLAGS

./configure \
	--prefix=%{_prefix} 	\
	--disable-rebuilds	\
	--disable-gtk-doc	\
	--without-libjasper

gmake -j3

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/gtk-2.0
touch %{buildroot}%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
touch %{buildroot}%{_sysconfdir}/gtk-2.0/gtk.immodules

gmake install DESTDIR=%{buildroot}

# Remove libtool .la files
find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%post
echo Running gdk-pixbuf-query-loaders...
%{_bindir}/gdk-pixbuf-query-loaders > %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
echo Running gtk-query-immodules-2.0...
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
echo Setting up Default theme symlink...
rm -rf %{_datadir}/themes/Default
ln -sf %{_datadir}/themes/Default-Gtk %{_datadir}/themes/Default
echo ---------------------------------------------------------------
echo NOTE: Make sure to install the latest libjpeg package from OSS!
echo apt-get does not recognize the versioning and will ignore this requirement!
echo ---------------------------------------------------------------

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_sysconfdir}/gtk-2.0/
%{_bindir}/*
%{_libdir}/gtk-2.0/2.*/engines/*.so
%{_libdir}/gtk-2.0/2.*/immodules/im-*.so
%{_libdir}/gtk-2.0/modules/*.so
%{_libdir}/gtk-2.0/2.*/loaders/libpixbufloader-*.so
%{_libdir}/gtk-2.0/2.*/printbackends/*.so
%{_libdir}/lib*.so*
%{_datadir}/themes/*
%{_datadir}/locale/*/LC_MESSAGES/gtk20*.mo

%files devel
%defattr(-, root, root)
%{_libdir}/gtk-2.0/include/gdkconfig.h
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gtk-2.0/*
%{_includedir}/gail-1.0
%{_includedir}/gtk-unix-print-2.0/*
%{_datadir}/aclocal/gtk-2.0.m4

%files doc
%defattr(-, root, root)
%dir %{_datadir}/gtk-2.0/
%docdir %{_datadir}/gtk-2.0/demo/
%docdir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-2.0/demo/
%{_datadir}/gtk-doc/html/*

%changelog
* Thu Aug 19 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.18.5-3
- Add hard dependency on xrender too
* Thu Aug 19 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.18.5-2
- Add hard dependency on atk. Otherwise this tries to link to Solaris'
  libatk.so and busts.
* Mon Jan 11 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 2.18.5-1
- Updated to 2.18.4
* Thu Oct 08 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 2.18.2-1
- Updated to latest version
- requires new glib2
* Wed Jul 15 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.16.4-1
- Updated to version 2.16.4
* Tue May 26 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.16.1-1
- Updated to version 2.16.1
- Cleaned up spec file
* Tue Sep 09 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.14.1-1
- Bumped to version 2.14.1
- Disabled jpeg2000 support with --without-libjasper (new in this version)
- Requires new glib2
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.12.11-3
- added Requires: glib2 = 2.16.5 , gtk2 should require the same version of glib2 it was built against
* Mon Aug 25 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.12.11-2
- added Conflicts: < 2.22.2-2
* Thu Jul 03 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.12.11-1
- bump
* Mon Jun 09 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.12.10-1
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
