%include perl-header.spec

Summary: MLDMB Perl Module

Name: perl-module-MLDBM
Version: 2.01
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: MLDBM-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
None given.

%prep

%setup -q -n MLDBM-%{version}

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
