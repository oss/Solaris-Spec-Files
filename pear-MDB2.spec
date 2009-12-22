Summary: PEAR: data abstraction layer
Name: pear-MDB2
Version: 2.4.1
Release: 1
License: PHP License
Group: Development/Libraries
Source: MDB2-%{version}.tgz
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}

%description
PEAR MDB2 is a merge of the PEAR DB and Metabase php database abstraction layers.

It provides a common API for all supported RDBMS. The main difference to most
other DB abstraction packages is that MDB2 goes much further to ensure
portability. MDB2 provides most of its many features optionally that
can be used to construct portable SQL statements:
* Object-Oriented API
* A DSN (data source name) or array format for specifying database servers
* Datatype abstraction and on demand datatype conversion
* Various optional fetch modes to fix portability issues
* Portable error codes
* Sequential and non sequential row fetching as well as bulk fetching
* Ability to make buffered and unbuffered queries
* Ordered array and associative array for the fetched rows
* Prepare/execute (bind) named and unnamed placeholder emulation
* Sequence/autoincrement emulation
* Replace emulation
* Limited sub select emulation
* Row limit emulation
* Transactions/savepoint support
* Large Object support
* Index/Unique Key/Primary Key support
* Pattern matching abstraction
* Module framework to load advanced functionality on demand
* Ability to read the information schema
* RDBMS management methods (creating, dropping, altering)
* Reverse engineering schemas from an existing database
* SQL function call abstraction
* Full integration into the PEAR Framework
* PHPDoc API documentation

%prep
%setup -q -n MDB2-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/MDB2
mkdir -p %{buildroot}/usr/local/lib/php/doc/MDB2

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp MDB2.php %{buildroot}/usr/local/lib/php/MDB2
cp -r MDB2/ %{buildroot}/usr/local/lib/php/
cp -r docs/ %{buildroot}/usr/local/lib/php/doc/MDB2

%files
%defattr(-,root,bin)
%doc
%dir /usr/local/lib/php/MDB2/
%dir /usr/local/lib/php/doc/MDB2
/usr/local/lib/php/MDB2/*
/usr/local/lib/php/doc/MDB2/*

%changelog
* Tue Dec 22 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.4.1
- Initial Build.
