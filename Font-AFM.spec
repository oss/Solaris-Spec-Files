%include perl-header.spec

Summary: Font::AFM - Interface to Adobe Font Metrics files

Name: perl-module-Font-AFM
Version: 1.18
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Font-AFM-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl


%description
    This module implements the Font::AFM class. Objects of this
    class are initialised from an AFM-file and allows you to obtain
    information about the font and the metrics of the various glyphs
    in the font.

    All measurements in AFM files are given in terms of units equal
    to 1/1000 of the scale factor of the font being used. To compute
    actual sizes in a document, these amounts should be multiplied
    by (scale factor of font)/1000.

%prep

%setup -q -n Font-AFM-%{version}

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
%{site_perl}/Font/AFM.pm
%{site_perl}/Font/Metrics/*
%{site_perl_arch}/auto/Font/AFM
%{perl_prefix}/man/man3/*
