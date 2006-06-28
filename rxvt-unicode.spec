Summary: rxvt-unicode
Name: rxvt-unicode
Version: 7.7
Release: 1
License: GPL
Group: Applications/Terminals
Source: %{name}-%{version}.tar.bz2
Patch: rxvt-unicode.diff
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
BuildRequires: pkgconfig, xft2-devel
Requires: xft2

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt.

Its main features (many of them unique) over rxvt are:
  Stores text in Unicode (either UCS-2 or UCS-4).
  Uses locale-correct input, output and width: as long as your system supports the locale, rxvt-unicode will display correctly.
  Daemon mode: one daemon can open multiple windows on multiple displays, which improves memory usage and startup time considerably.
  Re-wraps long lines instead of splitting or cutting them on resizes.
  Full combining character support (unlike xterm :).
  Multiple fonts supported at the same time: No need to choose between nice japanese and ugly latin, or no japanese and nice latin characters :).
  Supports Xft and core fonts in any combination.
  Locale-independent XIM support.

%prep
%setup -q
%patch -p1

%build
CXX=/opt/SUNWspro/bin/CC
LINKER=/opt/SUNWspro/bin/CC
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CXXFLAGS="-DX11USRLIBDIR=\"/usr/openwin/lib\" -I/usr/openwin/include"
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH
export CXX LINKER LDFLAGS CXXFLAGS PATH

env

./autogen.sh # Run autogen.sh to regenerate the configure script

./configure --enable-everything --enable-combining --enable-font-styles --enable-xpm-background --enable-transparency --enable-tinting --enable-fading --enable-rxvt-scroll --enable-next-scroll --enable-xterm-scroll --enable-plain-scroll --enable-iso14755 --enable-frills --enable-keepscrolling --enable-selectionscrolling --enable-mousewheel --enable-slipwheeling --enable-smart-resize --enable-text-blink --enable-pointer-blank --enable-utmp --enable-wtmp --enable-lastlog --disable-perl --disable-xim

cp config.h config.h.orig
awk '{if ($0 ~ /#define _XOPEN_SOURCE /) {print "#define _XOPEN_SOURCE 500"} else {print}}' < config.h > config.h.ru
cp config.h.ru config.h

#cp src/feature.h src/feature.h.orig
#awk '/#ifdef X11USRLIBDIR/ {print #define X11USRLIBDIR "/usr/openwin/lib"; print}; {print}' < src/feature.h > src/feature.h.ru
#cp src/feature.h.ru src/feature.h

gmake

%install
# Needed to run 'tic' and install the compiled terminfo stuff
mkdir -p %{buildroot}/usr/share/lib/terminfo
TERMINFO=%{buildroot}/usr/share/lib/terminfo gmake install DESTDIR=%{buildroot}

%clean
rm -rf {buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/urxvt
/usr/local/bin/urxvtc
/usr/local/bin/urxvtd
/usr/share/lib/terminfo/r/rxvt-unicode
/usr/local/man/man1/*
/usr/local/man/man7/*
