%include perl-header.spec

Summary: Crypt-OpenSSL-Random
Name: perl-module-Crypt-OpenSSL-Random
Version: 0.03
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Crypt-OpenSSL-Random-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Crypt-OpenSSL-Random

%prep
%setup -q -n Crypt-OpenSSL-Random-%{version}

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
