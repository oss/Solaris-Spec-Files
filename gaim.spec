Summary: A Gtk+ based multiprotocol instant messaging client
Name: gaim
Version: 0.72
Release: 1
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: libgnutls >= 0.8.6-2, gtk2 >= 2.2.2-4, gtkspell
BuildRequires: libgnutls >= 0.8.6-2, gtk2-devel >= 2.2.2-4, gtkspell, coreutils, sed

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
# Yay look at the pretty stuff I get to do because automake is dumb
#sed -e 's/^LINK = \(.*\) $(AM_CFLAGS) $(CFLAGS) \(.*\)$/LINK = \1 \2/' src/Makefile.in > src/Makefile.in.ru
#cp src/Makefile.in src/Makefile.in.damn_automake
#mv src/Makefile.in.ru src/Makefile.in

PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
export PATH
#CC="/opt/SUNWspro/bin/cc" LD="/usr/ccs/bin/ld" CFLAGS="-xO3" CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib -R/usr/local/lib"  ./configure --prefix=/usr/local --disable-perl --x-libraries=/usr/include/X11 --enable-gtkspell --disable-audio --disable-tcl --disable-tk --disable-nas --disable-sm --disable-nss --with-dynamic-prpls=gg,irc,jabber,man,oscar,yahoo
CC="/opt/SUNWspro/bin/cc" LD="/usr/ccs/bin/ld" CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib -R/usr/local/lib"  ./configure --prefix=/usr/local --disable-perl --x-libraries=/usr/include/X11 --enable-gtkspell --disable-audio --disable-tcl --disable-tk --disable-nas --disable-sm --disable-nss --with-dynamic-prpls=irc,jabber,msn,oscar,yahoo
gmake

%install
gmake install DESTDIR=%{buildroot}

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
/usr/local/share/applications/*
# I'd really rather not install these, but make install always does and
# if I don't have these lines rpm yells about installed but unpackaged files
/usr/local/share/sounds/*
/usr/local/include/gaim-remote/*.h
/usr/local/lib/libgaim-remote.la

# comment this line if building with nls
/usr/local/share/locale/*/*/*
#/usr/local/lib/charset.alias
#/usr/local/share/locale/locale.alias

# uncomment these lines if building with perl
#/usr/local/lib/perl5
#/usr/local/man/man3*/*
