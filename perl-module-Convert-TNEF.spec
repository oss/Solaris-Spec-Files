%include perl-header.spec

Summary: Convert TNEF perl module
Name: perl-module-Convert-TNEF
Version: 0.17
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Convert-TNEF-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Convert-TNEF-%{version}

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
%{site_perl}/*
%{perl_prefix}/man/man3/*
