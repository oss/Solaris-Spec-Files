%include perl-header.spec

Summary: Apache-Test is a test toolkit for testing an Apache server with any configuration.

Name: perl-module-Apache-Test
Version: 1.03 
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Apache-Test-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

Provides: perl-module-Apache-TestRun
Provides: perl-module-Apache-TestMM
Provides: perl-module-Apache-Client
Provides: perl-module-Apache-CommonPost
Provides: perl-module-Apache-TestConfigC
Provides: perl-module-Apache-TestServer
Provides: perl-module-Apache-TestConfig
Provides: perl-module-Apache-TestReportPerl
Provides: perl-module-Apache-TestHarness
Provides: perl-module-Apache-TestUtil
Provides: perl-module-Apache-TestSmoke
Provides: perl-module-Apache-TestTrace
Provides: perl-module-Apache-TestCommon
Provides: perl-module-Apache-TestSmokePerl
Provides: perl-module-Apache-ConfigParse
Provides: perl-module-Apache-Test5005compat
Provides: perl-module-Apache-TestBuild
Provides: perl-module-Apache-TestPerlDB
Provides: perl-module-Apache-TestRequest
Provides: perl-module-Apache-TestHandler
Provides: perl-module-Apache-TestRunPerl
Provides: perl-module-Apache-TestReport
Provides: perl-module-Apache-TestSSLCA
Provides: perl-module-Apache-TestSort
Provides: perl-module-Apache-ApacheTest

%description
Apache::Test is a test toolkit for testing an Apache server with any
configuration. It works with Apache 1.3 and Apache 2.0 and any of its
modules, including mod_perl 1.0 and 2.0. It was originally developed
for testing mod_perl 2.0.

%prep

%setup -q -n Apache-Test-%{version}

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
%doc README
%{site_perl}/Apache/Test*
%{site_perl}/Bundle/ApacheTest.pm
%{site_perl_arch}/auto/Apache/Test
%{perl_prefix}/man/man3/*
