%include perl-header.spec

Summary: Inheritable, overridable class data

Name: perl-module-Class-Data-Inheritable
Version: 0.08
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Class-Data-Inheritable-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl, perl-module-Test-Simple

%description
Class::Data::Inheritable is for creating accessor/mutators to class data. That is, if you want to 
store something about your class as a whole (instead of about a single object). This data is then 
inherited by your subclasses and can be overridden.

%prep

%setup -q -n Class-Data-Inheritable-%{version}

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
%doc README Changes
%{site_perl}/Class/Data/Inheritable.pm
%{site_perl_arch}/auto/Class/Data/Inheritable
%{perl_prefix}/man/man3/*

%changelog
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.08-1
- Added changelog and updated to version 0.08
