%include perl-header.spec

Summary: I18N::LangTags - functions for dealing with RFC3066-style language tags
Name: perl-module-I18N-LangTags
Version: 0.28
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: I18N-LangTags-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

Provides: perl-module-I18N-LangTags-List

%description
 Language tags are a formalism, described in RFC 3066 (obsoleting 1766), for declaring what
   language form (language and possibly dialect) a given chunk of information is in.

   This library provides functions for common tasks involving language tags as they are
needed in
   a variety of protocols and applications.

   Please see the "See Also" references for a thorough explanation of how to correctly use
   language tags.


%prep

%setup -q -n I18N-LangTags-%{version}

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
%{site_perl}/I18N/LangTags*
%{site_perl_arch}/auto/I18N/LangTags
%{perl_prefix}/man/man3/*
