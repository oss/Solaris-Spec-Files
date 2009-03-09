Summary: 	A Gtk+ based multiprotocol instant messaging client
Name: 		pidgin
Version: 	2.5.5
Release: 	1
License: 	GPL
Group: 		Applications/Internet
Source: 	%{name}-%{version}.tar.bz2
Patch:		pidgin-2.5.4-duplicates-adding.patch
URL: 		http://www.pidgin.im
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root

Requires:	libpurple = %{version}-%{release}
Requires:	nss >= 3.11-2, gtk2 >= 2.12.11-3, gtkspell >= 2.0.11, aspell-en, cairo >= 1.6.4,
Requires:	libxml2 >= 2.6.32, ncurses >= 5.6, tcl-tk >= 8.4.16, gstreamer >= 0.10.20
Requires:	fontconfig >= 2.6.0-2, startup-notification, hicolor-icon-theme

BuildRequires: 	nss-devel, gtk2-devel, gtkspell-devel, cairo-devel, libxml2-devel >= 2.6.32, ncurses-devel 
BuildRequires:	tcl-headers, tcl-tk, gstreamer-devel, fontconfig-devel, startup-notification-devel
BuildRequires:  libtool, intltool, gettext, pkgconfig, libpng3-devel, xrender-devel, pixman-devel
BuildRequires:	expat, expat-static

Obsoletes:	gaim
Provides:	gaim

Conflicts:	finch < %{version}-%{release} finch > %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}, libpurple-devel = %{version}-%{release}
Requires:	pkgconfig
Obsoletes:	gaim-devel
Provides:	gaim-devel

%package -n libpurple
Summary:	libpurple library for IM clients like Pidgin and Finch
Group:		Applications/Internet
Obsoletes:	gaim-silc
Obsoletes:	gaim-tcl
Obsoletes:	gaim-gadugadu
Conflicts:	pidgin < %{version}-%{release} pidgin > %{version}-%{release}
Conflicts:	finch < %{version}-%{release} finch > %{version}-%{release}

%package -n libpurple-devel
Summary:	Development headers, documentation, and libraries for libpurple
Group:		Applications/Internet
Requires:	libpurple = %{version}-%{release}
Requires:	pkgconfig

%package -n finch
Summary:	A text-based user interface for Pidgin
Group:		Applications/Internet
Requires:	libpurple = %{version}-%{release}
Conflicts:	pidgin < %{version}-%{release} pidgin > %{version}-%{release}

%package -n finch-devel
Summary:	Headers etc. for finch stuffs
Group:		Applications/Internet
Requires:	finch = %{version}-%{release}, libpurple-devel = %{version}-%{release}
Requires:	pkgconfig

%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ, Simple and Zephyr.

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
%patch -p1

%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
CFLAGS="-D__unix__"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LIBXML_LIBS="-lxml2 -lX11"
export PATH CC CXX CPPFLAGS CFLAGS LD LDFLAGS LIBXML_LIBS

./configure \
	--prefix="%{_prefix}"					\
	--mandir="%{_mandir}"					\
	--x-includes="/usr/openwin/include" 			\
	--x-libraries="/usr/openwin/lib" 			\
        --with-nss-includes="%{_includedir}/nss"                \
	--with-nss-libs="%{_libdir}"                            \
        --with-nspr-includes="%{_includedir}/nspr"              \
        --with-nspr-libs="%{_libdir}"                           \
        --with-tclconfig="%{_libdir}"                           \
        --with-tkconfig="%{_libdir}"                            \
        --with-ncurses-headers="%{_includedir}/ncursesw"        \
	--enable-consoleui					\
	--enable-startup-notification				\
	--enable-sm 						\
	--with-python						\
	--disable-perl 						\
	--disable-gevolution 					\
	--disable-gnutls 					\
	--disable-dbus 						\
	--disable-doxygen 					\
	--disable-schemas-install 				\
	--disable-meanwhile 					\
	--disable-avahi 					\
	--disable-nls 

gmake -j3

%install
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
export PATH

gmake DESTDIR=%{buildroot} install

