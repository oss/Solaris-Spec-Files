%define mysql_ver  3.23.58
%define mysql5_ver 5.0.45
%define apache_ver 1.3.39
%define php_ver    4.4.8
%define apache2_ver 2.2.6

%define mysql_prefix  /usr/local/mysql-%{mysql_ver}
%define mysql5_prefix  /usr/local/mysql5
%define apache_prefix /usr/local/apache-%{apache_ver}
%define apache2_prefix /usr/local/apache2-%{apache2_ver}
%define php_prefix    /usr/local

Summary: The PHP scripting language
Name: php
Version: %{php_ver}
Release: 1
License: PHP License
Group: Development/Languages
Source0: php-%{php_ver}.tar.bz2
#Source1: php_c-client-4.1.1.tar.gz
Source1: imap-2004g.tar.Z
Patch: php-4.1.1.patch
Patch1: mail_log.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: php-common = %{version}-%{release} apache2-module-php = %{version}-%{release} apache-module-php = %{version}-%{release}
BuildRequires: patch freetype2-devel make libmcrypt freetype2 gdbm openldap >= 2.3 openldap-devel >= 2.3 libpng3-devel >= 1.2.8 libjpeg >= 6b-11
BuildRequires: openssl >= 0.9.8e
BuildRequires: apache apache-devel = %{apache_ver} apache2 apache2-devel = %{apache2_ver} curl freetds-devel freetds-lib postfix-tls


%description
PHP is a popular scripting language used for CGI programming.
It is available as an Apache module as well as a standalone executable.


%package common
Group: Development/Languages
Summary: configuration files for php
Requires: libtool mm openssl >= 0.9.8e gdbm openldap >= 2.3 gd libmcrypt freetype2 openldap-lib >= 2.3 curl expat freetds-lib libiconv >= 1.9.2 aspell >= 0.6.4
Conflicts: php5-common
%description common
PHP Configuration Files

%package mysql
Group:Development/Languages
Summary: mysql DSO for PHP 
Requires: mysql >= %{mysql_ver} php-common = %{version}-%{release}  
BuildRequires: mysql-devel >= %{mysql_ver} mysql 
%description mysql
The MySQL shared library for MySQL version 3

%package mysql5
Group:Development/Languages
Summary: mysql DSO for PHP 
Requires: mysql5-common >= %{mysql5_ver} php-common = %{version}-%{release} 
BuildRequires: mysql5-devel >= %{mysql5_ver} 
%description mysql5
The MySQL shared library for MySQL version 5.0

%package devel
Group: Development/Headers
Summary: includes for php
Requires: php-common = %{version}-%{release}
Conflicts: php-bin
Obsoletes: php-bin
%description devel
The devel package includes everything you need to actually use PHP. Install
this if you care to use PHP for more than blindly running code on your web
server.

%package -n apache2-module-php
Group: Internet/Web
Summary: PHP module for Apache 2
Requires: php-common = %{version}-%{release} apache2

%description -n apache2-module-php
PHP module for Apache 2


%package -n apache-module-php
Group: Internet/Web
Summary: PHP module for Apache 1.3.x
Requires: php-common = %{version}-%{release} apache

%description -n apache-module-php
PHP module for Apache


%prep
%setup -q
%patch -p1
%patch1 -p1
%setup -q -D -T -b 1
mv ../imap-2004g ./


%build

if [ ! -x /usr/lib/sendmail ];then
  echo "/usr/lib/sendmail must exist. Symlink to postfix's sendmail, perhaps?"
  exit 1
fi

#clean the buildroot
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot};

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

#save the c-client, we are going to need it after make clean
mkdir -p %{buildroot}
/usr/local/bin/tar cvf %{buildroot}/imap.tar imap-2004g


# we are currently using multiple db's in php. openldap uses db4
# watch new releases of php for db4 support and try switching over
# when available.

SSL_BASE="/usr/local/ssl"
EAPI_MM="/usr/local"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_prefix}/lib/mysql \
    -R%{mysql_prefix}/lib/mysql -liconv"
LD_RUN_PATH="/usr/local/lib:%{mysql_prefix}/lib/mysql"
LD_LIBRARY_PATH="/usr/local/lib"

export SSL_BASE EAPI_MM LDFLAGS CPPFLAGS LD_RUN_PATH LD_LIBRARY_PATH

