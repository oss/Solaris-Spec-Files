%include perl-header.spec

Summary: Locale-Maketext

Name: perl-module-Locale-Maketext
Version: 1.05
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Locale-Maketext-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Locale::Maketext is a base class providing a framework for
localization and inheritance-based lexicons, as described in my
article in The Perl Journal #13 (a corrected version of which appears
in this dist).

This is a complete rewrite from the basically undocumented 0.x
versions.


%prep

%setup -q -n Locale-Maketext-%{version}

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
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
