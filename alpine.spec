Summary: 	University of Washington Pine mail user agent
Name: 		alpine
Version: 	2.00
Release: 	2
License: 	Apache License
Group: 		Applications/Mail
URL:		http://www.washington.edu/alpine
Source: 	ftp://ftp.cac.washington.edu/alpine/%{name}-%{version}.tar.gz
Patch1:		alpine-web-2.00-config.patch
Vendor: 	University of Washington
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  openssl >= 0.9.8h, openldap-devel >= 2.4, aspell
Requires:       openldap >= 2.4, aspell >= 0.60.5, aspell-en >= 0.60.5
Provides:       pine
Obsoletes:      pine

%description
Alpine -- an Alternatively Licensed Program for Internet
News & Email -- is a tool for reading, sending, and managing
electronic messages.  Alpine is the successor to Pine and was
developed by Computing & Communications at the University of
Washington.
  Though originally designed for inexperienced email users,
Alpine supports many advanced features, and an ever-growing number of
configuration and personal-preference options.

%package web
Summary:        Web components for Alternative Pine mail user agent implementation
Group:          Applications/Mail
Requires:       %{name} = %{version}-%{release}
Requires:	apache, ispell
BuildRequires:	tcl
#Note: When we built this it failed because it couldn't find tclsh, since we had /usr/local/bin/tclsh8.4, doing ln -s tclsh8.4 tclsh fixed the problem 

%description web
Alpine -- an Alternatively Licensed Program for Internet
News & Email -- is a tool for reading, sending, and managing
electronic messages.  Alpine is the successor to Pine and was
developed by Computing & Communications at the University of
Washington.
  Though originally designed for inexperienced email users,
Alpine supports many advanced features, and an ever-growing number of
configuration and personal-preference options.

%prep
%setup -q
cd web
%patch1 -p0
cd ..

%build
PATH="/opt/SUNWspro/bin:/usr/local/gnu/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" CFLAGS="-g -xs" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -llber -lnsl -lsocket -Bdirect -zdefs"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

sed 's/\/usr\/bin\/tclsh/\/usr\/local\/bin\/tclsh/g' web/lib/pkgcreate > web/lib/pkgcreate.fix
mv web/lib/pkgcreate.fix web/lib/pkgcreate
chmod +x web/lib/pkgcreate

cd web/bin
rm tclsh
ln -s /usr/local/bin/tclsh tclsh
cd ../..

#We want to link against sun curses not ncurses so change -lncurses to -lcurses
#because alpine has display issues with Solaris Terminal Emulation when build against ncurses
mv configure configure.wrong ; sed -e s/-lncurses/-lcurses/ configure.wrong > configure 
chmod 755 configure



./configure \
	--prefix="/usr/local" \
	--with-spellcheck-prog="aspell" \
	--with-ssl-dir="/usr/local/ssl" \
	--with-ssl-lib-dir="/usr/local/ssl/lib" \
	--without-krb5 \
	--with-ldap-include-dir="/usr/local/include" \
	--with-ldap-lib-dir="/usr/local/lib" \
	--without-ipv6 \
	--disable-nls \
	--enable-quotas \
	--with-system-pinerc="/usr/local/lib/pine.conf" \
	--with-system-fixed-pinerc="/usr/local/lib/pine.conf.fixed"

cd imap
sed -e "s/PASSWDTYPE=std/PASSWDTYPE=pmb/g" Makefile > Makefile.test
sed -e "s/SSLTYPE=nopwd/SSLTYPE=unix.nopwd/g" Makefile.test > Makefile.test2
mv -f Makefile.test2 Makefile

cd src/osdep/unix/
sed -e "s/PASSWDTYPE=std/PASSWDTYPE=pmb/g" Makefile > Makefile.test
sed -e "s/SSLTYPE=nopwd/SSLTYPE=unix.nopwd/g" Makefile.test > Makefile.test2
mv -f Makefile.test2 Makefile
cd ../../../..

gmake