MAINFLAGS="--prefix=%{php_prefix} --enable-track-vars \
 --enable-force-cgi-redirect --without-gettext --disable-nls --with-ndbm --enable-ftp \
 --with-mssql --with-openssl=/usr/local/ssl --with-imap=imap-2004g/c-client \
 --enable-shared --enable-sysvshm --enable-sysvsem --with-gd \
 --with-ldap=/usr/local --with-bz2 --with-zlib \
 --with-config-file-path=/usr/local/etc --with-mcrypt=/usr/local \
 --with-freetype-dir=/usr/local --with-xmlrpc --with-curl --with-pspell \
 --with-config-file-scan-dir=/usr/local/etc/php.d "

MYSQLFLAG="--with-mysql=shared,%{mysql_prefix}"
MYSQL5FLAG="--with-mysql=shared,%{mysql5_prefix}"

%ifos solaris2.9
EXTRAFLAGS="--with-png-dir=/usr/local --with-jpeg-dir=/usr/local"
%else
EXTRAFLAGS=""
%endif

export MAINFLAGS EXTRAFLAGS MYSQLFLAG MYSQL5FLAG

# Apparently you can't build the Apache 1 and 2 modules at the same time.
# We sneak in building a mysql 3 and a mysql 5 module with each apache 
# version respectively, hopefully md5 checksums don't lie


CC="gcc" ./configure $MAINFLAGS $MYSQLFLAG $EXTRAFLAGS --with-apxs=%{apache_prefix}/bin/apxs
make
mv .libs/libphp4.so %{buildroot}/apache13-libphp4.so
mv ./modules/mysql.so %{buildroot}/mysql.so

make clean

/usr/local/bin/tar xf %{buildroot}/imap.tar 
rm %{buildroot}/imap.tar 

#set ldflags to build against mysql5 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib \
         -L%{mysql5_prefix}/lib/mysql -R%{mysql5_prefix}/lib/mysql -liconv"
LD_RUN_PATH="/usr/local/lib:%{mysql5_prefix}/lib/mysql"
export LDFLAGS LD_RUN_PATH

CC="gcc" CPPFLAGS="$CPPFLAGS -I%{apache2_prefix}/include" ./configure $MAINFLAGS $MYSQL5FLAG $EXTRAFLAGS --with-apxs2=%{apache2_prefix}/bin/apxs
make
mv .libs/libphp4.so %{buildroot}/apache2-libphp4.so
mv ./modules/mysql.so %{buildroot}/mysql5.so

rm config.cache 
#build peary goodness
./configure $MAINFLAGS $EXTRAFLAGS --with-pear=/usr/local/lib/php

%install

mkdir -p %{buildroot}/usr/local/apache-modules
mkdir -p %{buildroot}/usr/local/apache2-modules
mkdir -p %{buildroot}/usr/local/lib
mkdir -p %{buildroot}/usr/local/lib/php/build
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/etc/php.d
mkdir -p %{buildroot}/usr/local/lib/php/modules

mv php.ini-recommended php.ini-recommended.old 
sed -e 's/extension_dir = ".\/"/extension_dir = "\/usr\/local\/lib\/php\/modules"/' php.ini-recommended.old > php.ini-recommended

install -m 0755 %{buildroot}/apache13-libphp4.so %{buildroot}/usr/local/apache-modules/libphp4.so

install -m 0755 %{buildroot}/apache2-libphp4.so %{buildroot}/usr/local/apache2-modules/libphp4.so

install -m 0755 %{buildroot}/mysql.so  %{buildroot}/usr/local/lib/php/modules/mysql.so
install -m 0755 %{buildroot}/mysql5.so  %{buildroot}/usr/local/lib/php/modules/mysql5.so

install -m 0644 php.ini-dist %{buildroot}/usr/local/etc/
install -m 0644 php.ini-recommended %{buildroot}/usr/local/etc/
ln -sf php.ini-recommended %{buildroot}/usr/local/etc/php.ini

install -m 0755 sapi/cli/php %{buildroot}/usr/local/bin/
rm %{buildroot}/mysql5.so %{buildroot}/mysql.so %{buildroot}/apache13-libphp4.so %{buildroot}/apache2-libphp4.so

# install-modules fails with 4.3.6, modules directory is there but empty
#make install-pear install-headers install-build install-programs install-modules INSTALL_ROOT=%{buildroot} 

make install-pear install-headers install-build install-programs INSTALL_ROOT=%{buildroot} 



cat > %{buildroot}/usr/local/etc/php.d/mysql.ini <<EOF
; Uncomment the mysql extension module you wish to enable
;extension=mysql.so
EOF

cat > %{buildroot}/usr/local/etc/php.d/mysql5.ini <<EOF
; Uncomment the mysql extension module you wish to enable
;extension=mysql5.so
EOF

