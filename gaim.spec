%define name gaim
%define version 2.0.0beta4
%define release 2
%define prefix /usr/local

Summary: 	A Gtk+ based multiprotocol instant messaging client
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Applications/Internet
Source: 	%{name}-%{version}.tar.gz
URL: 		http://gaim.sourceforge.net
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Patch:          gaim-solaris-build-fix.patch
Requires:	nss, gtk2 >= 2.2.2, python >= 2.4, gtkspell >= 2.0.11, startup-notification, python >= 2.4, tcl-tk >= 8.4.13
BuildRequires: 	make, nss-devel, gtk2-devel >= 2.2.2, intltool, cvs, startup-notification, python >= 2.4, tcl-headers >= 8.4.13, tcl-tk >= 8.4.13

%description
Gaim allows you to talk to anyone using a variety of messaging
protocols, including AIM (Oscar and TOC), ICQ, IRC, Yahoo!,
MSN Messenger, Jabber, Gadu-Gadu, Napster, and Zephyr.  These
protocols are implemented using a modular, easy to use design.
To use a protocol, just load the plugin for it.

Gaim supports many common features of other clients, as well as many
unique features, such as perl scripting and C plugins.

Gaim is NOT affiliated with or endorsed by AOL.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I../gtk" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

#mv plugins/Makefile.am plugins/Makefile.am.wrong 
#sed -e 's/ musicmessaging//g' plugins/Makefile.am.wrong > plugins/Makefile.am

#--with-dynamic-prpls=irc,jabber,msn,oscar,yahoo

./configure --prefix=/usr/local  --x-libraries=/usr/include/X11 \
--disable-perl --disable-nas --enable-sm --disable-gevolution \
--enable-startup-notification --disable-nls --disable-gnutls \
--enable-nss --with-nss-includes=/usr/local/include/nss \
--with-nspr-includes=/usr/local/include/nspr \
--with-nss-libs=/usr/local/lib --with-nspr-libs=/usr/local/lib \
--with-python --disable-dbus --with-tclconfig=/usr/local/lib \
--with-tkconfig=/usr/local/lib

gmake

%install
gmake install DESTDIR=%{buildroot}
#rm -rf %{buildroot}/usr/local/include/gaim
#rm -f  %{buildroot}/usr/local/lib/*.la
#rm -f  %{buildroot}/usr/local/lib/gaim/*.la
#rm -f  %{buildroot}/usr/local/lib/pkgconfig/gaim.pc

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
/usr/local/share/locale/*

# uncomment these lines if building with perl
#/usr/local/lib/perl5
#/usr/local/man/man3*/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/gaim.pc

%changelog
* Wed Nov 01 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta4-2
- Bump
* Tue Oct 31 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta4
- Bumped to latest beta release. Fixed a bunch of build bugs.
* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0svn
- Changed to latest svn build
* Thu Apr 06 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0cvs
- Added a devel package, latest cvs build of 2.0
