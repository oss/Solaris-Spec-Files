%define mysql_ver  5.0.22
%define apache_ver 1.3.34
%define php_ver    5.1.4
%define apache2_ver 2.2.0

%define mysql_prefix  /usr/local/mysql-%{mysql_ver}
%define apache_prefix /usr/local/apache-%{apache_ver}
%define apache2_prefix /usr/local/apache2-%{apache2_ver}
%define php_prefix    /usr/local
#%define php_prefix    /usr/local/php-%{php_ver}

Summary: The PHP scripting language
Name: php5
Version: %{php_ver}
Release: 1
License: PHP License
Group: Development/Languages
Source0: php-%{php_ver}.tar.bz2
Source1: imap-2004g.tar.Z
Patch0: php-4.1.1.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: php5-common = %{version}-%{release} apache2-module-php5 = %{version}-%{release} apache-module-php5 = %{version}-%{release} 
BuildRequires: patch freetype2-devel make libmcrypt freetype2 gdbm openldap >= 2.3 openldap-devel >= 2.3 mysql5-devel >= %{mysql_ver} openssl >= 0.9.7e apache apache-devel = %{apache_ver} apache2 apache2-devel = %{apache2_ver} curl freetds-devel freetds-lib libxml2-devel libxml2 libpng3-devel libjpeg >= 6b-11 aspell


%description
kPHP is a popular scripting language used for CGI programming.
It is available as an Apache module as well as a standalone executable.


%package common
Group: Development/Languages
Summary: configuration files for php
Requires: libtool mysql5 > 5.0  mysql5 < 5.1 mm openssl >= 0.9.7e gdbm openldap >= 2.3 gd libmcrypt mysql5 freetype2 openldap-lib >= 2.3 curl expat freetds-lib libxml2 >= 2.6.22 libjpeg >= 6b-11


%description common
php config files


%package devel
Group: Development/Headers
Summary: includes for php
Requires: php5-common = %{version}-%{release}
Conflicts: php5-bin
Obsoletes: php5-bin

%description devel
The devel package includes everything you need to actually use PHP. Install
this if you care to use PHP for more than blindly running code on your web
server.

%package -n apache2-module-php5
Group: Internet/Web
Summary: PHP module for Apache 2
Requires: php5-common = %{version}-%{release} apache2

%description -n apache2-module-php5
PHP module for Apache 2


%package -n apache-module-php5
Group: Internet/Web
Summary: PHP module for Apache 1.3.x
Requires: php5-common = %{version}-%{release} apache

%description -n apache-module-php5
PHP module for Apache


%prep
%setup -q -n php-%{version}
%patch0 -p1
%setup -q -D -T -b 1 -n php-%{version}
mv ../imap-2004g ./

%build

# start build c-client

cd imap-2004g
gmake soc 
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
LDFLAGS="-L/usr/local/lib -R/usr/local/lib \
    -L%{mysql_prefix}/lib/mysql -R%{mysql_prefix}/lib/mysql"
LD_RUN_PATH="/usr/local/lib:%{mysql_prefix}/lib/mysql"
LD_LIBRARY_PATH="/usr/local/lib"
CPPFLAGS="-I/usr/local/include"

export SSL_BASE EAPI_MM LDFLAGS CPPFLAGS LIBS LD_RUN_PATH LD_LIBRARY_PATH

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/mysql-%{mysql_ver}/bin:$PATH"
export PATH
hash -r

### ridiculous
which mysql_config

#no reentrant ldap
#reentrant ldap library please
#sed s/-lldap\ /-lldap_r\ /g configure > configure.ldapr
#mv configure configure~
#mv configure.ldapr configure
#chmod a+x configure

MAINFLAGS="--prefix=%{php_prefix} --enable-track-vars \
  --enable-force-cgi-redirect --with-gettext --with-ndbm --enable-ftp \
  --with-mysql=/%{mysql_prefix} --with-mssql --with-mysqli \
  --with-openssl=/usr/local/ssl --with-imap=imap-2004g/c-client \
  --enable-shared --enable-sysvshm --enable-sysvsem --with-gd \
  --with-ldap=/usr/local --with-bz2 --with-zlib \
  --with-config-file-path=/usr/local/etc --with-mcrypt=/usr/local \
  --with-freetype-dir=/usr/local --with-xmlrpc --with-curl --with-pspell"

%ifos solaris2.9
EXTRAFLAGS="--with-png-dir=/usr/local --with-jpeg-dir=/usr/local"
%else
EXTRAFLAGS=""
%endif

export MAINFLAGS EXTRAFLAGS

# Apparently you can't build the Apache 1 and 2 modules at the same time.
# -mt is both a linker and and a preprocessor flag. feel the love.

EXTRA_LIBS='-lrt' CC="/opt/SUNWspro/bin/cc" CFLAGS='-mt -g -xs' ./configure $MAINFLAGS $EXTRAFLAGS --with-apxs=%{apache_prefix}/bin/apxs

