%include perl-header.spec

Summary: HTML-Format

Name: perl-module-HTML-Format
Version: 2.04
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Format-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

Requires: perl-module-Font-AFM
BuildRequires: perl-module-Font-AFM

Requires: perl-module-HTML-Tree
BuildRequires: perl-module-HTML-Tree

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
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes test.html
%{site_perl}/HTML/*
%{site_perl_arch}/auto/HTML-Format
%{perl_prefix}/man/man3/*

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.04-1
- Added changelog, added build requirements, updated to version 2.04
