%include perl-header.spec

Summary: Perl module for sorting lines with delimited fields
Name: perl-module-Sort-Fields
Version: 0.90
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Sort-Fields-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Sort::Fields provides a general purpose technique for efficiently
sorting lists of lines that contain data separated into fields.

%prep
%setup -q -n Sort-Fields-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/auto/Sort/Fields
%{site_perl}/Sort/*
%{perl_prefix}/man/man3/*
