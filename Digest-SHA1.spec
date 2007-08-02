%include perl-header.spec

Summary: SHA-1 message digest algorithm for Perl.
Name: perl-module-Digest-SHA1
Version: 2.10
Release: 2
Group: Libraries/Perl
Copyright: GPL/Artistic
Source: Digest-SHA1-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}


%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs.  The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

SHA1 is described at <http://www.itl.nist.gov/fipspubs/fip180-1.htm>

%prep
%setup -q -n Digest-SHA1-%{version}

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
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%{perl_prefix}/man/man3/*
%{site_perl}/*

%changelog
* Tue Jul 31 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.10-2
- Respin
