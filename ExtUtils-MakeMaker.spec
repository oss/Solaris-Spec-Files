%include perl-header.spec

Summary: ExtUtils::MakeMaker - create an extension Makefile

Name: perl-module-ExtUtils-MakeMaker
Version: 6.17
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
	This utility is designed to write a Makefile for an extension 
	module from a Makefile.PL. It is based on the Makefile.SH model 
	provided by Andy Dougherty and the perl5-porters.

	It splits the task of generating the Makefile into several 
	subroutines that can be individually overridden. Each subroutine 
	returns the text it wishes to have written to the Makefile.

	MakeMaker is object oriented. Each directory below the current 
	directory that contains a Makefile.PL is treated as a separate 
	object. This makes it possible to write an unlimited number of 
	Makefiles with a single invocation of WriteMakefile(). 

%prep

%setup -q -n ExtUtils-MakeMaker-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
rm -f $RPM_BUILD_ROOT/%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,bin,bin)
%doc README Changes NOTES TODO
%{global_perl}/ExtUtils/*
%{global_perl_arch}/auto/*
%{perl_prefix}/bin/*
%{perl_prefix}/man/man3/*

