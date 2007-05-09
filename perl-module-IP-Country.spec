%include perl-header.spec

Summary: IP-Country
Name: perl-module-IP-Country
Version: 2.23
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: IP-Country-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements IP-Country

%prep
%setup -q -n IP-Country-%{version}

%build
%{perl_binary} Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/perl5/bin/*
%{perl_prefix}/man/*
%{site_perl_arch}
%{site_perl}/IP
