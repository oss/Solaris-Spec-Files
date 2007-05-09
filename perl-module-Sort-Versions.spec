%include perl-header.spec

Summary: Sort-Versions
Name: perl-module-Sort-Versions
Version: 1.5
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Sort-Versions-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Sort-Versions

%prep
%setup -q -n Sort-Versions-%{version}

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
%{site_perl}/Sort
