%include perl-header.spec

Summary: Perl interfaces for MD5, MD2 and SHA1 message digest algorithms
Name: perl-module-Digest-MD5
Version: 2.36
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Digest-MD5-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-Digest >= 1.15, perl-module-File-Spec >= 0.82-2
BuildRequires: perl = %{perl_version}, perl-module-Digest >= 1.15, perl-module-File-Spec >= 0.82-2
#Obsoletes: perl-module-SHA
#Provides: perl-module-Digest-SHA1 perl-module-Digest-MD2
Provides: perl-module-Digest-MD2

%description
This package contains Perl extension interfaces for the following
message digest algorithms:

  - RSA Data Security Inc. MD5   (RFC 1321)
  - RSA Data Security Inc. MD2   (RFC 1319)
  - NIST SHA-1                   (FIPS PUB 180-1)

Modules to calculate HMAC (RFC 2104) digests are also provided.

%prep
%setup -q -n Digest-MD5-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include " \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

perl Makefile.PL
gmake
gmake test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/
#%{site_perl_arch}/auto/Digest/*
#%{site_perl_arch}/*pm
#%{site_perl_arch}/Digest/*
%{perl_prefix}/man/man3/*

%changelog
* Fri Sep 5 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.36-2
- added environment variables 
- switched to gmake
- added Requires for perl-module-File-Spec
