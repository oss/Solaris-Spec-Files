Summary: FreeType library
Name: freetype
Version: 2.0.1
Release: 3
Source: freetype-%{version}.tar.gz
URL: http://www.freetype.org/
Copyright: BSD-Like
Group: X11/Libraries
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make fileutils

%description
The FreeType engine is a free and portable TrueType font rendering
engine.  It has been developed to provide TrueType support to a
great variety of platforms and environments.

Note that FreeType is a *library*.  It is not a font server for your
favorite platform, even though it was designed to be used in many of
them.  Note also that it is *not* a complete text-rendering library.
Its purpose is simply to open and manage font files, as well as
load, hint and render individual glyphs efficiently.  You can also
see it as a "TrueType driver" for a higher-level library, though
rendering text with it is extremely easy, as demo-ed by the test
programs.

This package contains the files needed to run programs that use the
FreeType engine.

%package devel
Summary: FreeType development headers and libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The FreeType engine is a free and portable TrueType font rendering
engine.  It has been developed to provide TrueType support to a
great variety of platforms and environments.

Note that FreeType is a *library*.  It is not a font server for your
favorite platform, even though it was designed to be used in many of
them.  Note also that it is *not* a complete text-rendering library.
Its purpose is simply to open and manage font files, as well as
load, hint and render individual glyphs efficiently.  You can also
see it as a "TrueType driver" for a higher-level library, though
rendering text with it is extremely easy, as demo-ed by the test
programs.

This package contains all supplementary files you need to develop
your own programs using the FreeType engine.

%prep
%setup -q

%build
gmake setup \
 LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include"
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/
gmake install prefix=$RPM_BUILD_ROOT/usr/local \
    INSTALL="/usr/local/gnu/bin/install"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc LICENSE.TXT docs/*
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
%doc LICENSE.TXT
/usr/local/bin/*
/usr/local/lib/lib*a
/usr/local/include/freetype2/*
