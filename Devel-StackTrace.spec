%include perl-header.spec

Summary: Devel::StackTrace - Stack trace and stack trace frame objects

Name: perl-module-Devel-StackTrace
Version: 1.03
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Devel-StackTrace-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace and Devel::StackTraceFrame. The goal of this object is to encapsulate the information that can found through using the caller() function, as well as providing a simple interface to this data.

The Devel::StackTrace object contains a set of Devel::StackTraceFrame objects, one for each level of the stack. The frames contain all the data available from caller() as of Perl 5.6.0 though this module still works with 5.00503.

This code was created to support my Exception::Class::Base class (part of Exception::Class) but may be useful in other contexts.

%prep

%setup -q -n Devel-StackTrace-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
%{site_perl}/Devel/StackTrace.pm
%{site_perl_arch}/auto/Devel/StackTrace
%{perl_prefix}/man/man3/*
