%include perl-header.spec

Summary: Devel::StackTrace - Stack trace and stack trace frame objects

Name: perl-module-Devel-StackTrace
Version: 1.1901
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Devel-StackTrace-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace 
and Devel::StackTraceFrame. The goal of this object is to encapsulate 
the information that can found through using the caller() function, 
as well as providing a simple interface to this data.

The Devel::StackTrace object contains a set of Devel::StackTraceFrame 
objects, one for each level of the stack. The frames contain all the 
data available from caller().

%prep

%setup -q -n Devel-StackTrace-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -r %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README LICENSE Changes
%{site_perl}/Devel/StackTrace.pm
%{site_perl_arch}/auto/Devel/StackTrace
%{perl_prefix}/man/man3/*

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.1901-1
- Added changelog and updated to version 1.1901
