%include perl-header.spec

Summary: This distribution generates a Errno package which will define and optionally export all E* constants defined in your system <errno.h> file.

Name: perl-module-Errno
Version: 1.09
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Errno-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This distribution generates a Errno package which will define and
optionally export all E* constants defined in your system <errno.h>
file.

The d/Errno.pm file included in the distribution is only a dummy file
to emsure CPAN file find a VERSION number. The real Errno.pm file
will be created when you run make

%prep

%setup -q -n Errno-%{version}

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
