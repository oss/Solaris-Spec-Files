%include perl-header.spec

Summary: Test::Simple Test::Builder and Test::More perl modules
Name: perl-module-Test-Simple
Version: 0.62
Release: 1
Group: System Environment/Base
License: Perl (Artistic and GPL)
Source: Test-Simple-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-ExtUtils-MakeMaker
BuildRequires: perl = %{perl_version}, perl-module-ExtUtils-MakeMaker

%description
Test writing utilities

%prep

%setup -n Test-Simple-%{version}

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
%defattr(-, bin, bin)
%doc README Changes
%{site_perl}/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
