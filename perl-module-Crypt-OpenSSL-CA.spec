%include perl-header.spec

Summary: The crypto parts of an X509v3 Certification Authority 
Name: perl-module-Crypt-OpenSSL-CA
Version: 0.08
Release: 1
Group: System Environment/Base
Copyright: GPL
Source: Crypt-OpenSSL-CA-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} openssl perl-module-Module-Build perl-module-File-Slurp
BuildRequires: perl = %{perl_version} openssl perl-module-Module-Build perl-module-File-Slurp

%description
This module performs the cryptographic operations necessary to issue 
X509 certificates and certificate revocation lists (CRLs). It is 
implemented as a Perl wrapper around the popular OpenSSL library.

Crypt::OpenSSL::CA is an essential building block to create an X509v3 
Certification Authority or CA, a crucial part of an X509 Public Key 
Infrastructure (PKI). A CA is defined by RFC4210 and friends (see 
Crypt::OpenSSL::CA::Resources) as a piece of software that can (among 
other things) issue and revoke X509v3 certificates. To perform the 
necessary cryptographic operations, it needs a private key that is kept 
secret (currently only RSA is supported).

Despite the name and unlike the openssl ca command-line tool, 
Crypt::OpenSSL::CA is not designed as a full-fledged X509v3 
Certification Authority (CA) in and of itself: some key features are 
missing, most notably persistence (e.g. to remember issued and revoked 
certificates between two CRL issuances) and security-policy based 
screening of certificate requests. Crypt::OpenSSL::CA mostly does ``just 
the crypto'', and this is deliberate: OpenSSL's features such as 
configuration file parsing, that are best implemented in Perl, have been 
left out for maximum flexibility.

%prep
%setup -q -n Crypt-OpenSSL-CA-%{version}

%build
%{perl_binary} Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/../Crypt/*
%{site_perl_arch}/auto/Crypt/CBC
