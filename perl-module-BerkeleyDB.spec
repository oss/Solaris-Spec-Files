%include perl-header.spec
%define dbversion 4.8
%define dbversion_minor .30


Summary: 	Perl interface to BerkeleyDB
Name: 		perl-module-BerkeleyDB
Version: 	0.36
Release: 	4
Group: 		System Environment/Base
License: 	GPL/Artistic
Source: 	BerkeleyDB-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	perl = %{perl_version}
Requires: 	db4 >= %{dbversion}%{dbversion_minor}
BuildRequires: 	db4-devel >= %{dbversion}%{dbversion_minor}
BuildRequires: 	perl = %{perl_version}

%description

%prep
%setup -q -n BerkeleyDB-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" \
CCFLAGS="-g -xO2 -I/usr/local/include" \
CPPFLAGS="-g -xO2 -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CCFLAGS CPPFLAGS LD LDFLAGS

rm config.in
echo "INCLUDE = /usr/local/include/db4" >> config.in
echo "LIB = /usr/local/lib" >> config.in
echo "DBNAME = -ldb-%{dbversion}" >> config.in
%{perl_binary} Makefile.PL 
gmake CCFLAGS="-g -xO2 -I/usr/local/include"

%check
gmake test

%install
rm -rf %{buildroot}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%doc README Changes
%{site_perl_arch}/auto/BerkeleyDB/*
%{site_perl_arch}/auto/BerkeleyDB/.packlist
%{site_perl_arch}/BerkeleyDB.pm
%{site_perl_arch}/BerkeleyDB.pod
%{site_perl_arch}/BerkeleyDB
%{perl_prefix}/man/man*/*

%changelog
* Fri Aug 20 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.36-4
- Require db4 with full version
* Fri Aug 20 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.36-3
- Respin against db4-4.8.30
* Fri Jan 08 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 0.36-2
- Respin against BDB 4.8
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.36-1
- Built against BDB 4.7 and updated to version 0.36
* Thu May 29 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.34-1
- Updated to 0.34
* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.32-1
- Updated to 0.32

