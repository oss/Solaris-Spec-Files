%include perl-header.spec

Summary: Attribute::Handlers - Simpler definition of attribute handlers

Name: perl-module-Attribute-Handlers
Version: 0.78
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Attribute-Handlers-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
	This module, when inherited by a package, allows that package's class to
	define attribute handler subroutines for specific attributes. Variables
	and subroutines subsequently defined in that package, or in packages
	derived from that package may be given attributes with the same names as
	the attribute handler subroutines, which will then be called at the end
	of the compilation phase (i.e. in a `CHECK' block).
												
%prep

%setup -q -n Attribute-Handlers-%{version}

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
%doc README Changes
%{perl_prefix}/man/man3/*
%{site_perl}/Attribute/*
%{site_perl_arch}/auto/Attribute/*

