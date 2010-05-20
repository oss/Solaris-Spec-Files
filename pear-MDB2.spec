%define minor b2

Summary:   PEAR: data abstraction layer
Name:      pear-MDB2
Version:   2.5.0
Release:   0.1.%{minor}
License:   BSD
Group:     Development/Libraries
Source:    http://download.pear.php.net/package/MDB2-%{version}%{?minor}.tgz
Packager:  Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:       http://pear.php.net/package/MDB2/download
Requires:  pear-DB >= 1.4.0
Requires:  php >= 4.3.2

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
%setup -q -n MDB2-%{version}%{?minor}

%build

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/php/MDB2
mkdir -p %{buildroot}%{_libdir}/php/doc/MDB2
cp -p MDB2.php %{buildroot}%{_libdir}/php/MDB2
cp -pr MDB2/ %{buildroot}%{_libdir}/php/
cp -pr docs/ %{buildroot}%{_libdir}/php/doc/MDB2


%files
%defattr(-,root,bin,-)
%doc LICENSE
%doc %{_libdir}/php/doc/MDB2/
%{_libdir}/php/MDB2/


%changelog
* Fri Apr 30 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.5.0-0.1.b2
- Update to 2.5.0b2

* Tue Dec 22 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.4.1
- Initial Build.
