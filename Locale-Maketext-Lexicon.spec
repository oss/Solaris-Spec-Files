%include perl-header.spec

Summary: Locale::Maketext::Lexicon
Name: perl-module-Locale-Maketext-Lexicon
Version: 0.27
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Locale-Maketext-Lexicon-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
 Locale::Maketext::Lexicon is a module providing
 lexicon-handling backends, for "Locale::Maketext" to read from other
 localization formats, such as PO files, MO files, or from databases via
 the "Tie" interface.

 You can also read my presentation "Web Localization in Perl" online at
 http://www.autrijus.org/webl10n/.  It gives an overview for the localization
 process, features a comparison between Gettext, Msgcat and Maketext, and
 talks about my experiences at localizing web applications based on HTML::Mason
 and the Template Toolkit.
 
%prep

%setup -q -n Locale-Maketext-Lexicon-%{version}

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
%doc README Changes AUTHORS
%{perl_prefix}/bin/xgettext.pl
%{site_perl}/Locale/Maketext/Lexicon.pm
%{site_perl}/Locale/Maketext/Lexicon
%{site_perl_arch}/auto/Locale/Maketext/Lexicon
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*
