%include perl-header.spec

Summary: RSA public-key cryptosystem 
Name: perl-module-Crypt-RSA
Version: 1.58
Release: 1
Group: System Environment/Base
Copyright: GPL
Source: Crypt-RSA-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Crypt-CBC perl-module-Class-Loader perl-module-Convert-ASCII-Armour perl-module-Crypt-Blowfish perl-module-Crypt-Primes perl-module-Data-Buffer perl-module-DigestMD2 perl-module-Sort-Versions perl-module-Tie-EncryptedHash
BuildRequires: perl = %{perl_version} perl-module-Crypt-CBC perl-module-Class-Loader perl-module-Convert-ASCII-Armour perl-module-Crypt-Blowfish perl-module-Crypt-Primes perl-module-Data-Buffer perl-module-DigestMD2 perl-module-Sort-Versions perl-module-Tie-EncryptedHash

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the RSA
public-key cryptosystem. It uses Math::Pari(3), a perl interface to the
blazingly fast PARI library, for big integer arithmetic and number
theoretic computations.

Crypt::RSA provides arbitrary size key-pair generation, plaintext-aware
encryption (OAEP) and digital signatures with appendix (PSS). For
compatibility with SSLv3, RSAREF2, PGP and other applications that
follow the PKCS #1 v1.5 standard, it also provides PKCS #1 v1.5
encryption and signatures.

%prep
%setup -q -n Crypt-RSA-%{version}

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
/usr/perl5/man/*
%{site_perl}/Crypt
%{site_perl_arch}
