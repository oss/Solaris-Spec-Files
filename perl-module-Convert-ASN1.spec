%include perl-header.spec

Summary: 	Convert ASN1 perl module
Name: 		perl-module-Convert-ASN1
Version: 	0.21
Release: 	1
Group: 		System Environment/Base
License: 	Perl (Artistic and GPL)
Source:	 	Convert-ASN1-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}, perl-module-Test-Simple
BuildRequires: 	perl = %{perl_version}, perl-module-Test-Simple

%description
ASN.1 Encode/Decode library

%prep

%setup -q -n Convert-ASN1-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefi}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%doc README Changes
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.21-1
- Updated to latest version (0.21).

