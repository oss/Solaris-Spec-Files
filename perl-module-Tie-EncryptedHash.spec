%include perl-header.spec

Summary: Tie-EncryptedHash
Name: perl-module-Tie-EncryptedHash
Version: 1.21
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Tie-EncryptedHash-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Tie-EncryptedHash

%prep
%setup -q -n Tie-EncryptedHash-%{version}

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
%{site_perl}/Tie