# Delete files that we don't want to put in any of the RPMs
rm -f %{buildroot}%{_libdir}/finch/*.la
rm -f %{buildroot}%{_libdir}/pidgin/*.la
rm -f %{buildroot}%{_libdir}/purple/*.la
rm -f %{buildroot}%{_libdir}/purple-2/*.la
rm -f %{buildroot}%{_libdir}/purple/private/*.la
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/gnt/irssi.la
rm -f %{buildroot}%{_libdir}/gnt/s.la
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
/usr/local/gnu/bin/find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
/usr/local/gnu/bin/find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'

/usr/local/gnu/bin/find %{buildroot}%{_libdir}/purple-2 -xtype f -print | \
	sed "s@^%{buildroot}@@g" | \
	grep -v /libbonjour.so | \
	grep -v /libsametime.so > %{name}-%{version}-purpleplugins

/usr/local/gnu/bin/find %{buildroot}%{_libdir}/pidgin -xtype f -print | \
        sed "s@^%{buildroot}@@g" > %{name}-%{version}-pidginplugins

/usr/local/gnu/bin/find %{buildroot}%{_libdir}/finch -xtype f -print | \
        sed "s@^%{buildroot}@@g" > %{name}-%{version}-finchplugins

%clean
rm -rf %{buildroot}

%post
touch -c %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch -c %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


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
%dir %{_datadir}/sounds/purple
%{_datadir}/sounds/purple/*
%{_datadir}/applications/*

%files -f %{name}-%{version}-purpleplugins -n libpurple
%defattr(-, root, root)

%{_libdir}/libpurple.so.*
%dir %{_libdir}/purple-2
%{_datadir}/purple/ca-certs/*

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
%{_libdir}/gnt/irssi.so
%{_libdir}/gnt/s.so

%files -n finch-devel
%defattr(-, root, root)
%dir %{_includedir}/finch
%{_includedir}/finch/*.h
%dir %{_includedir}/gnt
%{_includedir}/gnt/*.h
%{_libdir}/pkgconfig/gnt.pc
%{_libdir}/libgnt.so
%{_libdir}/pkgconfig/finch.pc

%changelog
* Mon Mar 09 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.5-1
- Updated to version 2.5.5
- Made some minor SPEC file changes
- Cleaned things up a bit
* Wed Jan 14 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.4-1
- Updated to version 2.5.4
- Added some things to BuildRequires
- Modified the duplicates patch to make it work with the new pidgin
* Mon Dec 22 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.3-1
- Added duplicates-adding.2.patch and updated to 2.5.3
* Tue Oct 21 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.5.2-1
- Updated to 2.5.2 
* Tue Sep 02 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.1-1
- Added some Conflicts, updated to version 2.5.1
* Fri Aug 29 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.0-3
- Made some Requires/BuildRequires changes, removed patch
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.0-2
- Respin against gstreamer 0.10.20
* Fri Aug 22 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.0-1
- Updated to version 2.5.0
- Added a patch so that configure does not check for gettext
* Wed Jul 2 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.4.3-1
- Updated to version 2.4.3
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.4.2-1
- Updated to version 2.4.2
* Thu Apr 03 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.4.1-1
- Updated to the latest version
* Mon Dec 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3.1-2
- Fixed GNT compile issue
- Added -D__unix__
* Mon Nov 26 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.3.0-1
- Bump to 2.3.0
* Sat Sep 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.2.1-1
- Bump to 2.2.1
* Fri Sep 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.2.0-1
- Bump to 2.2.0
- Patched dos line endings
* Tue Aug 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.1.1-1
- Bumping to 2.1.1
* Tue Aug 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.1.0-2
- Trying a new s.c patch
* Mon Jul 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.1.0-1
- Bump!
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.2-2
- Bump to fix the elusive GTK segfault bug
* Mon Jun 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.2-1
* Version bump
* Mon May 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.1-2
* Trying new finch patch
* Fri May 25 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.1-1
- Version bump
* Sat May 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-8
- Respin and some more testing
* Mon May 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-7
- Added dependencies, respun against new gtk
* Fri May 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-6
- Added gtk-icon-cache
- Turned gtkspell back on
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-5
- Disabled gtkspell to debug
* Thu May 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-4
- Tweeking some aspell issues
* Sun May 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-3
- Removed gconf
- Fixed libxml2 linkage away from Sun
* Sat May 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-2
- Respin
* Sat May 05 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0-1
- Full version build.
