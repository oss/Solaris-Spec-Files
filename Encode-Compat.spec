%include perl-header.spec

Summary: Encode::compat, a module providing compatibility interfaces for Encode.pm on Perl versions earlier than 5.7.1.

Name: perl-module-Encode-compat
Version: 0.05
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Encode-compat-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module provides a Perl interface to the iconv() codeset
conversion function, as defined by the Single UNIX Specification.
For more details see the POD documentation embedded in the file
Iconv.pm, which will also be installed as Text::Iconv(3) man page.


%prep

%setup -q -n Encode-compat-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Encode/compat.pm
%{site_perl}/Encode/compat
%{site_perl_arch}/auto/Encode/compat
%{perl_prefix}/man/man3/*
