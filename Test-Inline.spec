%include perl-header.spec

Summary: Test::Inline Inlining your tests next to the code being tested 

Name: perl-module-Test-Inline
Version: 0.15
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Test-Inline-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
Test::Inline Inlining your tests next to the code being tested. 
%prep

%setup -q -n Test-Inline-%{version}

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
%doc Changes docs
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/bin/pod2test
%{site_perl}/Pod/Tests.pm
%{site_perl}/Pod/Tests/*
%{site_perl}/Test/Inline.pm
%{site_perl}/Test/Inline
%{site_perl_arch}/auto/Test/Inline

