%include perl-header.spec

Summary: GDGraph -- a package to generate charts

Name: perl-module-GDGraph
Version: 1.43
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: GDGraph-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
%if %{which_perl} == "REPOSITORY"
Requires: perl-module-ExtUtils-MakeMaker >= 6.05-1
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.05-1
%endif

%description
This is GDGraph, a package to generate charts, using Lincoln Stein's
GD.pm. See the documentation for some history and more information.


%prep

%setup -q -n GDGraph-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
rm -f $RPM_BUILD_ROOT/%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README CHANGES
%{perl_prefix}/*
%{perl_prefix}/man/man3/*
%{site_perl}/GD/Graph.pm
%{site_perl}/GD/Graph/*
%{site_perl_arch}/auto/GD/Graph/*
