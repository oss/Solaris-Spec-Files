%include perl-header.spec

Summary: The Params::Validate module provides a flexible system for validation method/function call parameters.

Name: perl-module-Params-Validate
Version: 0.58
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Params-Validate-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.  The validation can be as simple as
checking for the presence of required parameters or as complex as
validating object classes (via isa) or capabilities (via can),
checking parameter types, and using customized callbacks to ensure
data integrity.

The module has been designed to work equally well with positional or
named parameters (as a hash or hash reference).

It includes both a fast XS implementation, and a slower pure Perl
implementation that it can fall back on.


%prep

%setup -q -n Params-Validate-%{version}

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
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
