%include perl-header.spec

Summary: Version number sorter for Perl
Name: perl-module-SortVersions
Version: 1.1
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: SortVersions-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module allows easy sorting (via comparisons) of mixed text and numeric
strings, similar to the complex "version numbers" that many revision control
packages and shared library systems use. For an explanation of the
algorithm, it's easiest to look at these examples:

  1.1   <  1.2
  1.1a  <  1.2
  1.1   <  1.1.1
  1.1   <  1.1a
  1.1.a <  1.1a
  1     <  a
  a     <  b
  1     <  2
  1     <  0002
  1.5   <  1.06

  [ from the documentation ]

%prep
%setup -q -n SortVersions-%{version}

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
%{site_perl_arch}/auto/Sort/*
%{site_perl}/Sort/*
%{perl_prefix}/man/man3/*
