Summary:	FreeType2 library
Name:		freetype2
Version:	2.3.4
Release:	1
Source:		freetype-%{version}.tar.gz
URL:		http://www.freetype.org/
Copyright:	BSD-Like
Group:		X11/Libraries
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	make fileutils
Provides:	freetype
Obsoletes:	freetype

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
%setup -q -n freetype-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
GNUMAKE="gmake"

export PATH CC CXX CPPFLAGS LD LDFLAGS GNUMAKE

./configure 

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
%doc docs/*
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
%doc docs/*
/usr/local/bin/*
/usr/local/lib/lib*a
/usr/local/lib/pkgconfig/*
/usr/local/include/ft2build.h
/usr/local/share/aclocal/freetype2.m4
/usr/local/include/freetype2/*

%changelog
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3.4-1
- Version bump
- Fixed the dreaded "memory font bug"
* Fri Jun 23 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.2.1-1
- Updated to 2.2.1
* Tue Feb 21 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.10-1
- Brought back to 2.1.10 for GTK 2.6.10 package
* Sat Dec 03 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.8-1
- Downgraded to 2.1.8 for compatibility with Mozilla Firefox 1.5
* Wed Nov 23 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.10-1
- Updated to 2.1.10
