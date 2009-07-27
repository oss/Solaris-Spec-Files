Summary: PEAR: Provides an implementation of the SMTP protocol
Name: pear-Net_SMTP
Version: 1.3.3
Release: 1
License: PHP License
Group: Development/Libraries
Source: Net_SMTP-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}
Requires: php pear-Net_Socket pear-Auth_SASL


%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

%prep
%setup -n Net_SMTP-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Net
mkdir -p %{buildroot}/usr/local/lib/php/doc/Net_SMTP
mkdir -p %{buildroot}/usr/local/lib/php/test/Net_SMTP

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp SMTP.php %{buildroot}/usr/local/lib/php/Net
cp -r docs/ %{buildroot}/usr/local/lib/php/doc/Net_SMTP
cp -r tests/ %{buildroot}/usr/local/lib/php/test/Net_SMTP

%files
%defattr(-,root,bin)
%dir /usr/local/lib/php/doc/Net_SMTP
%dir /usr/local/lib/php/test/Net_SMTP
/usr/local/lib/php/Net/SMTP.php
/usr/local/lib/php/doc/Net_SMTP/*
/usr/local/lib/php/test/Net_SMTP/*
%doc

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.3.3-1
- Fixed php requires.

