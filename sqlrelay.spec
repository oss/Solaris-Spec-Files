%define sqlrelayver 0.36.4
%define phpver 4.4.0
%define mysqlver 4.1.13
%define pythonver 2.3

%define sqlrelayprefix /usr/local/sqlrelay-%{sqlrelayver}
%define phpdir /usr/local/php-%{phpver} 
%define mysqldir /usr/local/mysql-%{mysqlver} 

%define phpextdir %(echo "`%{phpdir}/bin/php-config --extension-dir`")
%define	phppeardbdir %(echo "`%{phpdir}/bin/php-config --prefix`/share/pear/DB")
%define	perl_prefix %(eval `perl -V:prefix`; echo $prefix)
%define	perl_sitelib %(eval `perl -V:sitelib`;  echo $sitelib)
%define	perl_installarchlib %(eval `perl -V:installarchlib`; echo $installarchlib)
%define	perl_installsitearch %(eval `perl -V:installsitearch`; echo $installsitearch)
%define	perl_sitearch %(eval `perl -V:sitearch`; echo $sitearch)
%define	perl_installman3dir %(eval `perl -V:installman3dir`;  echo $installman3dir)
%define	perl_man3ext %(eval `perl -V:man3ext`; echo $man3ext)
%define pythondir /usr/local/lib/python%{pythonver}        

Name: sqlrelay
Version: %{sqlrelayver}  
Release: 2
Summary: Persistent database connection system.
License: GPL/LGPL and Others
Group: System Environment/Daemons
Source0: %{name}-%{version}.tar.gz
URL: http://sqlrelay.sourceforge.net
Buildroot: %{_tmppath}/%{name}-root
Requires: readline >= 4.1
BuildRequires: rudiments-devel >= 0.28.1 mysql4-devel = %{mysqlver} php-bin = %{phpver} php-devel = %{phpver} php-common = %{phpver} python => %{pythonver}

%description
SQL Relay is a persistent database connection pooling, proxying and load 
balancing system for Unix and Linux supporting ODBC, Oracle, MySQL, mSQL, 
PostgreSQL, Sybase, MS SQL Server, IBM DB2, Interbase, Lago and SQLite with C, 
C++, Perl, Perl-DBD, Python, Python-DB, Zope, PHP, Ruby, Java and TCL APIs,
command line clients, a GUI configuration tool and extensive documentation.
The APIs support advanced database operations such as bind variables, multi-row
fetches, client side result set caching and suspended transactions.  It is
ideal for speeding up database-driven web-based applications, accessing
databases from unsupported platforms, migrating between databases, distributing
access to replicated databases and throttling database access.


%package devel
Summary: Development libraries for SQL Relay.
Group: Applications/Libraries
%description devel
Static libraries for SQL Relay.


%package clients
Summary: Command line applications for accessing databases through SQL Relay.
Group: Applications/Database
%description clients
Command line applications for accessing databases through SQL Relay.


%package client-runtime
Summary: Runtime libraries for SQL Relay clients.
Group: Applications/Libraries
%description client-runtime
Runtime dependencies for SQL Relay clients

%package client-devel
Summary: Development files for developing programs in C/C++ that use SQL Relay.
Group: Development/Libraries
%description client-devel
Header files and static libraries to use for developing programs in C/C++ that
use SQL Relay.  


%package client-mysql
Summary: Drop in replacement library allowing MySQL clients to use SQL Relay instead.
Group: Applications/Libraries
%description client-mysql
Drop in replacement library allowing MySQL clients to use SQL Relay instead.

%package mysql
Summary: SQL Relay connection daemon for MySQL.
Group: Applications/Databases
%description mysql
SQL Relay connection daemon for MySQL.

%package perl
Summary: SQL Relay modules for Perl.
Group: Development/Languages
%description perl
SQL Relay modules for Perl.


%package php
Summary: SQL Relay modules for PHP.
Group: Development/Languages
Requires: php-bin >= %{phpver}
%description php
SQL Relay modules for PHP.

%package python
Summary: SQL Relay modules for Python.
Group: Development/Languages
Requires: python >= %{pythonver}
%description python
SQL Relay modules for Python.

%prep

%setup -q

%build
PATH="/usr/ccs/bin:%{mysqldir}/bin:%{phpdir}/bin:/usr/local/bin:/usr/local/gnu/bin:/usr/local/bin:$PATH"
export PATH

CC="gcc" 
export CC
CXX="g++" 
export CXX

LD_LIBRARY_PATH="/usr/local/lib" 
export LD_LIBRARY_PATH

LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L%{mysqldir}/lib/mysql -R%{mysqldir}/lib/mysql -L%{phpdir}/lib -R%{phpdir}/lib"  
export LD

%ifarch sparc64
LD_RUN_PATH="/usr/local/lib/sparcv9:%{mysqldir}/lib/mysql:%{phpdir}/lib/php/build"
export LD_RUN_PATH
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L%{phpdir}/lib -R%{phpdir}/lib -L%{mysqldir}/lib/mysql -R%{mysqldir}/lib/mysql -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" 
export LDFLAGS
%endif 

