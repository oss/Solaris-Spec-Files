%include perl-header.spec

Summary: Text-Autoformat
Name: perl-module-Text-Autoformat
Version: 1.12
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Autoformat-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
    Text::Autoformat provides intelligent formatting of
    plaintext without the need for any kind of embedded mark-up. The module
    recognizes Internet quoting conventions, a wide range of bulleting and
    number schemes, centred text, and block quotations, and reformats each
    appropriately. Other options allow the user to adjust inter-word
    and inter-paragraph spacing, justify text, and impose various
    capitalization schemes. 

    The module also supplies a re-entrant, highly configurable replacement
    for the built-in Perl format() mechanism.

%prep

%setup -q -n Text-Autoformat-%{version}

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
%doc README Changes test.pl
%{site_perl}/Text/Autoformat.pm
%{site_perl_arch}/auto/Text/Autoformat
%{perl_prefix}/man/man3/*
