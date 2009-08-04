Summary: PEAR: Database Abstraction Layer
Name: pear-DB
Version: 1.7.13
Release: 2 
License: PHP License
Group: Development/Libraries
Source: DB-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}


%description
DB is a database abstraction layer providing:
* an OO-style query API
* portability features that make programs written for one DBMS work with
  other DBMS's
* a DSN (data source name) format for specifying database servers
* prepare/execute (bind) emulation for databases that don't support it natively
* a result object for each query response
* portable error codes
* sequence emulation
* sequential and non-sequential row fetching as well as bulk fetching
* formats fetched rows as associative arrays, ordered arrays or objects
* row limit support
* transactions support
* table information interface
* DocBook and phpDocumentor API documentation

DB layers itself on top of PHP's existing
database extensions.

Drivers for the following extensions pass
the complete test suite and provide
interchangeability when all of DB's
portability options are enabled:

  fbsql, ibase, informix, msql, mssql,
  mysql, mysqli, oci8, odbc, pgsql,
  sqlite and sybase.

There is also a driver for the dbase
extension, but it can't be used
interchangeably because dbase doesn't
support many standard DBMS features.

DB is compatible with both PHP 4 and PHP 5.

%prep
%setup -q -n DB-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp DB.php %{buildroot}/usr/local/lib/php
cp -r DB %{buildroot}/usr/local/lib/php

%files
    %defattr(-,root,bin)
    %doc  doc/IDEAS doc/MAINTAINERS doc/STATUS doc/TESTERS
    %dir /usr/local/lib/php/DB
    /usr/local/lib/php/DB.php
    /usr/local/lib/php/DB/*

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.7.13-1
- Fixed php requires.
