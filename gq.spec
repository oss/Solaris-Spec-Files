%define name gq
%define version 1.2.2
%define release 3
%define prefix /usr/local

Name:		%name
Summary:	Interactive graphical LDAP browser
Version:	%version
Release:	%release
Copyright:	GPL
Group:		Networking/Utilities
URL:		http://biot.com/gq/
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
Source:		gq-%{version}.tar.gz
Patch:          fix_missing_setenv.patch
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	gtk2 gnome-keyring perl-module-XML-Parser libglade libxml2 openssl >= 0.9.8
BuildRequires:	openldap-devel >= 2.3 openldap-lib >= 2.3 gtk2-devel gnome-keyring-devel 
BuildRequires:	perl-module-XML-Parser libglade-devel libxml2-devel openssl >= 0.9.8

%description
GQ is GTK+ LDAP client and browser utility. It can be used
for searching LDAP directory as well as browsing it using a
tree view.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

sed -e 's/ENABLE_NLS 1/ENABLE_NLS 0/g' configure > configure.wrong
mv configure.wrong configure

sed -e 's/USE_NLS=yes/USE_NLS=no/g' configure > configure.wrong
mv configure.wrong configure
chmod +x configure

./configure \
	--without-included-gettext \
	--prefix=%{prefix} \
	--enable-cache \
	--enable-browser-dnd \
	--disable-update-mimedb \
	--disable-nls
gmake -j3

%install
gmake DESTDIR=$RPM_BUILD_ROOT install-strip

cat<<EOF

This package does not link properly, so to get it to work, you need to 
link /usr/local/lib/libcrypto.so.0.9.8 to /usr/lib/libcrypto.so.0.9.8

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{prefix}/bin/gq
%{prefix}/share/applications/gq.desktop 
%dir %{prefix}/share/pixmaps/gq
%{prefix}/share/gq/gq.glade
%{prefix}/share/mime/packages/gq-ldif.xml
%{prefix}/share/pixmaps/gq/*
#%{prefix}/share/locale/*/LC_MESSAGES/*.mo

%doc README
%doc INSTALL
%doc COPYING
%doc ChangeLog
%doc NEWS
%doc TODO
%doc AUTHORS

%changelog
* Mon Nov 19 2007 David lee Halik <dhalik@nbcs.rutgers.edu> - 1.2.2-3
- NLS completed hacked out
 
* Sun Nov 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.2.2-2
- Respun against gettext 0.17

* Thu Dec 07 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.2-1
- Updated to 1.2.2-1, switched to GTK2, redid patch and fixed other things

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
