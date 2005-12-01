Summary: PEAR: Abstraction of various SASL mechanism responses
Name: pear-DB
Version: 1.7.6
Release: 1
License: PHP/BSD
Group: Development/Libraries
Source: Auth_SASL-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php-common


%description
Provides code to generate responses to common SASL mechanisms, including:
o Digest-MD5
o CramMD5
o Plain
o Anonymous
o Login (Pseudo mechanism)

%prep
%setup -q -n Auth_SASL-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Auth

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp SASL.php %{buildroot}/usr/local/lib/php/Auth
cp -r SASL %{buildroot}/usr/local/lib/php/Auth

%files
    %defattr(-,root,bin)
    %dir /usr/local/lib/php/Auth/SASL
    /usr/local/lib/php/Auth/SASL.php
    /usr/local/lib/php/Auth/SASL/*

