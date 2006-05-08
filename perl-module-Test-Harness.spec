%include perl-header.spec
%define module_name Test-Harness

Summary: Run Perl standard test scripts with statistics
Name: perl-module-%{module_name}
Version: 2.56
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
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-, bin, bin)
%doc Changes NOTES
%{global_perl}/Test/*
%{global_perl_arch}/auto/*
%{perl_prefix}/bin/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 2.56-1
