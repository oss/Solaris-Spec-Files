Summary:	XMMS - Multimedia player for the X Window System.
Name:		xmms
Version:	1.2.10
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Vendor:		XMMS Development Team <bugs@xmms.org>
Url:		http://www.xmms.org/
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	/var/tmp/%{name}-%{version}-root
BuildRequires:	libvorbis gtk2
Requires:	libvorbis gtk2
Provides:	libxmms.so libxmms.so.1

%description
X MultiMedia System is a sound player written from scratch. Since it 
uses the WinAmp GUI, it can use WinAmp skins. It can play mp3s, mods, s3ms,
and other formats. It now has support for input, output, general, and
visualization plugins.

%prep
%setup -q

%build
CC="cc" CXX="CC" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local/ --without-gnome

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/lib/xmms
/usr/local/share/locale/*/LC_MESSAGES/xmms.mo
/usr/local/include/xmms
/usr/local/bin/*
/usr/local/share/xmms/*
/usr/local/share/aclocal/*
/usr/local/man/man1/*

