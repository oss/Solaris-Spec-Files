%include perl-header.spec
%define module_name Test-Harness

Summary: Run Perl standard test scripts with statistics
Name: perl-module-%{module_name}
Version: 3.13
Release: 1
Group: System Environment/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~petdance/%{module_name}-%{version}/lib/Test/Harness.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Test::Harness is the module that reads the output from Test::Simple, Test::More and other
modules based on Test::Builder.

%prep
%setup -qn %{module_name}-%{version}

%build
%{perl_binary} Makefile.PL
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
%defattr(-, bin, bin)
%doc README Changes
%{global_perl}/Test/*
%{global_perl}/App/*
%{global_perl}/TAP/*
%{global_perl_arch}/auto/*
%{perl_prefix}/bin/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*

%changelog
* Tue Sep 09 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.13-1
- Bumped to version 3.13
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.12-1
- Added changelog and updated to version 3.12
