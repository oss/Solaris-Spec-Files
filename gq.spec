%define name gq
%define version 0.7.0beta1
%define release 1
%define prefix /usr/local

Name:		%name
Summary:	Interactive graphical LDAP browser
Version:	%version
Release:	%release
Copyright:	GPL
Group:		Networking/Utilities
URL:		http://biot.com/gq/
Packager:	Bert Vermeulen <bert@biot.com>
Source:		gq-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root

%description
GQ is GTK+ LDAP client and browser utility. It can be used
for searching LDAP directory as well as browsing it using a
tree view.

%prep
%setup

%build
# tried to build it against gtk2, didn't work nicely
#GTK_CONFIG="/usr/local/bin/pkg-config gtk+-2.0"  \
#LDFLAGS=`pkg-config gtk+-2.0  --libs` CFLAGS=`pkg-config gtk+-2.0 --cflags` \
#./configure --prefix=/usr/local --disable-nls

# only working on 9 and 9-64 for now
PATH="/usr/sfw/bin:$PATH" \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
./configure --prefix=%{prefix} --disable-nls # --enable-cache --enable-browser-dnd
make

%install
make DESTDIR=$RPM_BUILD_ROOT install-strip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{prefix}/bin/gq
%{prefix}/share/gnome/apps/Internet/gq.desktop
%dir %{prefix}/share/pixmaps/gq
%{prefix}/share/pixmaps/gq/*
#%{prefix}/share/locale/*/LC_MESSAGES/*.mo

%doc README
%doc INSTALL
%doc COPYING
%doc ChangeLog
%doc NEWS
%doc TODO
%doc AUTHORS
%doc ABOUT-NLS
%doc README.TLS
%doc README.NLS


%changelog
* Thu Apr 25 2002 Peter Stamfest <peter@stamfest.at>
- Updated for I18N, added new enable arguments as a remainder

* Mon Sep 25 2000 Bert Vermeulen <bert@biot.com
- changed RPM spec maintainer

* Wed Mar 08 2000 Ross Golder <rossigee@bigfoot.com>
- Integrated spec file into source tree
- Added GNOME panel menu entry

* Fri May 28 1999 Borek Lupomesky <Borek.Lupomesky@ujep.cz>
- Update to 0.2.2

* Sat May 22 1999 Borek Lupomesky <Borek.Lupomesky@ujep.cz>
- Modified spec to use buildroot
