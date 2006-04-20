%include perl-header.spec
%define module_name Net-DNS

Summary: Perl interface to the DNS resolver
Name: perl-module-%{module_name}
Version: 0.49
Release: 2
Group: System Environment/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~olaf/%{module_name}-%{version}/lib/Net/DNS.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}, perl-module-Digest-HMAC
BuildRequires: perl = %{perl_version}, perl-module-Digest-HMAC

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System (DNS) resolver.
It allows the programmer to perform DNS queries that are beyond the capabilities of
gethostbyname and gethostbyaddr.

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
%doc Changes README TODO demo/
%{site_perl}/Net/*
%{site_perl_arch}/auto/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 0.49-2
- Rebuilt without perllocal.pod.