%include perl-header.spec

Summary: Perl interface to the DNS resolver
Name: perl-module-Net-DNS
Version: 0.14
Release: 6
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Net-DNS-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Net::DNS is a collection of Perl modules that act as a Domain Name
System (DNS) resolver.  It allows the programmer to perform DNS
queries that are beyond the capabilities of `gethostbyname' and
`gethostbyaddr'.

%prep
%setup -q -n Net-DNS-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Net/DNS
%{site_perl_arch}/auto/Net/DNS
%{perl_prefix}/man/man3/*
