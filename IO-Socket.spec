%include perl-header.spec

#IO-Socket-SSL-0.94.tar.gz

Summary: IO::Socket::SSL - Nearly transparent SSL encapsulation for IO::Socket::INET.

Name: perl-module-IO-Socket-SSL
Version: 0.94
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: IO-Socket-SSL-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl
Requires: perl

Requires: perl-module-Net-SSLeay
BuildRequires: perl-module-Net-SSLeay

%description
   This module is a true drop-in replacement for IO::Socket::INET that uses SSL to encrypt
   data before it is transferred to a remote server or client. IO::Socket::SSL supports all
   the extra features that one needs to write a full-featured SSL client or server
   application: multiple SSL contexts, cipher selection, certificate verification, and SSL
   version selection. As an extra bonus, it works perfectly with mod_perl.

   If you have never used SSL before, you should read the appendix labelled 'Using SSL'
   before attempting to use this module.

   If you have used this module before, read on, as versions 0.93 and above have several
   changes from the previous IO::Socket::SSL versions (especially see the note about return
   values).

%prep

%setup -q -n IO-Socket-SSL-%{version}

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
%{site_perl}/IO/Socket/SSL.pm
%{site_perl_arch}/auto/IO/Socket/SSL
%{perl_prefix}/man/man3/*
