%include perl-header.spec

Summary: Information about Perl modules

Name: perl-module-Module-Info
Version: 0.31
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Module-Info-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
BuildRequires: perl-module-Module-Build, perl-module-Test-Simple

Requires: perl-module-Params-Validate >= 0.62-2
BuildRequires: perl-module-Params-Validate >= 0.62-2

%if %{which_perl} == "SOLARIS"
Requires: perl-module-ExtUtils-MakeMaker >= 6.05-1
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.05-1

Requires: perl-module-File-Spec >= 0.82-2
BuildRequires: perl-module-File-Spec >= 0.82-2
%endif


%description
Module::Info gives you information about Perl modules without actually loading the module. 
It actually isn't specific to modules and should work on any perl code.

%prep
%setup -q -n Module-Info-%{version}

%build
%{pbuild}
./Build test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pbuild_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc Changes
%{global_perl}/bin/*
%{global_perl}/man/man3/*
%{global_perl}/man/man1/*
%{site_perl}/B/Module/*
%{site_perl}/B/BUtils.pm
%{site_perl}/Module/Info.pm
%{site_perl_arch}/auto/Module/*

%changelog
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.31-1
- Added changelog and updated to latest version
