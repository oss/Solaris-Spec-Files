%define cvsdate %(date +%d%m%Y)

Summary: A Gtk+ based multiprotocol instant messaging client
Name: gaim
Version: 2.0.0cvs%{cvsdate}
Release: 1
License: GPL
Group: Applications/Internet
#Source: %{name}-%{version}.tar.bz2
URL: http://gaim.sourceforge.net
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Etan Reisner <deryni@jla.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: nss, gtk2 >= 2.2.2
BuildRequires: make, nss-devel, gtk2-devel >= 2.2.2, intltool, cvs
#check whether providing this is right for us
#Provides: libgaim-remote0

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
#%setup -q -n gaim

%build
rm -rf gaim

cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/gaim login
cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/gaim co -P gaim

cd gaim

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

sh autogen.sh

./configure --prefix=/usr/local --disable-perl --x-libraries=/usr/include/X11 --disable-gtkspell --disable-audio --disable-tcl --disable-tk --disable-nas --disable-sm --disable-gevolution --disable-startup-notification --disable-nls --disable-gnutls --enable-nss --with-dynamic-prpls=irc,jabber,msn,oscar,yahoo --with-nss-includes=/usr/local/include/nss --with-nspr-includes=/usr/local/include/nspr --with-nss-libs=/usr/local/lib --with-nspr-libs=/usr/local/lib
gmake

%install
cd gaim
gmake install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/local/include/gaim
rm -f  %{buildroot}/usr/local/lib/*.la
rm -f  %{buildroot}/usr/local/lib/gaim/*.la
rm -f  %{buildroot}/usr/local/lib/pkgconfig/gaim.pc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%doc doc/CREDITS
%doc NEWS
%doc COPYING
%doc AUTHORS
%doc COPYRIGHT
%doc README
%doc ChangeLog
/usr/local/bin/*
/usr/local/lib/gaim/*.so
/usr/local/man/man1/*
/usr/local/share/pixmaps/*
/usr/local/share/applications/*
/usr/local/share/sounds/*
/usr/local/share/aclocal/*

# uncomment these lines if building with nls
#/usr/local/share/locale/*/*/*
#/usr/local/lib/charset.alias
#/usr/local/share/locale/locale.alias

# uncomment these lines if building with perl
#/usr/local/lib/perl5
#/usr/local/man/man3*/*
