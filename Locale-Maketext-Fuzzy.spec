%include perl-header.spec

Summary: Locale-Maketext-Fuzzy
Name: perl-module-Locale-Maketext-Fuzzy
Version: 0.02
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Locale-Maketext-Fuzzy-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Locale::Maketext::Fuzzy is a subclass of Locale::Maketext with 
additional support for localizing messages that already contains 
interpolated variables.

%prep

%setup -q -n Locale-Maketext-Fuzzy-%{version}

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
%{site_perl}/Locale/Maketext
%{site_perl_arch}/auto/Locale/Maketext
%{perl_prefix}/man/man3/*
