%include perl-header.spec

Summary: Class-Data-Inheritable - Inheritable, overridable class data

Name: perl-module-Class-Data-Inheritable
Version: 0.02
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Class-Data-Inheritable-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
Class::Data::Inheritable is for creating accessor/mutators to class data. That is, if you want to store something about your class as a whole (instead of about a single object). This data is then inherited by your subclasses and can be overriden.

%prep

%setup -q -n Class-Data-Inheritable-%{version}

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
%{site_perl}/Class/Data/Inheritable.pm
%{site_perl_arch}/auto/Class/Data/Inheritable
%{perl_prefix}/man/man3/*
