%define mysql_ver  3.23.51
%define apache_ver 1.3.27
%define php_ver    4.3.1

%define mysql_prefix  /usr/local/mysql-%{mysql_ver}
%define apache_prefix /usr/local/apache-1.3.27
%define apache2_prefix /usr/local/apache2-2.0.44
%define php_prefix    /usr/local
#%define php_prefix    /usr/local/php-%{php_ver}

Summary: The PHP scripting language
Name: php
Version: %{php_ver}
Release: 2
License: PHP License
Group: Development/Languages
Source0: php-%{php_ver}.tar.bz2
#Source1: php_c-client-4.1.1.tar.bz2
Source1: imap.tar.Z
Patch: php-4.1.1.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: php-common php-bin apache-module-php apache2-module-php
BuildRequires: patch make gdbm openldap >= 2.1.8 openldap-devel >= 2.1.8
BuildRequires: mysql-devel = %{mysql_ver} openssl >= 0.9.6g
BuildRequires: apache apache-devel apache2 apache2-devel


%description
PHP is a popular scripting language used for CGI programming.  This
package contains an Apache module as well as a standalone executable.


%package common
Group: Development/Languages
Summary: configuration files for php
Requires: mysql > 3.22  mysql < 3.24 mm openssl >= 0.9.6g gdbm openldap >= 2.1.2

%description common
php config files


%package bin
Group: Development/Languages
Summary: PHP CLI
Requires: php-common

%description common
PHP CLI


%package devel
Group: Development/Headers
Summary: includes for php
Requires: php-common

%description devel
includes for php


%package -n apache2-module-php
Group: Internet/Web
Summary: PHP module for Apache 2
Requires: php-common >= 4.3.0 apache2

%description -n apache2-module-php
PHP module for Apache 2


%package -n apache-module-php
Group: Internet/Web
Summary: PHP module for Apache 1.3.x
Requires: php-common >= 4.3.0 apache

%description -n apache-module-php
PHP module for Apache


%prep
%setup -q
%patch -p1
%setup -q -D -T -b 1
#mv ../php-4.1.1/c-client ./
mv ../imap-2001a ./
#%patch -p1


%build

# start build c-client

cd imap-2001a
make sol
cd c-client
mkdir include
mkdir lib
ln -s c-client.a libc-client.a
mv *.a lib
mv *.o *.c *.h include
cd ../..

#end c-client

# we are currently using multiple db's in php. openldap uses db4
# watch new releases of php for db4 support and try switching over
# when available.

SSL_BASE="/usr/local/ssl"
EAPI_MM="/usr/local"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_prefix}/lib/mysql \
    -R%{mysql_prefix}/lib/mysql"
LD_RUN_PATH="/usr/local/lib:%{mysql_prefix}/lib/mysql"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib -R/usr/local/lib \
    -L%{mysql_prefix}/lib/mysql -R%{mysql_prefix}/lib/mysql"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib:%{mysql_prefix}/lib/mysql"
CPPFLAGS="-I/usr/sfw/include -I/usr/local/include"

export SSL_BASE EAPI_MM LDFLAGS CPPFLAGS LIBS LD_RUN_PATH # LD_PRELOAD


MAINFLAGS="--prefix=%{php_prefix} --enable-track-vars \
 --enable-force-cgi-redirect --with-gettext --with-ndbm --enable-ftp \
  --with-mysql=/%{mysql_prefix} \
  --with-openssl=/usr/local/ssl --with-imap=imap-2001a/c-client \
  --enable-shared --enable-sysvshm --enable-sysvsem --with-gd \
  --with-ldap=/usr/local --with-bz2 --with-zlib \
  --with-config-file-path=/usr/local/etc"

%ifos solaris2.9
EXTRAFLAGS="-with-png-dir=/usr/sfw --with-jpeg-dir=/usr/sfw"
%else
EXTRAFLAGS=""
%endif

export MAINFLAGS EXTRAFLAGS

# Apparently you can't build the Apache 1 and 2 modules at the same time.

CC="gcc" ./configure $MAINFLAGS $EXTRAFLAGS --with-apxs=%{apache_prefix}/bin/apxs
make
mv .libs/libphp4.so apache13-libphp4.so

CC="gcc" CPPFLAGS="$CPPFLAGS -I%{apache2_prefix}/include" ./configure $MAINFLAGS $EXTRAFLAGS --with-apxs2=%{apache2_prefix}/bin/apxs
make
mv .libs/libphp4.so apache2-libphp4.so

rm config.cache && ./configure $MAINFLAGS --with-pear=/usr/local/lib/php

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/local/apache-modules
mkdir -p %{buildroot}/usr/local/apache2-modules
mkdir -p %{buildroot}/usr/local/php/lib
mkdir -p %{buildroot}/usr/local/bin/
mkdir -p %{buildroot}/usr/local/etc

install -m 0755 apache13-libphp4.so %{buildroot}/usr/local/apache-modules/libphp4.so
install -m 0755 apache2-libphp4.so %{buildroot}/usr/local/apache2-modules/libphp4.so

install -m 0644 php.ini-dist %{buildroot}/usr/local/php-%{version}/lib/
install -m 0644 php.ini-recommended %{buildroot}/usr/local/php-%{version}/lib/
ln -sf php.ini-recommended %{buildroot}/usr/local/php-%{version}/lib/

install -m 0755 sapi/cli/php %{buildroot}/usr/local/bin/

make install-pear INSTALL_ROOT=%{buildroot}


%post
cat<<EOF

PHP will now look in /usr/local/etc for the php.ini file.

This is different from previous package releases where the file was to
be located in the /usr/local/php-ver/lib directory.

EOF

%post -n apache2-module-php
#if [ ! -r /usr/local/php ]; then
#	ln -s /usr/local/php-%{version} /usr/local/php
#	echo /usr/local/php now points to /usr/local/php-%{version}
#fi
cat <<EOF
From http://www.php.net/manual/en/install.apache2.php:

 *** Warning ***
 * Do not use Apache 2.0 and PHP in a production environment 
 * neither on Unix nor on Windows. 

TO COMPLETE THE INSTALLATION: put these lines in your httpd.conf:
     LoadModule php4_module ../apache2-modules/libphp4.so
     AddType application/x-httpd-php .php

EOF

%post -n apache-module-php
cat <<EOF

TO COMPLETE THE INSTALLATION: put these lines in your httpd.conf:
     LoadModule php4_module ../apache-modules/libphp4.so
     AddType application/x-httpd-php .php

EOF


%clean
rm -rf %{buildroot}

%files common
%defattr(-, root, other)
%doc TODO CODING_STANDARDS CREDITS LICENSE
%config(noreplace)/usr/local/php-%{version}/lib/php.ini
/usr/local/php-%{version}/lib/php.ini-dist
/usr/local/php-%{version}/lib/php.ini-recommended

%files bin
%defattr(-, root, other)
/usr/local/bin/php

%files devel
%defattr(-, root, other)
/usr/local/php-%{version}/include

%files -n apache2-module-php
%defattr(-, root, other)
/usr/local/apache2-modules/libphp4.so

%files -n apache-module-php
%defattr(-, root, other)
/usr/local/apache-modules/libphp4.so


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
