%include perl-header.spec
%define module_name ExtUtils-MakeMaker

Summary: Create a module Makefile
Name: perl-module-%{module_name}
Version: 6.31
Release: 1
Group: System Environment/Base
License: Perl (Artistic and GPL-2)
Source: ExtUtils-MakeMaker-%{version}.tar.gz
URL: http://search.cpan.org/~mschwern/ExtUtils-MakeMaker-6.31/lib/ExtUtils/MakeMaker.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}, perl-module-Test-Simple

%description
This utility is designed to write a Makefile for an extension module from a Makefile.PL.
It is based on the Makefile.SH model provided by Andy Dougherty and the perl5-porters.

%prep
%setup -qn %{module_name}-%{version}

%build
perl Makefile.PL
make
make test

%install
# Since it is built locally, it is necessary to specify PERL5LIB here,
# otherwise you get this error:
# Can't locate ExtUtils/Command/MM.pm in @INC
PERL5LIB="$PERL5LIB:%{buildroot}/usr/perl5/5.6.1/"
export PERL5LIB
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes NOTES PATCHING TODO
%{global_perl}/ExtUtils/*
%{global_perl_arch}/auto/*
%{perl_prefix}/bin/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*

%changelog
* Thu Apr 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 6.30-3
- Added perl-module-Test-Simple to BuildRequires.
* Tue Apr 18 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 6.30-2
- Made the ExtUtils-MakeMaker perl module spec file follow the naming convention.
