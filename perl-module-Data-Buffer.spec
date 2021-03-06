%include perl-header.spec

Summary: Data-Buffer
Name: perl-module-Data-Buffer
Version: 0.04
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Data-Buffer-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Data-Buffer

%prep
%setup -q -n Data-Buffer-%{version}

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
%{site_perl}/Data
