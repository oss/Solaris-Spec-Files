%include perl-header.spec

Summary: Helps parse HTML
Name: perl-module-HTML-Tagset
Version: 3.03
Release: 1
Group: System Enviroment/Base
Copyright: GPL
Source: HTML-Tagset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl
BuildRequires: perl

%description
This module contains data tables useful in dealing with HTML.

It provides no functions or methods.

%prep

%setup -q -n HTML-Tagset-%{version}

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
%{site_perl}/HTML/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

