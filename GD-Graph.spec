%include perl-header.spec

Summary: YAML Ain't Markup Language (tm)

Name: perl-module-YAML
Version: 0.35
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: YAML-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
%if %{which_perl} == "REPOSITORY"
Requires: perl-module-ExtUtils-MakeMaker >= 6.05-1
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.05-1
%endif
#Requires: perl-module-Module-Build >= 0.18-1
#BuildRequires: perl-module-Module-Build >= 0.18-1

%description
YAML Stands For: YAML Ain't Markup Language
this: is valid YAML
YAML website: http://www.yaml.org

%prep

%setup -q -n YAML-%{version}

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
%doc README Changes
%{perl_prefix}/bin/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*
%{site_perl}/YAML*
%{site_perl_arch}/auto/YAML
