%include perl-header.spec

Summary: Text-Template

Name: perl-module-Text-Template
Version: 1.45
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Template-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.  


%prep

%setup -q -n Text-Template-%{version}

%build
perl Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Artistic COPYING
%{site_perl}/Text/Template.pm
%{site_perl}/Text/Template/*
%{site_perl_arch}/auto/Text/Template
%{perl_prefix}/man/man3/*

%changelog
* Thu Jun 26 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.45-1
- Added changelog and updated to version 1.45
