%include perl-header.spec
%define module_name Mail-SPF-Query

Summary: query Sender Policy Framework for an IP,email,helo
Name: perl-module-%{module_name}
Version: 1.999.1
Release: 1
Group: System Environment/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~jmehnle/%{module_name}-%{version}/lib/Mail/SPF/Query.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}, perl-module-Net-DNS >= 0.46, perl-module-URI, perl-module-Sys-Hostname-Long, perl-module-Net-CIDR-Lite >= 0.15
BuildRequires: perl = %{perl_version}, perl-module-Net-DNS >= 0.46, perl-module-URI, perl-module-Sys-Hostname-Long, perl-module-Net-CIDR-Lite >= 0.15

%description
The SPF protocol relies on sender domains to describe their designated
outbound mailers in DNS. Given an email address, Mail::SPF::Query determines
the legitimacy of an SMTP client IP address.

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
%{perl_prefix}/bin/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*
%{site_perl}/Mail/*
%{site_perl_arch}/auto/*

%changelog
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.99.1-1
- Initial package.