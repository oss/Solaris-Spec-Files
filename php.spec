%define mysql_ver  3.23.47
%define apache_ver 1.3.26
%define php_ver    4.2.1

%define mysql_prefix  /usr/local/mysql-%{mysql_ver}
%define apache_prefix /usr/local/apache-%{apache_ver}
%define php_prefix    /usr/local/php-%{php_ver}

Summary: The PHP scripting language
Name: php
Version: %{php_ver}
# NEXT RELEASE SHOULD BE %{apache_ver}_1 WHEN VERSION CHANGES
Release: 5
License: PHP License
Group: Development/Languages
Source0: php-%{version}.tar.bz2
#Source1: php_c-client-4.1.1.tar.bz2
Source1: imap.tar.Z
Patch: php-4.1.1.patch
BuildRoot: %{_tmppath}/%{name}-root

Conflicts: apache < %{apache_ver}  apache > %{apache_ver}
#Requires: mysql = %{mysql_ver}
%ifos solaris2.8
Requires: mm openssl gdbm openldap
%else
Requires: mm openssl gdbm
%endif
BuildRequires: patch make gdbm
BuildRequires: mysql-devel = %{mysql_ver}
BuildRequires: apache-devel > 1.3 apache-devel < 1.4

%description
PHP is a popular scripting language used for CGI programming.  This
package contains an Apache module as well as a standalone executable.
*Solaris 8 packages have LDAP support, 2.6 and 2.7 do not have LDAP
support.*

%prep
%setup -q
%patch -p1
%setup -q -D -T -b 1
#mv ../php-4.1.1/c-client ./
mv ../imap-2001a ./
#%patch -p1

%build
SSL_BASE="/usr/local/ssl"
EAPI_MM="/usr/local"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_prefix}/lib -R%{mysql_prefix}/lib"
CPPFLAGS="-I/usr/local/include"
#LIBS="-lru"
export SSL_BASE EAPI_MM LDFLAGS CPPFLAGS LIBS

#TOPDIR=`pwd`

cd imap-2001a
make sol
cd c-client
mkdir include
mkdir lib
ln -s c-client.a libc-client.a
mv *.a lib
mv *.o *.c *.h include
cd ../..

%ifos solaris2.8
./configure --prefix=%{php_prefix} --enable-track-vars \
  --enable-force-cgi-redirect --with-gettext --with-ndbm --enable-ftp \
  --with-apxs=%{apache_prefix}/bin/apxs --with-mysql=/%{mysql_prefix} \
  --with-openssl=/usr/local/ssl --with-imap=imap-2001a/c-client \
  --enable-shared --enable-sysvshm --enable-sysvsem --with-gd \
  --with-ldap=/usr/local/ --with-bz2 --with-zlib 
%else
./configure --prefix=%{php_prefix} --enable-track-vars \
  --enable-force-cgi-redirect --with-gettext --with-ndbm --enable-ftp \
  --with-apxs=%{apache_prefix}/bin/apxs --with-mysql=/%{mysql_prefix} \
  --with-openssl=/usr/local/ssl --with-imap=imap-2001a/c-client \
  --enable-shared --enable-sysvshm --enable-sysvsem --with-gd \
  --with-bz2 --with-zlib 
%endif

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

TOPDIR=`pwd`

/bin/sh $TOPDIR/libtool --silent --silent --mode=install cp libphp4.la \
  $TOPDIR/libs/libphp4.la >/dev/null 2>&1
mkdir -p %{buildroot}%{php_prefix}/bin
mkdir -p %{buildroot}%{php_prefix}/libexec
mkdir -p %{buildroot}/usr/local/apache-%{apache_ver}/libexec

install -m 0644 $TOPDIR/php.ini-dist %{buildroot}/usr/local/php-%{version}/
install -m 0644 $TOPDIR/php.ini-recommended %{buildroot}/usr/local/php-%{version}/

install -m 0755 $TOPDIR/.libs/libphp4.so \
  %{buildroot}/usr/local/apache-%{apache_ver}/libexec/libphp4.so

mkdir -p %{buildroot}%{apache_prefix}/libexec

cd $TOPDIR/pear && make install prefix=%{buildroot}%{php_prefix}
cd %{buildroot}/usr/local/
ln -s php-%{version} php

%post
%ifos solaris2.8
cat <<EOF
Install with
> apxs -aen php4 /usr/local/apache-%{apache_ver}/libexec/libphp4.so
EOF
%else
cat <<EOF
ONLY THE SOLARIS 2.8 PACKAGES HAVE LDAP SUPPORT, THIS ONE DOES NOT
Install with
> apxs -aen php4 /usr/local/apache-%{apache_ver}/libexec/libphp4.so
EOF
%endif


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, other)
%doc TODO CODING_STANDARDS CREDITS LICENSE
/usr/local/php-%{version}/php.ini*
/usr/local/php-%{version}/bin
/usr/local/php-%{version}/include
/usr/local/php-%{version}/lib
/usr/local/php
/usr/local/apache-%{apache_ver}/libexec/libphp4.so
#%{php_prefix}

%changelog
* Tue Feb 5 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Made path change for post-install information to point to 
  correct libphp4.so. 

* Mon Feb 4 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Apache 1.3.23

* Wed Jan 30 2002 Christopher Suleski <chrisjs@nbcs.rutgers.edu>
- Upgraded to PHP 4.1.1 against Apache 1.3.22, MySQL 3.23.47

* Fri Dec 21 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to PHP 4.1.0 against Apache 1.3.22, MySQL 3.23.46
- Changed build to match TINT package
