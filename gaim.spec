Summary: A Gtk+ based multiprotocol instant messaging client
Name: gaim
Version: 0.77
Release: 1
License: GPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: nss, gtk2 >= 2.2.2
BuildRequires: make, nss-devel, gtk2-devel >= 2.2.2
#check whether providing this is right for us
Provides: libgaim-remote0

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
#PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
#export PATH
# can't use sun cc since glib was built with gcc and glib therefore expects G_VA_COPY to be __va_copy which sun cc doesn't have (signals.c uses it)
#CC="/opt/SUNWspro/bin/cc" LD="/usr/ccs/bin/ld" CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib -R/usr/local/lib"  ./configure --prefix=/usr/local --disable-perl --x-libraries=/usr/include/X11 --enable-gtkspell --disable-audio --disable-tcl --disable-tk --disable-nas --disable-sm --disable-nss --with-dynamic-prpls=irc,jabber,msn,oscar,yahoo
CC="gcc" CPPFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib -R/usr/local/lib"  ./configure --prefix=/usr/local --disable-perl --x-libraries=/usr/include/X11 --disable-gtkspell --disable-audio --disable-tcl --disable-tk --disable-nas --disable-sm --disable-gevolution --disable-startup-notification --disable-nls --disable-gnutls --enable-nss --with-dynamic-prpls=irc,jabber,msn,oscar,yahoo --with-nss-includes=/usr/local/include/nss --with-nspr-includes=/usr/local/include/nspr --with-nss-libs=/usr/local/lib --with-nspr-libs=/usr/local/lib
gmake

%install
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%doc doc/CREDITS NEWS COPYING AUTHORS COPYRIGHT
%doc README ChangeLog
/usr/local/bin/*
/usr/local/lib/gaim/*.so
/usr/local/lib/libgaim-remote.so.*
/usr/local/man/man1/*
/usr/local/share/pixmaps/*
/usr/local/share/applications/*
# I'd really rather not install these, but make install always does and
# if I don't have these lines rpm yells about installed but unpackaged files
/usr/local/share/sounds/*
/usr/local/include/gaim-remote/*.h

# comment these lines if not building with nls
#/usr/local/share/locale/*/*/*
#/usr/local/lib/charset.alias
#/usr/local/share/locale/locale.alias

# uncomment these lines if building with perl
#/usr/local/lib/perl5
#/usr/local/man/man3*/*
