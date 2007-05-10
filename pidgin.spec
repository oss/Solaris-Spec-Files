
%define name pidgin
%define version 2.0.0
%define release 4
%define prefix /usr/local 

Summary: 	A Gtk+ based multiprotocol instant messaging client
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Applications/Internet
Source: 	%{name}-%{version}.tar.gz
URL: 		http://www.pidgin.im
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Patch0:		finch_curses_bug2.patch
Patch1:		nat_pmp_bug.patch
Requires:	nss, gtk2 >= 2.2.2, python >= 2.4, gtkspell >= 2.0.11
Requires:	startup-notification, python >= 2.4, tcl-tk >= 8.4.13
Requires:	libxml2 >= 2.6.28, aspell
BuildRequires: 	make, nss-devel, gtk2-devel >= 2.2.2, intltool, fontconfig-devel, aspell
BuildRequires:	startup-notification, python >= 2.4, tcl-headers >= 8.4.13
BuildRequires:	gtkspell-devel, gtkspell-devel, tcl-tk >= 8.4.13, cairo-devel
BuildRequires:	gettext, ncurses-devel, pkgconfig, libxml2-devel >= 2.6.28
Obsoletes:	gaim
Provides:	gaim

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols, including AIM (Oscar and TOC), ICQ, IRC, Yahoo!,
MSN Messenger, Jabber, Gadu-Gadu, Napster, and Zephyr.  These
protocols are implemented using a modular, easy to use design.
To use a protocol, just load the plugin for it.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting and C plugins.

Pidgin is NOT affiliated with or endorsed by AOL.

%package devel
Summary:	Development headers, documentation, and libraries for Pidgin
Group:		Applications/Internet
Requires:	%{name} = %{version}, libpurple-devel = %{version}
Requires:	pkgconfig
Obsoletes:	gaim-devel
Provides:	gaim-devel

%package -n libpurple
Summary:	libpurple library for IM clients like Pidgin and Finch
Group:		Applications/Internet
Obsoletes:	gaim-silc
Obsoletes:	gaim-tcl
Obsoletes:	gaim-gadugadu

%package -n libpurple-devel
Summary:	Development headers, documentation, and libraries for libpurple
Group:		Applications/Internet
Requires:	libpurple = %{version}
Requires:	pkgconfig

%package -n finch
Summary:    A text-based user interface for Pidgin
Group:      Applications/Internet
Requires:   libpurple = %{version}

%package -n finch-devel
Summary:    Headers etc. for finch stuffs
Group:      Applications/Internet
Requires:   finch = %{version}, libpurple-devel = %{version}
Requires:   pkgconfig

%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%description -n finch
A text-based user interface for using libpurple.  This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CFLAGS="-g -xs" \
LIBXML_LIBS="-lxml2" \
GTKSPELL_LIBS="-laspell"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS LIBXML_LIBS GTKSPELL_LIBS

./configure \
	--prefix="/usr/local" \
	--x-libraries="/usr/include/X11" \
	--enable-sm \
	--disable-perl \
	--disable-gevolution \
	--enable-startup-notification \
	--disable-gnutls \
	--enable-nss \
	--with-nss-includes="/usr/local/include/nss" \
	--with-nspr-includes="/usr/local/include/nspr" \
	--with-nss-libs="/usr/local/lib" \
	--with-nspr-libs="/usr/local/lib" \
	--with-python \
	--disable-dbus \
	--with-tclconfig="/usr/local/lib" \
	--with-tkconfig="/usr/local/lib" \
	--disable-doxygen \
	--mandir="/usr/local/man" \
	--with-ncurses-headers="/usr/local/include/ncursesw" \
	--disable-schemas-install \
	--enable-gtkspell

gmake %{?_smp_mflags}

%install
gmake DESTDIR=%{buildroot} install

