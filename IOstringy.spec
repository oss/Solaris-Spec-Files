%include perl-header.spec

Summary: IO stringy perl module
Name: perl-module-IO-stringy
Version: 2.108
Release: 0
Group: System Environment/Base
Copyright: Unknown
Source: IO-stringy-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n IO-stringy-%{version}

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
%{site_perl}/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
