%define mysql_ver  3.23.51
%define apache_ver 1.3.26
%define php_ver    4.2.2

%define mysql_prefix  /usr/local/mysql-%{mysql_ver}
%define apache_prefix /usr/local/apache-%{apache_ver}
%define php_prefix    /usr/local/php-%{php_ver}

Summary: The PHP scripting language
Name: php
Version: %{php_ver}
# NEXT RELEASE SHOULD BE %{apache_ver}_1 WHEN VERSION CHANGES
Release: 1ru.apache1.3.26
License: PHP License
Group: Development/Languages
Source0: php-%{php_ver}.tar.bz2
#Source1: php_c-client-4.1.1.tar.bz2
Source1: imap.tar.Z
Patch: php-4.1.1.patch
BuildRoot: %{_tmppath}/%{name}-root

Conflicts: apache < %{apache_ver}  apache > %{apache_ver}
Requires: mysql > 3.22  mysql < 3.24
Requires: mm openssl gdbm openldap >= 2.1.2
BuildRequires: patch make gdbm openldap >= 2.1.2 openldap-devel >= 2.1.2
BuildRequires: mysql-devel = %{mysql_ver}
BuildRequires: apache-devel > 1.3 apache-devel < 1.4

%description
PHP is a popular scripting language used for CGI programming.  This
package contains an Apache module as well as a standalone executable.

%package devel
Group: Development/Headers
Summary: includes for php

%description devel
includes for php

%prep
%setup -q
%patch -p1
%setup -q -D -T -b 1
#mv ../php-4.1.1/c-client ./
mv ../imap-2001a ./
#%patch -p1

%build


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

# we are currently using multiple db's in php. openldap uses db4
# watch new releases of php for db4 support and try switching over
# when available.

SSL_BASE="/usr/local/ssl"
EAPI_MM="/usr/local"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_prefix}/lib/mysql -R%{mysql_prefix}/lib/mysql"
LD_PRELOAD="/usr/local/lib/libldap.so.2.0.102"
LD_RUN_PATH="/usr/local/lib:%{mysql_prefix}/lib/mysql"
CPPFLAGS="-I/usr/local/include"
#LIBS="-lru"
export SSL_BASE EAPI_MM LDFLAGS CPPFLAGS LIBS LD_RUN_PATH LD_PRELOAD

CC="cc" ./configure --prefix=%{php_prefix} --enable-track-vars \
  --enable-force-cgi-redirect --with-gettext --with-ndbm --enable-ftp \
  --with-apxs=%{apache_prefix}/bin/apxs --with-mysql=/%{mysql_prefix} \
  --with-openssl=/usr/local/ssl --with-imap=imap-2001a/c-client \
  --enable-shared --enable-sysvshm --enable-sysvsem --with-gd \
  --with-ldap=/usr/local/ --with-bz2 --with-zlib

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

%post
if [ ! -r /usr/local/php ]; then
	ln -s /usr/local/php-%{version} /usr/local/php
	echo /usr/local/php now points to /usr/local/php-%{version}
fi
cat <<EOF
To complete your PHP install switch to the apache bin directory
> cd /usr/local/apache-%{apache_ver}/bin
and execute (as privledged user)
> ./apxs -aen php4 /usr/local/apache-%{apache_ver}/libexec/libphp4.so
EOF


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, other)
%doc TODO CODING_STANDARDS CREDITS LICENSE
/usr/local/php-%{version}/php.ini*
/usr/local/php-%{version}/bin
/usr/local/php-%{version}/lib
/usr/local/apache-%{apache_ver}/libexec/libphp4.so
#%{php_prefix}

%files devel
%defattr(-, root, other)
/usr/local/php-%{version}/include

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
