%include perl-header.spec

Summary: Mason allows web pages and sites to be constructed from shared, reusable building blocks called components.

Name: perl-module-HTML-Mason
Version: 1.19
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Mason-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Welcome to Mason, a Perl-based web site development and delivery
system.  Mason allows web pages and sites to be constructed from
shared, reusable building blocks called components. Components contain
a mix of Perl and HTML, and can call each other and pass values back
and forth like subroutines. Components increase modularity and
eliminate repetitive work: common design elements (headers, footers,
menus, logos) can be extracted into their own components where they
need be changed only once to affect the whole site.

%prep

%setup -q -n HTML-Mason-%{version}

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
