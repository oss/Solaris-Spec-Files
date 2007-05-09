%include perl-header.spec
%define module_name Mail-DomainKeys

Summary: A perl implementation of DomainKeys 
Name: perl-module-%{module_name}
Version: 1.0
Release: 1
Group: System Environment/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/CPAN/authors/id/A/AN/ANTHONYU/%{module_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version} perl-module-Crypt-RSA perl-module-Crypt-OpenSSL-RSA
BuildRequires: perl = %{perl_version} perl-module-Crypt-RSA perl-module-Crypt-OpenSSL-RSA

%description
Mail::DomainKeys is a perl implementation of Yahoo's mail signature 
protocol.

This library allows one to sign and verify signatures as per draft 03 of 
the DomainKeys specification:

http://www.ietf.org/internet-drafts/draft-delany-domainkeys-base-03.txt

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
%doc README Changes
%{perl_prefix}/man/man3/*
%{site_perl}/Mail/*

%changelog
* Thu May 03 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0-1
- Initial Rutgers release
