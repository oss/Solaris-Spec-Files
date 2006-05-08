%include perl-header.spec
%define module_name Sys-Hostname-Long
 
Summary: Try every conceivable way to get full hostname
Name: perl-module-%{module_name}
Version: 1.4
Release: 3
Group: System Environments/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~scott/%{module_name}-%{version}/lib/Sys/Hostname/Long.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}, perl-module-Test-Simple

%description
How to get the host full name in perl on multiple operating systems (mac,
windows, unix* etc)

%prep
%setup -qn %{module_name}-%{version}

%build
%{perl_binary} Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-, bin, bin)
%doc Changes README
%{site_perl}/Sys/*
%{site_perl_arch}/auto/*
%{perl_prefix}/man/man3/*

%changelog
* Thu Apr 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4-3
- Added perl-module-Test-Simple to BuildRequires.
* Wed Apr 19 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.4-1