%post
cat<<EOF

PHP will now look in /usr/local/etc for the php.ini file.

This is different from previous package releases where the file was to
be located in the /usr/local/php-ver/lib directory.

If you plan to use PHP with a MySQL database you should install php-mysql for 
MySQL version 3 functionality or php-mysql5 for MySQL version 5 functionality. 

EOF

%post -n apache2-module-php
cat <<EOF
From http://us3.php.net/manual/en/install.unix.apache2.php:

We do not recommend using a threaded MPM in production with Apache2.
Use the prefork MPM instead, or use Apache1.

TO COMPLETE THE INSTALLATION: put these lines in your httpd.conf:
     LoadModule php4_module ../apache2-modules/libphp4.so
     AddType application/x-httpd-php .php

EOF

%post -n apache-module-php
cat <<EOF

TO COMPLETE THE INSTALLATION: put these lines in your httpd.conf:
     LoadModule php4_module ../apache-modules/libphp4.so
     AddType application/x-httpd-php .php
     AddModule mod_php4.c
EOF

%post mysql
cat <<EOF

TO COMPLETE THE INSTALLATION: Make sure php.ini contains
extension_dir = "/usr/local/lib/php/modules" 

AND Uncomment or add this line to /usr/local/etc/php.d/mysql.ini
extension=mysql.so

EOF

%post mysql5
cat <<EOF

TO COMPLETE THE INSTALLATION: Make sure php.ini contains
extension_dir = "/usr/local/lib/php/modules" 

AND Uncomment or add this line to /usr/local/etc/php.d/mysql5.ini
extension=mysql5.so

EOF


%clean
rm -rf %{buildroot}

%files 
#main package is empty

%files common
%defattr(-, root, other)
%doc TODO CODING_STANDARDS CREDITS LICENSE
%config(noreplace)/usr/local/etc/php.ini
%config(noreplace)/usr/local/etc/php.ini-dist
%config(noreplace)/usr/local/etc/php.ini-recommended
%dir /usr/local/lib/php
/usr/local/lib/php/.channels
/usr/local/lib/php/.depdb
/usr/local/lib/php/.depdblock
/usr/local/lib/php/.filemap
/usr/local/lib/php/.lock
/usr/local/lib/php/.registry
/usr/local/lib/php/Archive
/usr/local/lib/php/Console
/usr/local/lib/php/data
/usr/local/lib/php/doc
/usr/local/lib/php/HTML
/usr/local/lib/php/Net
/usr/local/lib/php/OS
/usr/local/lib/php/PEAR
/usr/local/lib/php/pearcmd.php
/usr/local/lib/php/peclcmd.php
/usr/local/lib/php/System.php
/usr/local/lib/php/test/HTML_Template_IT
/usr/local/lib/php/PEAR.php
/usr/local/lib/php/Structures/Graph.php                                      
/usr/local/lib/php/Structures/Graph/Manipulator/AcyclicTest.php              
/usr/local/lib/php/Structures/Graph/Manipulator/TopologicalSorter.php        
/usr/local/lib/php/Structures/Graph/Node.php                                 
/usr/local/lib/php/test/Structures_Graph/tests/README                        
/usr/local/lib/php/test/Structures_Graph/tests/all-tests.php                 
/usr/local/lib/php/test/Structures_Graph/tests/testCase/BasicGraph.php
%dir /usr/local/lib/php/modules/
%config(noreplace)/usr/local/etc/pear.conf

%files devel
%defattr(-, root, other)
/usr/local/include/php/
/usr/local/lib/php/build
/usr/local/bin/*
/usr/local/man/*

%files -n apache2-module-php
%defattr(-, root, other)
/usr/local/apache2-modules/libphp4.so

%files -n apache-module-php
%defattr(-, root, other)
/usr/local/apache-modules/libphp4.so

%files mysql
%defattr(-, root, other)
%config(noreplace)/usr/local/etc/php.d/mysql.ini
/usr/local/lib/php/modules/mysql.so

%files mysql5
%defattr(-, root, other)
%config(noreplace)/usr/local/etc/php.d/mysql5.ini
/usr/local/lib/php/modules/mysql5.so


%changelog
* Fri Jan 4 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 4.4.8-1
- Updated to 4.4.8.

* Sun Nov 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.4.7-6
- Attempting without-gettext

* Sun Nov 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.4.7-5
- Respun against gettext 0.17

* Thu Aug 9 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu>
- Added mail_log.patch

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
