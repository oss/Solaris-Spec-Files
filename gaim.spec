name: gaim
Version: 0.64
Release: 1
Summary: Multi-Protocol Instant Message client using gtk. Inc. custom Jabber/SSL code.
Source: http://aleron.dl.sourceforge.net/sourceforge/gaim/gaim-%{version}.tar.bz2
Patch: gaim-0.64-tls+ru.patch
Copyright: GPL
Group: Applications/Internet
BuildRoot: /var/tmp/%{name}-root
Requires: libgnutls >= 0.8.6-2 gtk2 >= 2.2.2-4 gtkspell smooth-themes
BuildRequires: libgnutls >= 0.8.6-2 gtk2-devel >= 2.2.2-4 gtkspell

%description
Multi-Protocol Instant Message client using gtk. 
Inc. custom Jabber/SSL code.

%prep
%setup -q

%patch -p1

%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib /usr/local/lib/libstdc++.so.2.10.0"
CFLAGS="-O3 -pipe"
CPPFLAGS="-I/usr/local/include/gnutls"
export LD_LIBRARY_PATH CFLAGS LD_RUN_PATH CPPFLAGS LDFLAGS
./configure --prefix=/usr/local --disable-esd --disable-gnome --disable-artsc --disable-perl --x-libraries=/usr/include/X11 --enable-gtkspell
make LD_RUN_PATH="/usr/local/lib"

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post
%postun

%files
%defattr(-,root,root)
/usr/local/share/pixmaps/gaim.png
/usr/local/share/sounds/gaim/arrive.wav
/usr/local/share/sounds/gaim/leave.wav
/usr/local/share/sounds/gaim/receive.wav
/usr/local/share/sounds/gaim/redalert.wav
/usr/local/share/sounds/gaim/send.wav
/usr/local/share/pixmaps/gaim
/usr/local/share/applications/gaim.desktop
/usr/local/lib/gaim/*.so
/usr/local/man/man1/gaim.1
/usr/local/bin/gaim
/usr/local/bin/gaim-remote
