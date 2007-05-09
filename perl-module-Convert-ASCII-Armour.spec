%include perl-header.spec

Summary: Convert-ASCII-Armour
Name: perl-module-Convert-ASCII-Armour
Version: 1.4
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Convert-ASCII-Armour-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Convert-ASCII-Armour

%prep
%setup -q -n Convert-ASCII-Armour-%{version}

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
%{site_perl}/Convert
%{site_perl_arch}/auto/Convert/ASCII/Armour
