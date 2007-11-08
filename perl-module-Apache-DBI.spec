%include perl-header.spec

Summary: 	This is version 0.91 of Apache::AuthDBI and Apache::DBI.
Name: 		perl-module-Apache-DBI
Version: 	1.06
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	Apache-DBI-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl
BuildRequires: 	perl

%description
These modules are supposed to be used with the Apache server together with 
an embedded perl interpreter like mod_perl. They provide support for basic 
authentication and authorization as well as support for persistent database 
connections via Perl's Database Independent Interface (DBI). 

%prep

%setup -q -n Apache-DBI-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

perl Makefile.PL
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes traces.txt eg
%{site_perl}/Apache/*
%{site_perl_arch}/auto/Apache/DBI
%{perl_prefix}/man/man3/*

%changelog
* Thu Nov 8 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.06-1
- Updated to latest version (1.06).
