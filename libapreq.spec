%include perl-header.spec

Summary: Generic Apache Request Library

Name: perl-module-libapreq
Version: 1.2
Release: 4
Group: System Environment/Base
Copyright: GPL/Artistic
Source: libapreq-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
Requires: mod_perl
BuildRequires: perl

Requires: perl-module-Apache-Test

Provides: perl-module-Apache-Request
Provides: perl-module-Apache-Cookie

%description
libapreq - Generic Apache Request Library
http://httpd.apache.org/apreq/

This package contains modules for manipulating client request data via
the Apache API with Perl and C.  Functionality includes:

 - parsing of application/x-www-form-urlencoded data
 - parsing of multipart/form-data 
 - parsing of HTTP Cookies

See libapreq.pod for the C API documentation and
eg/c/ for examples.


%prep

%setup -q -n libapreq-%{version}

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
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/Apache/*
%{site_perl_arch}/auto/Apache
%{site_perl_arch}/auto/libapreq
%{perl_prefix}/man/man3/*
