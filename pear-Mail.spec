Summary: PEAR: Class that provides multiple interfaces for sending emails
Name: pear-Mail
Version: 1.1.9
Release: 1
License: PHP/BSD
Group: Development/Libraries
Source: Mail-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php-common pear-Net


%description
PEAR's Mail package defines an interface for implementing mailers under the PEAR hierarchy.  It also provides supporting functions useful to multiple mailer backends.	Currently supported backends include: PHP's native mail() function, sendmail, and SMTP.	 This package also provides a RFC822 email address list validation utility class.

%prep
%setup -q -n Mail-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/
mkdir -p %{buildroot}/usr/local/lib/php/test/Mail

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp Mail.php %{buildroot}/usr/local/lib/php/
cp -r Mail/ %{buildroot}/usr/local/lib/php/
cp -r test/ %{buildroot}/usr/local/lib/php/test/Mail

%files
%defattr(-,root,bin)
%dir /usr/local/lib/php/Mail
%dir /usr/local/lib/php/test/Mail
/usr/local/lib/php/Mail.php
/usr/local/lib/php/Mail/*
/usr/local/lib/php/test/Mail/*

