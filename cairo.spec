Name:		cairo
Version:	1.8.8
Release:	1
Group:		System Environment/Libraries
License:	GPL
URL:		http://cairographics.org
Source:		http://cairographics.org/releases/cairo-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	pkgconfig, xrender-devel, libpng3-devel, libxml2-devel
BuildRequires:	pixman-devel, freetype2-devel, fontconfig-devel

# We don't want a librsvg dependency
BuildConflicts:	librsvg

Summary:        2D Graphics Library

%description
Cairo is a 2D graphics library with support for multiple output devices. 
Currently supported output targets include the X Window System, image 
buffers, PostScript, PDF, and SVG output.

Cairo is designed to produce consistent output on all output media while 
taking advantage of display hardware acceleration when available (e.g. 
through the X Render Extension).

%package devel
Group:		Development/Libraries

Requires:	cairo = %{version}-%{release}
Requires:	xrender-devel, libpng3-devel, pixman-devel
Requires:	freetype2-devel, fontconfig-devel, pkgconfig

Summary:        Cairo development files

%description devel 
This package contains files needed for building applications that use cairo.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:i/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix} 	\
	--disable-static 	\
	--enable-xlib 		\
	--enable-xlib-xrender	\
	--enable-png		\
	--enable-ft 		\
	--enable-ps		\
	--enable-pdf		\
	--enable-svg 		\
	--disable-gtk-doc

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post
cat << EOF

You may wish to install the following for additional functionality:
	
	poppler : provides PDF support

	gs : provides PS support

	librsvg : provides SVG support

EOF

%files
%defattr(-, root, root)
%doc AUTHORS BIBLIOGRAPHY BUGS ChangeLog COPYING NEWS README
%doc COPYING-LGPL-2.1 COPYING-MPL-1.1 PORTING_GUIDE
%{_libdir}/libcairo*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/cairo

%changelog
* Wed Jul 15 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.8-1
- Updated to version 1.8.8

* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.6-2
- Made Requires explicit since RPM 4.1 does not properly pick up library dependencies

* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.8.6-1
- Updated to version 1.8.6
- Modified Requires/BuildRequires
- No longer build static libraries
- Modified configure options

* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.4-1
- Added pixman requirement and pixman-devel build requirement
- Updated to version 1.6.4

* Wed Aug 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10-2
- Removing librsvg dependency and support

* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10-1
- Bump to 1.4.10

* Mon Jan 29 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.6-1
- Updated to latest version and added 8 bit fix

* Tue Aug 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.2-2
- Updated to latest version and enabled poppler support

* Fri Dec 02 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.2-2
- Split into regular and devel packages

* Thu Dec 01 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.2-1
- Initial Rutgers release
