%include perl-header.spec


Summary: IO::String

Name: perl-module-IO-String
Version: 1.08
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: IO-String-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl
Requires: perl

%description
Emulate file interface for in-core strings 

%prep

%setup -q -n IO-String-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/IO/String.pm
%{site_perl_arch}/auto/IO/String
%{perl_prefix}/man/man3/*
