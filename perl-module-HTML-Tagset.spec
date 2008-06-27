%include perl-header.spec

Summary: Helps parse HTML
Name: perl-module-HTML-Tagset
Version: 3.20
Release: 1
Group: System Enviroment/Base
Copyright: GPL
Source: HTML-Tagset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl
BuildRequires: perl
BuildRequires: perl-module-Test-Simple

%description
This module contains data tables useful in dealing with HTML.

It provides no functions or methods.

%prep

%setup -q -n HTML-Tagset-%{version}

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
%defattr(-,root,root)
%doc README Changes
%{site_perl}/HTML/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 3.20-1
- Added changelog and updated to latest version

