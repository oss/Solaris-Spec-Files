%include perl-header.spec

Summary: Crypt-OpenSSL-RSA
Name: perl-module-Crypt-OpenSSL-RSA
Version: 0.24
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Crypt-OpenSSL-RSA-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Crypt-OpenSSL-Random
BuildRequires: perl = %{perl_version} perl-module-Crypt-OpenSSL-Random

%description
This perl module implements Crypt-OpenSSL-RSA

%prep
%setup -q -n Crypt-OpenSSL-RSA-%{version}

%build
%{perl_binary} Makefile.PL INC="-I/usr/local/ssl/include" LIBS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -lssl -lcrypto"
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
