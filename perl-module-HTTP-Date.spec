%include perl-header-unstable.spec

Summary: date conversion routines

%define module_name HTTP-Date

Name: perl-module-%{module_name}
Version: 6.00
Release: 1.ru
Group: System Environment/Base
License: GPL/Artistic
Source: %{module_name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl >= 5.8.8
BuildRequires: perl-devel >= 5.8.8

%description
This module provides functions that deal the date formats used by the HTTP protocol (and then some more). Only the first two functions, time2str() and str2time(), are exported by default.

%prep

%setup -q -n %{module_name}-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

#Remove the packlist file
find $RPM_BUILD_ROOT -name .packlist | xargs rm
find $RPM_BUILD_ROOT -name *.pod | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,bin,bin)
%doc README Changes

%{site_perl}/HTTP/Date.pm

%changelog
* Fri Mar 31 2011 Vaibhav Verma <vverna@nbcs.rutgers.edu> 6.00-1.ru 
- Initial Rutgers build
