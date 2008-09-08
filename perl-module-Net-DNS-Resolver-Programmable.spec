%include perl-header.spec

Summary:	Net-DNS-Resolver-Programmable
Name:		perl-module-Net-DNS-Resolver-Programmable
Version:	0.003
Release:	1
Group:		System Environment/Base
License:	GPL/Artistic
Source:		Net-DNS-Resolver-Programmable-v%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
BuildRequires:	perl = %{perl_version}, perl-module-Module-Build
Requires:	perl-module-version, perl-module-Net-DNS
BuildRequires:	perl-module-version, perl-module-Net-DNS

%description
This perl module implements Net-DNS-Resolver-Programmable

%prep
%setup -q -n Net-DNS-Resolver-Programmable-v%{version}

%build
%{pbuild}
./Build test

%install
rm -rf %{buildroot}
%{pbuild_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README LICENSE CHANGES TODO
%{global_perl}/man/man3/*
%{site_perl_arch}/auto/Net/DNS/Resolver/Programmable
%{site_perl}/Net/DNS/Resolver/Programmable.pm

%changelog
* Mon Sep 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.003-1
- Added changelog, use pbuild now, updated to version 0.003.

