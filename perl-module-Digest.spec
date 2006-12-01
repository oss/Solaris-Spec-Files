%include perl-header.spec

Summary: Digest module
Name: perl-module-Digest
Version: 1.15
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Digest-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This is just a simple frontend module for autoloading of various
Digest:: modules.  It also provide documentation of the interface that
all Digest:: modules should provide.

%prep
%setup -q -n Digest-%{version}

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
%{site_perl}/Digest.pm
%{site_perl}/Digest/*
%{site_perl_arch}/
%{perl_prefix}/man/man3/*
