%define glib2_version 2.20.0

Name:		librsvg
Version:	2.26.0
Release:        1
License:	LGPL
Group:		System Environment/Libraries
Source:		http://ftp.gnome.org/pub/GNOME/sources/librsvg/%{version}/librsvg-%{version}.tar.gz
URL:		http://librsvg.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	libgsf > 1.14.1 
Requires:       glib2 = %{glib2_version}

Obsoletes:	librsvg-static

BuildRequires:	libgsf-devel > 1.14.1 libcroco-devel atk-devel 
BuildRequires:	cairo-devel pixman-devel pango-devel
BuildRequires:  glib2-devel = %{glib2_version}
BuildRequires:  gtk2-devel mozilla-firefox-devel

Summary:        Free, Open Source SVG Rendering Library

%description
In simple terms, librsvg is a component used within software 
applications to enable support for SVG-format scalable graphics. In 
contrast to raster formats, scalable vector graphics provide users and 
artists a way to create, view, and provide imagery that is not limited 
to the pixel or dot density that an output device is capable of.

Many software developers use the librsvg library to render SVG graphics. 
It is lightweight and portable, requiring only libxml and libart at a 
minimum, while providing extra features when used with libcroco, libgsf, 
and mozilla. It is included as part of the GNOME Desktop, and is 
licensed under the LGPL license.

%package devel 
Group:		Applications/Libraries
Requires: 	librsvg = %{version}-%{release}
Summary:	librsvg development files

%description devel
This package contains files needed for building applications that use 
librsvg.

%package doc
Group: 		Applications/Libraries
Requires:	librsvg = %{version}-%{release}
Summary:	Additional librsvg documentation

%description doc
This package contains the GTK docs for librsvg.

%prep
%setup -q

cd tests/pdiff
%{__sed} -i '/typedef/d' pdiff.c perceptualdiff.c
cd ../..

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix} 	\
	--mandir=%{_mandir}	\
	--disable-static	\
	--with-svgz 		\
	--with-croco 		\
	--disable-gtk-doc 	\
	--enable-mozilla-plugin \
	--disable-nls

gmake

%install
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

gmake install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING* AUTHORS MAINTAINERS NEWS ChangeLog
%{_bindir}/*
%{_libdir}/librsvg-2.so.*
%{_libdir}/gtk-2.0/2.10.0/engines/*.so
%{_libdir}/gtk-2.0/2.10.0/loaders/*.so
%{_libdir}/mozilla/plugins/*.so
%{_mandir}/man1/*
%{_datadir}/pixmaps/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/librsvg-2.so
%{_libdir}/pkgconfig/*

%files doc
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/*

%changelog
* Tue May 26 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.26.0-1
- Updated to version 2.26.0
- No longer build static libraries
- Cleaned up spec file
* Tue Sep 09 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.22.2-4
- Respun against new glib2
* Mon Aug 25 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.22.2-2
- Added Requires: libgsf > 1.14.1 to fix libintl.so.3 issues 
* Mon Jul 07 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.22.2-1
- Updated to version 2.22.2
* Sat Nov 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.18.2-1
- Bump to 2.18.2
- Disable NLS
* Thu Nov 8 2007 Naveen Gavini <ngavininbcs.rutgers.edu> - 2.16.1-2
- Fixed defattr
* Thu Jul 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.16.1-1
- Bump to 2.16.1
* Thu May 25 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.14.4-1
- Initial Rutgers release
