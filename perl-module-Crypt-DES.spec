%include perl-header.spec

Summary: Perl module for DES encryption
Name: perl-module-Crypt-DES
Version: 2.03
Release: 3
Group: System Environment/Base
Copyright: Systemics
Source: Crypt-DES-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements the DES encryption algorithm.

%prep
%setup -q -n Crypt-DES-%{version}

%build
%{perl_binary} Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/Crypt/*
%{site_perl_arch}/auto/Crypt/DES/*
%{perl_prefix}/man/*/*
