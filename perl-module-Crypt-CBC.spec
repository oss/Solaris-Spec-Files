%include perl-header.spec

Summary: Perl module for DES encryption
Name: perl-module-Crypt-CBC
Version: 2.29
Release: 1
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>
Group: System Environment/Base
Copyright: Systemics
Source: Crypt-CBC-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Crypt-DES perl-module-Digest-MD5
BuildRequires: perl = %{perl_version}

%description
This perl module implements the CBC encryption algorithm.

%prep
%setup -q -n Crypt-CBC-%{version}

%build
%{perl_binary} Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/../Crypt/*
%{site_perl_arch}/auto/Crypt/CBC
%{perl_prefix}/man/*/*

%changelog
* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.29-1
- Added changelog, updated to version 2.29
