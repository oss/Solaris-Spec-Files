Summary:	Beep Media Player 
Name:		bmpx
Version:	0.14.4
Release:        8
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.bz2
Patch:		bmpx.solaris.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk2, taglib, glib2 >= 2.10, libglade, cairo, neon, gamin, startup-notification, libmusicbrainz, gstreamer, libxml2, gst-plugins-ugly
BuildRequires:	gtk2-devel >= 2.8, glib2-devel >= 2.10, libglade-devel, cairo-devel, neon-devel, gamin-devel, startup-notification-devel, taglib-devel, libmusicbrainz-devel, gstreamer-devel, libxml2-devel

%description
BMPx is a media player that features support for specifications like XDS 
DnD, XSPF and DBus. BMPx is highly interoperable and integrates well 
with other applications and a variety of desktop environments.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q
%patch -p1

%build
CPPFLAGS="-I/usr/local/include"
CFLAGS="-I/usr/local/include -D_XPG4_2=1 -ggdb" 
#CFLAGS="-I/usr/local/include -D_XPG4_2=1"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lintl"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CC="gcc"
export CPPFLAGS CFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

#PATH="/opt/SUNWspro/bin:${PATH}" \
#CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
#LD="/usr/ccs/bin/ld" \
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
#export PATH CC CXX CPPFLAGS LD LDFLAGS

sh autogen.sh

./configure --prefix=/usr/local --enable-amazon --disable-dbus

mv xcs/xcs.c xcs/xcs.c.wrong
mv src/signals.c src/signals.c.wrong

sed -e 's/#include <getopt.h>//' xcs/xcs.c.wrong > xcs/xcs.c
sed -e 's/#include <signal.h>/#include <sys\/signal.h>/' src/signals.c.wrong > src/signals.c

rm xcs/xcs.c.wrong
rm src/signals.c.wrong

for i in `find . -name Makefile` ; do mv $i $i.wrong ; sed -e 's/-mt //g' $i.wrong > $i ; done

for i in `find . -type f|grep "\.c"` ; do mv $i $i.wrong ; sed -e 's/#include <stdint.h>//g' $i.wrong > $i ; rm $i.wrong ; done

for i in `find . -type f|grep "\.h"` ; do mv $i $i.wrong ; sed -e 's/#include <stdint.h>//g' $i.wrong > $i ; rm $i.wrong ; done

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

#rm $RPM_BUILD_ROOT/usr/local/share/locale/locale.alias

chmod -R 755 $RPM_BUILD_ROOT/usr/local/lib/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/libexec/beep-media-player-2-bin
/usr/local/lib/*.so
/usr/local/lib/*so*
/usr/local/lib/bmp-2.0/plugins/container/*.so
/usr/local/lib/bmp-2.0/plugins/container/*so*
/usr/local/lib/bmp-2.0/plugins/flow/*.so
/usr/local/lib/bmp-2.0/plugins/flow/*so*
/usr/local/lib/bmp-2.0/plugins/transport/*.so
/usr/local/lib/bmp-2.0/plugins/transport/*so*
/usr/local/share/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Thu May 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.14.4
- Initial Rutgers release
