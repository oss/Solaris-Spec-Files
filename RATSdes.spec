%include perl-header.spec

Summary: RATS encryption module
Name: perl-module-RATSdes
Version: 0.0.1
Release: 1
Group: System Environment/Base
Copyright: Rutgers University
Source: RATSdes-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: openssl
BuildRequires: perl = %{perl_version}
BuildRequires: openssl

%description

%prep
%setup -q -n RATSdes

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/*/*
