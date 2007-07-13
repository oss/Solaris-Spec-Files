Summary:	Free, Open Source SVG Rendering Library
Name:		librsvg
Version:	2.16.1
Release:        1
License:	LGPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
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

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --with-svgz --with-croco --disable-gtk-doc --enable-mozilla-plugin

#mv rsvg-private.h rsvg-private.h.wrong
#sed -e 's/__PRETTY_FUNCTION__/__func__/g' rsvg-private.h.wrong > rsvg-private.h

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/lib/gtk-2.0/2.10.0/engines/*.so
/usr/local/lib/gtk-2.0/2.10.0/loaders/*.so
/usr/local/lib/mozilla/plugins/*.so
/usr/local/man/man1/*
/usr/local/share/pixmaps/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files doc
/usr/local/share/gtk-doc/*

%changelog
* Thu Jul 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.16.1-1
- Bump to 2.16.1
* Thu May 25 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.14.4-1
- Initial Rutgers release
