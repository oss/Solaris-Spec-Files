
Summary:	Alternative Pine mail user agent implementation
Name:		alpine
Version:	1.00
Release:	7
License:	Apache License
Group:		Applications/Internet
URL:		http://www.washington.edu/alpine/
Source:		ftp://ftp.cac.washington.edu/alpine/alpine.tar.bz2
Patch0:		alpine-web-1.00-sunfix.patch
Patch1:		alpine-web-1.00-config.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	aspell, openssl >= 0.9.8g, openldap-devel
Requires:	openldap, aspell-en
Provides:	pine
Obsoletes:	pine

%description
Alpine (Alternatively Licensed Program for Internet News & Email) is a tool
for reading, sending, and managing electronic messages. Alpine is the
successor to Pine and was developed by Computing & Communications at the
University of Washington.  

Though originally designed for inexperienced email users, Alpine supports
many advanced features, and an ever-growing number of configuration and
personal-preference options.

%package web
Summary:        Web components for Alternative Pine mail user agent implementation
Group:          Applications/Internet
Requires:       %{name} = %{version}
Requires:	apache, ispell
BuildRequires:	tcl

%description web
Alpine (Alternatively Licensed Program for Internet News & Email) is a tool
for reading, sending, and managing electronic messages. Alpine is the
successor to Pine and was developed by Computing & Communications at the
University of Washington.

Though originally designed for inexperienced email users, Alpine supports
many advanced features, and an ever-growing number of configuration and
personal-preference options.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/local/gnu/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" CFLAGS="-g -xs -xO0" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -llber -lnsl -lsocket -Bdirect -zdefs"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

sed 's/\/usr\/bin\/tclsh/\/usr\/local\/bin\/tclsh/g' web/lib/pkgcreate > web/lib/pkgcreate.fix
mv web/lib/pkgcreate.fix web/lib/pkgcreate
chmod +x web/lib/pkgcreate

cd web/bin
rm tclsh
ln -s /usr/local/bin/tclsh tclsh
cd ../..

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

make
cd web/src
make
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
make install
cd ../..
mkdir -p %{buildroot}/usr/local/libexec
cp -R web %{buildroot}/usr/local/libexec/alpine-%{version}
cd %{buildroot}/usr/local/libexec/alpine-%{version}
rm -rf src

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
