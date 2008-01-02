%include perl-header.spec

Summary: 	SQL parsing and processing engine
Name: 		perl-module-SQL-Statement
Version: 	1.15
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	SQL-Statement-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution engine. While it by no means implements full ANSI standard, it does support many features including column and table aliases, built-in and user-defined functions, implicit and explicit joins, complexly nested search conditions, and other features.


%prep
%setup -q -n SQL-Statement-%{version}

%build
perl Makefile.PL
make
set +e; make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%{site_perl}/SQL
%{perl_prefix}/man/man3/*
/usr/perl5/5.6.1/lib/sun4-solaris-64int/perllocal.pod

%changelog
* Wed Jan 02 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.15-1
- Initial Build.