# Delete files that we don't want to put in any of the RPMs
rm -f %{buildroot}%{_libdir}/finch/*.la
rm -f %{buildroot}%{_libdir}/pidgin/*.la
rm -f %{buildroot}%{_libdir}/purple/*.la
rm -f %{buildroot}%{_libdir}/purple/private/*.la
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
/usr/local/gnu/bin/find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
/usr/local/gnu/bin/find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'

%find_lang %{name}

/usr/local/gnu/bin/find $RPM_BUILD_ROOT%{_libdir}/purple-2 -xtype f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" | \
        grep -v /libbonjour.so | \
        grep -v /libsametime.so > %{name}-%{version}-purpleplugins

/usr/local/gnu/bin/find $RPM_BUILD_ROOT%{_libdir}/pidgin -xtype f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-pidginplugins

/usr/local/gnu/bin/find $RPM_BUILD_ROOT%{_libdir}/finch -xtype f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-finchplugins

# files -f file can only take one filename :(
cat %{name}.lang >> %{name}-%{version}-purpleplugins
cat %{name}.lang >> %{name}-%{version}-pidginplugins
cat %{name}.lang >> %{name}-%{version}-finchplugins

%clean
rm -rf %{buildroot}

%files -f %{name}-%{version}-pidginplugins
%defattr(-, root, root)

%doc AUTHORS
%doc COPYING
%doc COPYRIGHT
%doc ChangeLog
%doc NEWS
%doc README
%doc README.MTN
%doc doc/the_penguin.txt
%doc %{_mandir}/man1/pidgin.1
%dir %{_libdir}/pidgin

%{_bindir}/pidgin
%{_datadir}/pixmaps/pidgin
%{_datadir}/icons/hicolor/*/apps/pidgin.*
%dir %{_datadir}/sounds/pidgin
%{_datadir}/sounds/pidgin/*
%{_datadir}/applications/*


%files -f %{name}-%{version}-purpleplugins -n libpurple
%defattr(-, root, root)

%{_libdir}/libpurple.so.*
%dir %{_libdir}/purple-2

%{_datadir}/pixmaps/purple

%files devel
%defattr(-, root, root)
%dir %{_includedir}/pidgin
%{_includedir}/pidgin/*.h
%{_libdir}/pkgconfig/pidgin.pc

%files -n libpurple-devel
%defattr(-, root, root)

%doc ChangeLog.API
%doc HACKING
%doc PLUGIN_HOWTO

%dir %{_includedir}/libpurple
%{_includedir}/libpurple/*.h
%{_libdir}/libpurple.so
%{_libdir}/pkgconfig/purple.pc
%{_datadir}/aclocal/purple.m4

%files -f %{name}-%{version}-finchplugins -n finch
%defattr(-, root, root)

%doc %{_mandir}/man1/finch.*
%{_bindir}/finch
%{_libdir}/libgnt.so.*

%files -n finch-devel
%defattr(-, root, root)
%dir %{_includedir}/finch
%{_includedir}/finch/*.h
# libgnt
%dir %{_includedir}/gnt
%{_includedir}/gnt/*.h
%{_libdir}/pkgconfig/gnt.pc
%{_libdir}/libgnt.so

%changelog
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-4
- Tweeking some aspell issues
* Sun May 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-3
- Removed gconf
- Fixed libxml2 linkage away from Sun
* Sat May 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-2
- Respin
* Sat May 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-1
- Full version build.
* Wed May 02 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0beta7-3
- Added Mono support
* Tue May 01 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta7-2
- Added debug flags.
- Added Finch.
* Mon Apr 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta7-1
- Initial Pidgin build.
- Temporary net-pmp.c build patch for solaris.
* Wed Nov 01 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta4-4
- Bump
* Wed Nov 01 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta4-3
- Added libgaim.so
* Wed Nov 01 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta4-2
- Bump
* Tue Oct 31 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta4
- Bumped to latest beta release. Fixed a bunch of build bugs.
* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0svn
- Changed to latest svn build
* Thu Apr 06 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.0cvs
- Added a devel package, latest cvs build of 2.0
