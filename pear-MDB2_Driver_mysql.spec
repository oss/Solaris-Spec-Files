Summary: PEAR: MySQL MDB2 driver
Name: pear-MDB2_Driver_mysql
Version: 1.4.1
Release: 1
License: PHP License
Group: Development/Libraries
Source: MDB2_Driver_mysql-%{version}.tgz
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}

%description
The MySQL MDB2 driver.

%prep
%setup -q -n MDB2_Driver_mysql-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/MDB2

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp -r MDB2/ %{buildroot}/usr/local/lib/php/

%files
%defattr(-,root,bin)
%doc
%dir /usr/local/lib/php/MDB2/
/usr/local/lib/php/MDB2/*

%changelog
* Tue Dec 22 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.1
- Initial Build.
