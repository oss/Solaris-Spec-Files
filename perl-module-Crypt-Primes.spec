%include perl-header.spec

Summary: Crypt-Primes
Name: perl-module-Crypt-Primes
Version: 0.50
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Crypt-Primes-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Crypt-Random
BuildRequires: perl = %{perl_version} perl-module-Crypt-Random

%description
This perl module implements Crypt-Primes

%prep
%setup -q -n Crypt-Primes-%{version}

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
%{perl_prefix}/man/*
%{site_perl_arch}
%{site_perl}/Crypt
/usr/perl5/bin/largeprimes
