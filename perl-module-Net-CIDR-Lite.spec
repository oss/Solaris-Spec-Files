%include perl-header.spec
%define module_name Net-CIDR-Lite

Summary: Perl extension for merging IPv4 or IPv6 CIDR addresses
Name: perl-module-%{module_name}
Version: 0.20
Release: 2
Group: System Environments/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~dougw/%{module_name}-%{version}/Lite.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}, perl-module-Test-Simple

%description
Faster alternative to Net::CIDR when merging a large number of CIDR address ranges.
Works for IPv4 and IPv6 addresses.

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
%{site_perl}/Net/*
%{site_perl_arch}/auto/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.20-2
- Removed perl-module-Test-Simple from Requires.
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.20-1
- Updated to the latest version.