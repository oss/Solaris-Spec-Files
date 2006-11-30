%include perl-header.spec

Summary: File-Which

Name: perl-module-File-Which
Version: 0.05
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: File-Which-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
File-Which

%prep

%setup -q -n File-Which-%{version}

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
%doc README
%{site_perl}/File
%{site_perl_arch}/auto/File/*
/usr/perl5/bin/pwhich
%{perl_prefix}/man/*
