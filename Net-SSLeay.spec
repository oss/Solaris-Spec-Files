%include perl-header.spec

Summary: Net::SSLeay - Perl extension for using OpenSSL or SSLeay

Name: perl-module-Net-SSLeay
Version: 1.23
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Net_SSLeay.pm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl
Requires: perl

Provides: perl-module-Net-SSLeay-Handle

%description
   There is a related module called Net::SSLeay::Handle included in this distribution that
   you might want to use instead. It has its own pod documentation.

   This module offers some high level convinience functions for accessing web pages on SSL
   servers, a sslcat() function for writing your own clients, and finally access to the SSL
   api of SSLeay/OpenSSL package so you can write servers or clients for more complicated
   applications.

   For high level functions it is most convinient to import them to your main namespace as
   indicated in the synopsis.


%prep

%setup -q -n Net_SSLeay.pm-%{version}

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
%doc README Changes test.html
%{site_perl_arch}/Net/*
%{site_perl_arch}/auto/Net/SSLeay*
%{perl_prefix}/man/man3/*
