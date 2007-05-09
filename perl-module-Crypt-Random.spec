%include perl-header.spec

Summary: Crypt-Random
Name: perl-module-Crypt-Random
Version: 1.25
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Crypt-Random-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Math-Pari
BuildRequires: perl = %{perl_version} perl-module-Math-Pari

%description
This perl module implements Crypt-Random

%prep
%setup -q -n Crypt-Random-%{version}

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
%{perl_prefix}/man/man3/*
%{site_perl_arch}
%{site_perl}/Crypt
/usr/perl5/bin/makerandom
