%include perl-header.spec

Summary: Perl module for DES encryption
Name: perl-module-Crypt-DES
Version: 2.05
Release: 1
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS 

perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/Crypt/*
%{site_perl_arch}/auto/Crypt/DES/*
%{site_perl_arch}/auto/Crypt/DES/.packlist
%{perl_prefix}/man/*/*

%changelog
* Thu Jun 26 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.05-1
- Added changelog and updated to version 2.05
