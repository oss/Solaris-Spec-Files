%include perl-header.spec

Summary: HTML-Format

Name: perl-module-HTML-Format
Version: 2.03
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Format-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
Requires: perl-module-Font-AFM
Requires: perl-modules-HTML-Element
BuildRequires: perl

Provides: perl-module-HTML-FormatPS
Provides: perl-module-HTML-FormatRTF
Provides: perl-module-HTML-Formatter
Provides: perl-module-HTML-FormatText

%description
This is a collection of modules that formats HTML as plaintext,
PostScript or RTF.

The modules present in this package are:

  HTML::FormatText - Formatter that converts a syntax tree to plain
        readable text.

  HTML::FormatPS - Formatter that outputs PostScript code.

  HTML::FormatRTF - Formatter that outputs RTF code.

  HTML::Formatter - Base class for various formatters.  Formatters
        traverse a syntax tree and produce some textual output.  None
        of the current formatters handle tables or forms yet.


%prep

%setup -q -n HTML-Format-%{version}

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
%doc README Changes test.html
%{site_perl}/HTML/*
%{site_perl_arch}/auto/HTML-Format
%{perl_prefix}/man/man3/*