# I'm not happy about this at all. /usr/local/bin/mcrypt-config is sane but
# apparently PHP5 doesn't look there. So -lltdl from aclocal/mcrypt.m4 gets
# in WRONGLY. I don't see anything to fix in libmcrypt package, so:
sed s/-lltdl//g Makefile > Makefile.new
mv Makefile.new Makefile
gmake -j3
mv .libs/libphp5.so apache13-libphp5.so

EXTRA_LIBS='-lrt' CC="/opt/SUNWspro/bin/cc" CFLAGS='-g -xs' CPPFLAGS="$CPPFLAGS -I%{apache2_prefix}/include" ./configure $MAINFLAGS $EXTRAFLAGS --with-apxs2=%{apache2_prefix}/bin/apxs
# See above.
sed s/-lltdl//g Makefile > Makefile.new
mv Makefile.new Makefile
gmake -j3
mv .libs/libphp5.so apache2-libphp5.so

# I have no idea why pear is done separately. Does it need to be?
# I don't feel like investigating right now.
rm config.cache
EXTRA_LIBS='-lrt' CC="/opt/SUNWspro/bin/cc" CFLAGS='-g -xs' ./configure $MAINFLAGS $EXTRAFLAGS --with-pear=/usr/local/lib/php

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/local/apache-modules
mkdir -p %{buildroot}/usr/local/apache2-modules
mkdir -p %{buildroot}/usr/local/php-%{version}/lib
mkdir -p %{buildroot}/usr/local/php-%{version}/lib/php/build
mkdir -p %{buildroot}/usr/local/php-%{version}/bin
mkdir -p %{buildroot}/usr/local/etc

install -m 0755 apache13-libphp5.so %{buildroot}/usr/local/apache-modules/libphp5.so
install -m 0755 apache2-libphp5.so %{buildroot}/usr/local/apache2-modules/libphp5.so

install -m 0644 php.ini-dist %{buildroot}/usr/local/php-%{version}/lib/
install -m 0644 php.ini-recommended %{buildroot}/usr/local/php-%{version}/lib/
ln -sf php.ini-recommended %{buildroot}/usr/local/php-%{version}/lib/php.ini

install -m 0755 sapi/cli/php %{buildroot}/usr/local/php-%{version}/bin/

# install-modules fails with 4.3.6, modules directory is there but empty
#make install-pear install-headers install-build install-programs install-modules INSTALL_ROOT=%{buildroot} 

gmake install-pear install-headers install-build install-programs INSTALL_ROOT=%{buildroot} 



%post
cat<<EOF

PHP will now look in /usr/local/etc for the php.ini file.

This is different from previous package releases where the file was to
be located in the /usr/local/php-ver/lib directory.

EOF

%post -n apache2-module-php5
#if [ ! -r /usr/local/php ]; then
#	ln -s /usr/local/php-%{version} /usr/local/php
#	echo /usr/local/php now points to /usr/local/php-%{version}
#fi
cat <<EOF
From http://us3.php.net/manual/en/install.unix.apache2.php:

We do not recommend using a threaded MPM in production with Apache2.
Use the prefork MPM instead, or use Apache1.

TO COMPLETE THE INSTALLATION: put these lines in your httpd.conf:
     LoadModule php5_module ../apache2-modules/libphp5.so
     AddType application/x-httpd-php .php

EOF

%post -n apache-module-php5
cat <<EOF

TO COMPLETE THE INSTALLATION: put these lines in your httpd.conf:
     LoadModule php5_module ../apache-modules/libphp5.so
     AddType application/x-httpd-php .php
     AddModule mod_php5.c
EOF


%clean
rm -rf %{buildroot}

%files 
#main package is empty

%files common
%defattr(-, root, other)
%doc TODO CODING_STANDARDS CREDITS LICENSE
%config(noreplace)/usr/local/php-%{version}/lib/php.ini
%config(noreplace)/usr/local/php-%{version}/lib/php.ini-dist
%config(noreplace)/usr/local/php-%{version}/lib/php.ini-recommended
/usr/local/lib/php
%config(noreplace)/usr/local/php-%{version}/etc/pear.conf
/usr/local/php-%{version}/.channels/.alias/pear.txt
/usr/local/php-%{version}/.channels/.alias/pecl.txt
/usr/local/php-%{version}/.channels/__uri.reg
/usr/local/php-%{version}/.channels/pear.php.net.reg
/usr/local/php-%{version}/.channels/pecl.php.net.reg
/usr/local/php-%{version}/.depdb
/usr/local/php-%{version}/.depdblock
/usr/local/php-%{version}/.filemap
/usr/local/php-%{version}/.lock


%files devel
%defattr(-, root, other)
/usr/local/php-%{version}/include
# Huh? this is globbed by bin/*
#/usr/local/php-%{version}/bin/pear
/usr/local/php-%{version}/lib/php/build/*
/usr/local/php-%{version}/bin/*
/usr/local/php-%{version}/man/*

%files -n apache2-module-php5
%defattr(-, root, other)
/usr/local/apache2-modules/libphp5.so

%files -n apache-module-php5
%defattr(-, root, other)
/usr/local/apache-modules/libphp5.so


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
