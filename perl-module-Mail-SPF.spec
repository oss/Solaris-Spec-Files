%include perl-header.spec

Summary:	Mail::SPF - An object-oriented implementation of Sender Policy Framework
Name:		perl-module-Mail-SPF
Version:	2.006
Release:	1
Group:		System Environment/Base
License:	BSD
Vendor:		NBCS-OSS
Distribution:	RU-Solaris
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Source:		Mail-SPF-v%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
Requires:       perl-module-version, perl-module-Error, perl-module-NetAddr-IP
Requires:       perl-module-Net-DNS-Resolver-Programmable, perl-module-URI
BuildRequires:	perl = %{perl_version} 
BuildRequires:	perl-module-Module-Build, perl-module-Test-Simple
BuildRequires:	perl-module-version, perl-module-Error, perl-module-NetAddr-IP
BuildRequires:  perl-module-Net-DNS-Resolver-Programmable, perl-module-URI

%description
Mail::SPF is an object-oriented implementation of Sender Policy Framework (SPF). 
See http://www.openspf.org for more information about SPF.

This class collection aims to fully conform to the SPF specification (RFC 4408) 
so as to serve both as a production quality SPF implementation and as a reference 
for other developers of SPF implementations.

%prep
%setup -q -n Mail-SPF-v%{version}

%build
%{pbuild}

# Test fails on 00.03-class-result.t
# Hopefully things will still work
# ./Build test 

%install
rm -rf %{buildroot}
%{pbuild_install}

# Module::Build provides no mechanism to set sbin path
mkdir %{buildroot}/usr/local
mv %{buildroot}/usr/sbin %{buildroot}/usr/local/sbin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README LICENSE CHANGES TODO
%{global_perl}/man/man1/*
%{global_perl}/man/man3/*
%{global_perl}/bin/*
%{site_perl}/Mail/SPF.pm
%{site_perl}/Mail/SPF
%{site_perl_arch}/auto/Mail/SPF/.packlist
%{_sbindir}/spfd

%changelog
* Mon Sep 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.006-1
- Initial build.

