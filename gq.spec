Name:		gq
Summary:	Interactive graphical LDAP browser
Version:	1.2.3
Release:	1
License:	GPL
Group:		Networking/Utilities
URL:		http://biot.com/gq/
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		gq-%{version}.tar.gz
Patch:          fix_missing_setenv.patch
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	openldap-lib >= 2.4 gtk2 gnome-keyring atk
Requires:	libglade libxml2 cairo openssl >= 0.9.8
Requires:	perl-module-XML-Parser libgcrypt pango
BuildRequires:	openldap-devel >= 2.4 gtk2-devel gnome-keyring-devel 
BuildRequires:	cairo-devel pixman-devel perl-module-XML-Parser libglade-devel 
BuildRequires:	libxml2-devel openssl >= 0.9.8 libgcrypt-devel atk-devel pango-devel

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

sed \
	-e 's/ENABLE_NLS 1/ENABLE_NLS 0/g' \
	-e 's/USE_NLS=yes/USE_NLS=no/g' -i configure

./configure \
	--without-included-gettext \
	--prefix=%{_prefix} \
	--enable-cache \
	--enable-browser-dnd \
	--disable-update-mimedb \
	--disable-nls
gmake -j3

%install
gmake DESTDIR=%{buildroot} install-strip

cat << EOF

This package does not link properly, so to get it to work, you need to 
link /usr/local/lib/libcrypto.so.0.9.8 to /usr/lib/libcrypto.so.0.9.8

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/gq
%{_datadir}/gq
%{_datadir}/pixmaps/gq
%{_datadir}/applications/gq.desktop 
%{_datadir}/mime/packages/gq-ldif.xml
%doc README COPYING ChangeLog NEWS TODO AUTHORS

%changelog
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.2.3-1
- Built against openldap 2.4, updated to version 1.2.3

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
