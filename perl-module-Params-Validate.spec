%include perl-header.spec

Summary: Params::Validate - Validate method/function parameters

Name: perl-module-Params-Validate
Version: 0.91
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Params-Validate-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

Requires: perl
BuildRequires: perl

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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%doc Changes
%{perl_prefix}/man/man3/*
%{site_perl}/Attribute/Params/*
%{site_perl}/Params/*
%{site_perl_arch}/auto/Params/*

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.91-1
- Fixed spec file name, added changelog, updated to version 0.91

