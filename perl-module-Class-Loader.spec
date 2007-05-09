%include perl-header.spec

Summary: Class-Loader
Name: perl-module-Class-Loader
Version: 2.03
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Class-Loader-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Class-Loader

%prep
%setup -q -n Class-Loader-%{version}

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
%{site_perl}/Class/*
%{site_perl_arch}
