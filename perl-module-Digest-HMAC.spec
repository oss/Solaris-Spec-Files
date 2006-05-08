%include perl-header.spec
%define module_name Digest-HMAC
 
Summary: Try every conceivable way to get full hostname
Name: perl-module-%{module_name}
Version: 1.01
Release: 2
Group: System Environments/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~gaas/%{module_name}-%{version}/lib/Digest/HMAC_MD5.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}, perl-module-Test-Simple

%description
This module provide HMAC-MD5 hashing.

%prep
%setup -qn %{module_name}-%{version}

%build
%{perl_binary} Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-, bin, bin)
%doc Changes README
%{site_perl}/Digest/*
%{site_perl_arch}/auto/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Apr 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.01-2
- Added perl-module-Test-Simple to BuildRequires.
* Wed Apr 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.01-1
