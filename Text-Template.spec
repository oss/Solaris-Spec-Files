%include perl-header.spec

Summary: Text-Template

Name: perl-module-Text-Template
Version: 1.44
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Template-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
Text::Template v1.44

This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.  


%prep

%setup -q -n Text-Template-%{version}

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
%doc README Artistic COPYING
%{site_perl}/Text/Template.pm
%{site_perl}/Text/Template/*
%{site_perl_arch}/auto/Text/Template
%{perl_prefix}/man/man3/*
