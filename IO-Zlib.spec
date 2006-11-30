%include perl-header.spec


Summary: IO::Zlib

Name: perl-module-IO-Zlib
Version: 1.04
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: IO-Zlib-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl
Requires: perl

%description
IO:: style interface to Compress::Zlib

%prep

%setup -q -n IO-Zlib-%{version}

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
%{site_perl}/IO/Zlib.pm
%{site_perl_arch}/auto/IO/Zlib
%{perl_prefix}/man/man3/*
