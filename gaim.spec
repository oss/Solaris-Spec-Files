Summary: A Gtk+ based multiprotocol instant messaging client
Name: gaim
Version: 0.70
Release: 1
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: libgnutls >= 0.8.6-2 gtk2 >= 2.2.2-4 gtkspell smooth-themes
BuildRequires: libgnutls >= 0.8.6-2 gtk2-devel >= 2.2.2-4 gtkspell

%description
Gaim allows you to talk to anyone using a variety of messaging
protocols, including AIM (Oscar and TOC), ICQ, IRC, Yahoo!,
MSN Messenger, Jabber, Gadu-Gadu, Napster, and Zephyr.  These
protocols are implemented using a modular, easy to use design.
To use a protocol, just load the plugin for it.

Gaim supports many common features of other clients, as well as many
unique features, such as perl scripting and C plugins.

Gaim is NOT affiliated with or endorsed by AOL.

%prep
%setup -q

%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CFLAGS="-O3 -pipe"
export LD_LIBRARY_PATH CFLAGS LD_RUN_PATH
./configure --prefix=/usr/local --disable-perl --x-libraries=/usr/include/X11 --enable-gtkspell --disable-audio --disable-tcl --disable-tk
make LD_RUN_PATH="/usr/local/lib"

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post

%postun

%files
%defattr(-,root,root)

%doc doc/CREDITS doc/FAQ NEWS COPYING AUTHORS
%doc README ChangeLog
/usr/local/bin/*
/usr/local/lib/gaim/*
/usr/local/lib/libgaim-remote.so.*
/usr/local/man/man1/*
/usr/local/share/pixmaps/*
/usr/local/share/locale/*/*/*
/usr/local/share/applications/*
