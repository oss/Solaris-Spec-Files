%include perl-header.spec

Summary: Regexp::Common - Provide commonly requested regular expressions

Name: perl-module-Regexp-Common
Version: 2.113
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Regexp-Common-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
By default, this module exports a single hash (%RE) that stores or generates commonly needed regular expressions (see "List of available patterns").

There is an alternative, subroutine-based syntax described in "Subroutine-based interface". 

%prep

%setup -q -n Regexp-Common-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
%{site_perl}/Regexp/Common.pm
%{site_perl}/Regexp/Common
%{site_perl_arch}/auto/Regexp/Common
%{perl_prefix}/man/man3/*
