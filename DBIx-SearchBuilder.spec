%include perl-header.spec

Summary: DBIx-SearchBuilder - Encapsulate SQL queries and rows in simple perl objects

Name: perl-module-DBIx-SearchBuilder
Version: 0.88
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: DBIx-SearchBuilder-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
 Encapsulate SQL queries and rows in simple perl objects

%prep

%setup -q -n DBIx-SearchBuilder-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Changes
%{site_perl}/DBIx/SearchBuilder.pm
%{site_perl}/DBIx/SearchBuilder/*
%{site_perl_arch}/auto/DBIx/SearchBuilder
%{perl_prefix}/man/man3/*
