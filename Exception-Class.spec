%include perl-header.spec

Summary: This module allows you to declare hierarchies of exception classes for use in your code.

Name: perl-module-Exception-Class
Version: 1.12
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Exception-Class-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module allows you to declare hierarchies of exception classes for
use in your code.  It also provides a simple exception class that it
uses as the default base class for all other exceptions.

You may choose to use another base class for your exceptions.
Regardless, the ability to declare all your exceptions at compile time
is a fairly useful trick and helps push people towards more structured
use of exceptions.


%prep

%setup -q -n Exception-Class-%{version}

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
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
