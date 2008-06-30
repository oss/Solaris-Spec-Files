%include perl-header.spec

Summary: Perl-based web site development and delivery system 
Name: perl-module-HTML-Mason
Version: 1.39
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Mason-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl, perl-module-Module-Build 

Requires: perl-module-Cache-Cache >= 1
BuildRequires: perl-module-Cache-Cache >= 1

Requires: perl-module-Class-Container
BuildRequires: perl-module-Class-Container

Requires: perl-module-Exception-Class
BuildRequires: perl-module-Exception-Class

Requires: perl-module-Scalar-List-Util
BuildRequires: perl-module-Scalar-List-Util

Requires: perl-module-Params-Validate >= 0.7
BuildRequires: perl-module-Params-Validate >= 0.7

Requires: perl-module-HTML-Parser
BuildRequires: perl-module-HTML-Parser

Requires: perl-module-Test-Simple
BuildRequires: perl-module-Test-Simple

%description
Mason allows web pages and sites to be constructed from shared, 
reusable building blocks called components. Components contain
a mix of Perl and HTML, and can call each other and pass values back
and forth like subroutines. Components increase modularity and
eliminate repetitive work: common design elements (headers, footers,
menus, logos) can be extracted into their own components where they
need be changed only once to affect the whole site.

%prep

%setup -q -n HTML-Mason-%{version}

%build
%{pbuild}
./Build test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pbuild_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Apache/Mason.pm
%{site_perl}/Bundle/HTML/Mason.pm
%{site_perl}/HTML/Mason.pm
%{site_perl}/HTML/Mason/*
%{site_perl_arch}/auto/HTML/Mason
%{global_perl}/bin/*
%{global_perl}/man/man3/*

%changelog
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.39-1
- Added changelog, added some requirements, and updated to version 1.39
