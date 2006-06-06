Summary:	XMMS - Multimedia player for the X Window System.
Name:		xmms
Version:	1.2.10
Release:        3
Copyright:	GPL
Group:		Applications/Multimedia
Vendor:		XMMS Development Team <bugs@xmms.org>
Url:		http://www.xmms.org/
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	/var/tmp/%{name}-%{version}-root
BuildRequires:	libvorbis gtk2, libmikmod
Requires:	libvorbis gtk2, libmikmod
Provides:	libxmms.so libxmms.so.1

%description
X MultiMedia System is a sound player written from scratch. Since it 
uses the WinAmp GUI, it can use WinAmp skins. It can play mp3s, mods, s3ms,
and other formats. It now has support for input, output, general, and
visualization plugins.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lintl" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --without-gnome

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
for i in `find . -name '*.a'`; do rm $i; done
for i in `find . -name '*.la'`; do rm $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/lib/xmms
/usr/local/share/locale/*/LC_MESSAGES/xmms.mo
/usr/local/include/xmms
/usr/local/bin/*
/usr/local/share/xmms/*
/usr/local/share/aclocal/*
/usr/local/man/man1/*

