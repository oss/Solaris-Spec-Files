%include perl-header.spec

Summary: Perl interface to the iconv() codeset conversion function
Name: perl-module-Text-Iconv
Version: 1.2
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
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
