%include perl-header.spec

Summary: Module::Info - Show information about modules

Name: perl-module-Module-Info
Version: 0.20
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Module-Info-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%if %{which_perl} == "SOLARIS"
Requires: perl-module-File-Spec >= 0.82-2
BuildRequires: perl-module-File-Spec >= 0.82-2
%endif

%if %{which_perl} == "REPOSITORY"
Requires: perl-module-ExtUtils-MakeMaker >= 6.05-1
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.05-1
%endif


%description
	Show information about modules

%prep

%setup -q -n Module-Info-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
rm -f %{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Changes
%{perl_prefix}/bin/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*
%{site_perl}/B
%{site_perl}/Module
%{site_perl_arch}/auto/Module
