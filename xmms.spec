Summary:	XMMS - Multimedia player for the X Window System.
Name:		xmms
Version:	1.2.2
Release: 3
Copyright:	GPL
Group:		Applications/Multimedia
Vendor:		XMMS Development Team <bugs@xmms.org>
Url:		http://www.xmms.org/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.2
Provides:	libxmms.so libxmms.so.1

%description
X MultiMedia System is a sound player written from scratch. Since it 
uses the WinAmp GUI, it can use WinAmp skins. It can play mp3s, mods, s3ms,
and other formats. It now has support for input, output, general, and
visualization plugins.

%prep
%setup -q

%build
CFLAGS="-O2"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib"
export CFLAGS CPPFLAGS CXXFLAGS LDFLAGS LD

# We're building without gnome because the subdirectory building is
# broken (you can't make after running ../configure ...
./configure --prefix=/usr/local/ --without-gnome

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/lib/xmms
/usr/local/lib/locale/*/LC_MESSAGES/xmms.mo
/usr/local/include/xmms
/usr/local/bin/*
/usr/local/share/xmms/*
/usr/local/share/aclocal/*
