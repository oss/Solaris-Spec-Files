%include perl-header.spec

Summary: Params::Validate - Validate method/function parameters

Name: perl-module-Params-Validate
Version: 0.62
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Params-Validate-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

Requires: perl
BuildRequires: perl

Requires: perl-module-Attribute-Handlers >= 0.78-1
BuildRequires: perl-module-Attribute-Handlers >= 0.78-1

%if %{which_perl} == "SOLARIS"
Requires: perl-module-File-Spec >= 0.82-2
BuildRequires: perl-module-File-Spec >= 0.82-2

Requires: perl-module-ExtUtils-MakeMaker >= 6.05-1
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.05-1
%endif

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

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
rm -f $RPM_BUILD_ROOT/%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Changes
%{perl_prefix}/man/man3/*
%{site_perl}/Attribute/Params
%{site_perl}/Params
%{site_perl_arch}/auto/Params

