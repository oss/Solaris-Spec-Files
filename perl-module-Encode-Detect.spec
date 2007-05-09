%include perl-header.spec

Summary: Encode-Detect
Name: perl-module-Encode-Detect
Version: 1.00
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Encode-Detect-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-ExtUtils-CBuilder
BuildRequires: perl = %{perl_version} perl-module-ExtUtils-CBuilder

%description
This perl module implements Encode-Detect

%prep
%setup -q -n Encode-Detect-%{version}

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
