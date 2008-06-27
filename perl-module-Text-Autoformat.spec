%include perl-header.spec

Summary: Text-Autoformat
Name: perl-module-Text-Autoformat
Version: 1.14.0
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Autoformat-v%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl, perl-module-version, perl-module-Text-Reform
Requires: perl-module-Text-Reform

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

%setup -q -n Text-Autoformat-v%{version}

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
%doc README Changes
%{site_perl}/Text/Autoformat.pm
%{site_perl_arch}/auto/Text/Autoformat
%{perl_prefix}/man/man3/*

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.14.0-1
- Added changelog and updated to version 1.14.0
