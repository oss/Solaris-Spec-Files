%include perl-header.spec

Summary: File-Spec

Name: perl-module-File-Spec
Version: 0.82
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: File-Spec-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
File-Spec

%prep

%setup -q -n File-Spec-%{version}

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
%{global_perl}/File
%{global_perl_arch}/auto/File/*
%{perl_prefix}/man/man3/*