%ifarch sparc
LD_RUN_PATH="/usr/local/lib/:%{mysqldir}/lib/mysql:%{phpdir}/lib/php/build"
export LD_RUN_PATH
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L%{phpdir}/lib -R%{phpdir}/lib -L%{mysqldir}/lib/mysql -R%{mysqldir}/lib/mysql -L/usr/local/lib -R/usr/local/lib" 
export LDFLAGS
%endif 

./configure \
	--prefix='%{sqlrelayprefix}' \
	--disable-gtk \
        --disable-db2 \
        --disable-freetds \
        --disable-interbase \
        --disable-lago \
        --disable-mdbtools \
        --disable-msql \
        --disable-odbc \
        --disable-oracle \
        --disable-postgresql \
        --disable-sqlite \
        --disable-sybase \
        --disable-java \
        --disable-tcl \
        --disable-ruby \
        --disable-zope ;
        # --disable-python \
        # --disable-mysql \
        # --disable-php \
        # --disable-perl \
	
gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot} 


%post


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%config %attr(600, root, root) %{sqlrelayprefix}/etc/sqlrelay.conf.example
%config %attr(600, root, root) %{sqlrelayprefix}/etc/sqlrelay.dtd
%{sqlrelayprefix}/bin/sqlr-cachemanager*
%{sqlrelayprefix}/bin/sqlr-listener*
%{sqlrelayprefix}/bin/sqlr-scaler*
%{sqlrelayprefix}/bin/sqlr-start*
%{sqlrelayprefix}/bin/sqlr-stop
%{sqlrelayprefix}/lib/libsqlrconnection*
%{sqlrelayprefix}/lib/libpqsqlrelay-0.36.4.so.1.0.0
%{sqlrelayprefix}/lib/libsqlrutil*
%{sqlrelayprefix}/var/sqlrelay/tmp
%{sqlrelayprefix}/var/sqlrelay/debug
%{sqlrelayprefix}/share
%{sqlrelayprefix}/man

%files devel
%defattr(-, root, root)
%{sqlrelayprefix}/lib/libpqsqlrelay.a
%{sqlrelayprefix}/lib/libpqsqlrelay.la

%files clients
%defattr(-, root, root)
%{sqlrelayprefix}/bin/backupschema
%{sqlrelayprefix}/bin/fields
%{sqlrelayprefix}/bin/query
%{sqlrelayprefix}/bin/sqlrsh

%files client-runtime
%defattr(-, root, root)
%{sqlrelayprefix}/lib/libsqlrclient-*.so.*
%{sqlrelayprefix}/var/sqlrelay/cache
%{sqlrelayprefix}/lib/libsqlrclientwrapper-*.so.*

%files client-devel
%defattr(-, root, root)
%{sqlrelayprefix}/bin/sqlrclient-config
%{sqlrelayprefix}/include/sqlrelay/sqlrclient.h
%{sqlrelayprefix}/include/sqlrelay/private
%{sqlrelayprefix}/lib/libsqlrclient.a
%{sqlrelayprefix}/lib/libsqlrclient.la
%{sqlrelayprefix}/lib/libsqlrclient.so
%{sqlrelayprefix}/lib/pkgconfig/sqlrelay-c++.pc
%{sqlrelayprefix}/bin/sqlrclientwrapper-config
%{sqlrelayprefix}/include/sqlrelay/sqlrclientwrapper.h
%{sqlrelayprefix}/lib/libsqlrclientwrapper.a
%{sqlrelayprefix}/lib/libsqlrclientwrapper.la
%{sqlrelayprefix}/lib/libsqlrclientwrapper.so
%{sqlrelayprefix}/lib/pkgconfig/sqlrelay-c.pc

%files client-mysql
%defattr(-, root, root)
%{sqlrelayprefix}/lib/libmysql*sqlrelay-*.so.*
%{sqlrelayprefix}/lib/libmysql*sqlrelay.so
%{sqlrelayprefix}/lib/libmysql*sqlrelay.a
%{sqlrelayprefix}/lib/libmysql*sqlrelay.la

%files mysql
%defattr(-, root, root)
%{sqlrelayprefix}/bin/sqlr-connection-mysql*

%files perl
%defattr(-, root, root)
%{perl_sitelib}/DBD/SQLRelay.pm
%{perl_sitearch}/auto/DBD/SQLRelay
%{perl_sitearch}/SQLRelay/Connection.pm
%{perl_sitearch}/SQLRelay/Cursor.pm
%{perl_sitearch}/auto/SQLRelay/Connection
%{perl_sitearch}/auto/SQLRelay/Cursor
# %{perl_installman3dir}/*.%{perl_man3ext}*

%files php
%defattr(-, root, root)
%{phpextdir}/sql_relay.so
%{phppeardbdir}/sqlrelay.php

%files python
%defattr(-, root, root)
%{pythondir}/site-packages/SQLRelay

%changelog
* Fri Aug 19 2005 John M. Santel <jmsl@ncbs.rutgers.edu>
- added requirement for gnu readline package
* Mon Aug 15 2005 John M. Santel <jmsl@ncbs.rutgers.edu>
- First RU version
- Made %define statements that call shell commands compatible with sh
- built against php, perl, and mysql and python.

