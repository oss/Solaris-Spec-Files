Summary:	Free, Open Source SVG Rendering Library
Name:		librsvg
Version:	2.18.2
Release:        2
License:	LGPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	libgsf, libcroco
BuildRequires:	libgsf-devel, libcroco-devel, mozilla-firefox-devel

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
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%package doc
Summary: GTK docs for %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description doc
The %{name}-doc package contains all the GTK specs and docs for %{name}

%package static
Summary: Static libraries for %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description static
The %{name}-static package contains all the static libraries for %{name}

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--with-svgz \
	--with-croco \
	--disable-gtk-doc \
	--enable-mozilla-plugin \
	--disable-nls

cd tests/pdiff
sed -e 's/stdint.h/inttypes.h/g' pdiff.c > pdiff.c.wrong
mv pdiff.c.wrong pdiff.c
sed -e 's/stdint.h/inttypes.h/g' perceptualdiff.c > perceptualdiff.c.wrong
mv perceptualdiff.c.wrong perceptualdiff.c
cd ../..

gmake

%install
rm -rf $RPM_BUID_ROOT

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/lib/gtk-2.0/2.10.0/engines/*.so
/usr/local/lib/gtk-2.0/2.10.0/loaders/*.so
/usr/local/lib/mozilla/plugins/*.so
/usr/local/share/man/man1/*
/usr/local/share/pixmaps/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files doc
%defattr(-,bin,bin)
/usr/local/share/gtk-doc/*

%files static
%defattr(-,bin,bin)
/usr/local/lib/gtk-2.0/2.10.0/engines/libsvg.a
/usr/local/lib/gtk-2.0/2.10.0/engines/libsvg.la
/usr/local/lib/gtk-2.0/2.10.0/loaders/svg_loader.a
/usr/local/lib/gtk-2.0/2.10.0/loaders/svg_loader.la
/usr/local/lib/librsvg-2.a
/usr/local/lib/librsvg-2.la
/usr/local/lib/mozilla/plugins/libmozsvgdec.a
/usr/local/lib/mozilla/plugins/libmozsvgdec.la

%changelog
* Sat Nov 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.18.2-1
- Bump to 2.18.2
- Disable NLS
* Thu Nov 8 2007 Naveen Gavini <ngavininbcs.rutgers.edu> - 2.16.1-2
- Fixed defattr
* Thu Jul 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.16.1-1
- Bump to 2.16.1
* Thu May 25 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.14.4-1
- Initial Rutgers release