cd web/src
gmake
cd ../..

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 alpine/alpine %{buildroot}/usr/local/bin/alpine
%{__install} -Dp -m0755 pico/pico %{buildroot}/usr/local/bin/pico
%{__install} -Dp -m0755 pico/pilot %{buildroot}/usr/local/bin/pilot
%{__install} -Dp -m0755 alpine/rpload %{buildroot}/usr/local/bin/rpload
%{__install} -Dp -m0755 alpine/rpdump %{buildroot}/usr/local/bin/rpdump
%{__install} -Dp -m0755 imap/mailutil/mailutil %{buildroot}/usr/local/bin/mailutil
%{__install} -Dp -m0755 imap/mlock/mlock %{buildroot}/usr/local/sbin/mlock
%{__install} -Dp -m0644 doc/alpine.1 %{buildroot}/usr/local/man/man1/alpine.1
%{__install} -Dp -m0644 doc/pico.1 %{buildroot}/usr/local/man/man1/pico.1
%{__install} -Dp -m0644 doc/pilot.1 %{buildroot}/usr/local/man/man1/pilot.1
%{__install} -Dp -m0644 doc/rpload.1 %{buildroot}/usr/local/man/man1/rpload.1
%{__install} -Dp -m0644 doc/rpdump.1 %{buildroot}/usr/local/man/man1/rpdump.1
%{__install} -Dp -m0644 imap/src/mailutil/mailutil.1 %{buildroot}/usr/local/man/man1/mailutil.1

# Install web component
cd web/src
gmake install
cd ../..
mkdir -p %{buildroot}/usr/local/libexec/config
cd web
rm detach
cd cgi
rm detach
cd alpine-2.0
rm alpine.tcl
cd lib
rm yui
cd ../../../../

cp -R web %{buildroot}/usr/local/libexec/alpine-%{version}
#make a bogus /var/local/tmp/webpine in the buildroot so that we can link to it
mkdir -p %{buildroot}/var/local/tmp
touch %{buildroot}/var/local/tmp/webpine
cd %{buildroot}/usr/local/libexec/alpine-%{version}
ln -s ../../../../var/local/tmp/webpine detach
cd cgi
ln -s ../../../../../var/local/tmp/webpine detach
cd alpine-2.0
ln -s ../../../../../usr/local/libexec/config/alpine.tcl
#cd ../alpine/2.0
#ln -s ../../../../../usr/local/libexec/config/alpine.tcl
#cd ../../
rm -rf src
#remove the buildroot var so it doesn't get packaged
rm -rf %{buildroot}/var

cd %{buildroot}
cd usr/local/bin
ln -s alpine pine
cd ../../..

cd usr/local/man/man1
ln -s alpine.1 pine.1

%clean
%{__rm} -rf %{buildroot}

%post web
cat <<EOF
================================================================
You MUST link alpine-web to the appropriate Apache document
root. Normally this is done with a link to the apache space, but
a virtual host is preferred in httpd.conf

you may also wish to:

ln -s /usr/local/libexec/alpine-%{version} /usr/local/libexec/alpine
================================================================
EOF

%files
%defattr(-, root, root, 0755)
%doc LICENSE NOTICE README VERSION doc/*.txt
%doc /usr/local/man/man1/alpine.1
%doc /usr/local/man/man1/mailutil.1
%doc /usr/local/man/man1/pico.1
%doc /usr/local/man/man1/pilot.1
%doc /usr/local/man/man1/rpdump.1
%doc /usr/local/man/man1/rpload.1
%doc /usr/local/man/man1/pine.1
/usr/local/bin/alpine
/usr/local/bin/mailutil
/usr/local/bin/pico
/usr/local/bin/pilot
/usr/local/bin/pine
/usr/local/bin/rpdump
/usr/local/bin/rpload

%defattr(2755, root, mail, 0755)
/usr/local/sbin/mlock

%files web
%defattr(-, root, root, 0755)
/usr/local/libexec/alpine-%{version}/*

%changelog
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 2.00-2
- Respin against openldap 2.4
* Wed Aug 27 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.00-1
- bumped to 2.00
- checked patches and spec file for accuracy
- updated web config patch
* Fri Mar 21 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.10-1
- bumped version, commented out Patch0 - no longer needed 
- modified Patch1 so that deskmail.conf is still removed
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-14
- added correct linking for detach -> /var/local/tmp/webpine
* Tue Feb 05 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-13
- removed -xO0 from CFLAGS as per Sun's Forum , added requires tcl
* Mon Jan 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-12
- reverted back to aspell
* Mon Jan 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-11
- removed requires aspell and aspell-en, changed configure to build against Sun spell
* Fri Jan 25 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-10
- added requires: aspell >= 0.60.5 and aspell-en >= 0.60.5, removed BuildConflicts ncurses
* Tue Jan 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-9
- same as 8
* Fri Jan 18 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.00-8
- added BuildConflicts: ncurses
* Tue Jan 08 2008 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.00-7
- Fixed alpine-web segfault
* Fri Dec 21 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.00-1
- First stable release
* Wed Dec 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.999999-3
- Added alpine-web subpackage
* Fri Dec 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.999999-1
- Bump to 0.999999
* Mon Nov 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.99999-4
- Removed Maildir support ;)
* Sat Nov 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.99999
- Bump and setenv() fix
- Added Maildir support
* Fri Nov 02 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.9999
- Initial Rutgers Build.
