%include perl-header.spec

Summary: Perl date parser
Name: perl-module-TimeDate
Version: 1.16
Release: 4
Group: System Environment/Base
Copyright: GPL/Artistic
Source: TimeDate-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module parses absolute date strings.

%prep
%setup -q -n TimeDate-%{version}

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
%doc README
%{site_perl_arch}/auto/TimeDate
%{site_perl}/Time/*
%{site_perl}/Date/*
%{perl_prefix}/man/man3/*

%changelog
* Thu Aug 16 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.16-4
- Updated to newest version
