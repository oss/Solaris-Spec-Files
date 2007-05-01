
%define name pidgin
%define version 2.0.0beta7 
%define release 1
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
Patch0:		pidgin_net_pmp_bug.patch
Requires:	nss, gtk2 >= 2.2.2, python >= 2.4, gtkspell >= 2.0.11
Requires:	startup-notification, python >= 2.4, tcl-tk >= 8.4.13
BuildRequires: 	make, nss-devel, gtk2-devel >= 2.2.2, intltool
BuildRequires:	startup-notification, python >= 2.4, tcl-headers >= 8.4.13
BuildRequires:	gtkspell-devel, gtkspell-devel, tcl-tk >= 8.4.13
BuildRequires:	libxml2-devel
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


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local  --x-libraries=/usr/include/X11 \
--disable-nas --enable-sm --disable-perl --disable-gevolution \
--enable-startup-notification --disable-nls --disable-gnutls \
--enable-nss --with-nss-includes=/usr/local/include/nss \
--with-nspr-includes=/usr/local/include/nspr \
--with-nss-libs=/usr/local/lib --with-nspr-libs=/usr/local/lib \
--with-python --disable-dbus --with-tclconfig=/usr/local/lib \
--with-tkconfig=/usr/local/lib --disable-doxygen

make

%install
make install DESTDIR=%{buildroot}

# Delete files that we don't want to put in any of the RPMs
rm -f %{buildroot}%{_libdir}/finch/*.la
rm -f %{buildroot}%{_libdir}/pidgin/*.la
rm -f %{buildroot}%{_libdir}/purple/*.la
rm -f %{buildroot}%{_libdir}/purple/liboscar.so
rm -f %{buildroot}%{_libdir}/purple/libjabber.so
rm -f %{buildroot}%{_libdir}/purple/private/*.la
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
/usr/local/gnu/bin/find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
/usr/local/gnu/bin/find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'

%find_lang %{name}

/usr/local/gnu/bin/find $RPM_BUILD_ROOT%{_libdir}/purple-2 -xtype f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" | \
        grep -v /libbonjour.so | \
        grep -v /libsametime.so | \
        grep -v /mono.so | \
        grep -v ".dll$" > %{name}-%{version}-purpleplugins

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
%doc /usr/local/share/man/man1/pidgin.1
%doc /usr/local/share/man/man1/finch.1
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


%changelog
* Mon Apr 30 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0beta7-1
- Initial Pidgin build.
- Temporary net-pmp.c build patch for solaris


