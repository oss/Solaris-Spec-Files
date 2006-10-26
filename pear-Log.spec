Summary: PEAR: Logging utilities
Name: pear-Log
Version: 1.9.9
Release: 1
License: PHP License
Group: Development/Libraries
Source: Log-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php-common


%description
The Log framework provides an abstracted logging system. It supports logging
to console, file, syslog, SQL, Sqlite, mail, and mcal targets. It also
provides a subject - observer mechanism.

%prep
%setup -q -n Log-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php
mkdir -p %{buildroot}/usr/local/lib/php/data/Log
mkdir -p %{buildroot}/usr/local/lib/php/doc/Log
mkdir -p %{buildroot}/usr/local/lib/php/test/Log

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp Log.php %{buildroot}/usr/local/lib/php
cp -r Log %{buildroot}/usr/local/lib/php
cp -r docs %{buildroot}/usr/local/lib/php/doc/Log
cp -r tests %{buildroot}/usr/local/lib/php/test/Log
cp -r misc %{buildroot}/usr/local/lib/php/data/Log

%files
%defattr(-,root,bin)
     /usr/local/lib/php/Log.php
%dir /usr/local/lib/php/Log
     /usr/local/lib/php/Log/*
%dir /usr/local/lib/php/data/Log
     /usr/local/lib/php/data/Log/*
%dir /usr/local/lib/php/doc/Log
     /usr/local/lib/php/doc/Log/*
%dir /usr/local/lib/php/test/Log
     /usr/local/lib/php/test/Log/*

