Summary: PEAR: Validate various data
Name: pear-Validate
Version: 0.8.1
Release: 1
License: PHP/BSD
Group: Development/Libraries
Source: Validate-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php-common


%description
Package to validate various datas. It includes :
- numbers (min/max, decimal or not)
- email (syntax, domain check, rfc822)
- string (predifined type alpha upper and/or lowercase, numeric,...)
- date (min, max, rfc822 compliant)
- uri (RFC2396)
- possibility valid multiple data with a single method call (::multiple)

%prep
%setup -q -n Validate-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Validate

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp Validate.php %{buildroot}/usr/local/lib/php/Validate

%files
    %defattr(-,root,bin)
    /usr/local/lib/php/Validate/Validate.php
