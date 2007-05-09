%include perl-header.spec

Summary: Math-Pari
Name: perl-module-Math-Pari
Version: 2.010709
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Math-Pari-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Math-Pari

%prep
%setup -q -n Math-Pari-%{version}

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
