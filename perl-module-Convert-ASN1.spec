%include perl-header.spec

Summary: Convert ASN1 perl module
Name: perl-module-Convert-ASN1
Version: 0.18
Release: 1
Group: System Environment/Base
License: Perl (Artistic and GPL)
Source: Convert-ASN1-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-Test-Simple
BuildRequires: perl = %{perl_version}, perl-module-Test-Simple

%description
ASN.1 Encode/Decode library

%prep

%setup -n Convert-ASN1-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefi}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%doc README Changes
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/man/man3/*
