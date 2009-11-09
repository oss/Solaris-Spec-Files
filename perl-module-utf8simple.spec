#%define perl_version=5.6.1
%include perl-header.spec
Summary: Module providing utf8 functions for perl < 5.8
Name: perl-module-utf8simple
Version: 1.06
Release: 1
Group: System Environment/Base
License: apache
Source: utf8simple-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Versions of perl before 5.8 had very limited support for utf8 functions.
This is a plugin backporting some of the most commonly used ones.

%prep
%setup -q -n Unicode-UTF8simple-1.06

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
%{perl_prefix}/man/man3/*
%{site_perl}/*
#%{global_perl_arch}/perllocal.pod

%post

%changelog
* Mon Nov 09 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 1.06-1
 - Initial Build
