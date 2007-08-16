%include perl-header.spec

Summary: Net Server perl module
Name: perl-module-Net-Server
Version: 0.97
Release: 2
Group: System Environment/Base
Copyright: Unknown
Source: Net-Server-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Net-Server-%{version}

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

%changelog
* Thu Aug 16 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.97-2
- Updated to newest version.

