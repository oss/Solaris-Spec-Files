%include perl-header.spec

Summary: Perl interface to the iconv() codeset conversion function
Name: perl-module-Text-Iconv
Version: 1.7
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Iconv-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module provides a Perl interface to the iconv() codeset
conversion function, as defined by the Single UNIX Specification.
For more details see the POD documentation embedded in the file
Iconv.pm, which will also be installed as Text::Iconv(3) man page.


%prep

%setup -q -n Text-Iconv-%{version}

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
rm -rf %{buildroot}
%{pmake_install}
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

%changelog
* Tue Jun 26 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.7-1
- Added changelog and updated to version 1.7
