%include perl-header.spec

Summary: Interpolate and search lists
Name: perl-module-Math-Interpolate
Version: 1.05
Release: 1
Group: System Enviroment/Base
Copyright: GPL
Source: Math-Interpolate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl
BuildRequires: perl

%description
This is the Math::Interpolate package.  This module contains several
useful routines for interpolating data sets and finding where a given
value lies in a sorted list.

%prep
%setup -q -n Math-Interpolate-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{site_perl}/Math/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

