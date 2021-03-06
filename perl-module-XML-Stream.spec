%include perl-header.spec

Summary: XML Stream perl module
Name: perl-module-XML-Stream
Version: 1.22
Release: 5
Group: System Environments/Base
License: LGPL
Source: XML-Stream-%{version}.tar.gz
Source1: XML-Stream-encode-compat.diff
BuildRoot: /var/tmp/%{name}-root
Requires: perl-module-Authen-SASL, perl-module-MIME-Base64, perl-module-IO-Socket-SSL, perl-module-Encode-compat
BuildRequires: perl-module-Authen-SASL, perl-module-MIME-Base64, perl-module-IO-Socket-SSL, perl-module-Encode-compat

%description
This module provides you with access to XML Streams.  An XML Stream
is just that.  A stream of XML over a connection between two computers.
For more information about XML Streams, and the group that created them,
please visit:

http://etherx.jabber.org/streams

%prep

%setup -qn XML-Stream-%{version}

%build
gpatch -p1 < %{SOURCE1}
perl Makefile.PL
make
# Needs some test modules we don't have that don't want to build cleanly.
#make test

%install
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm $RPM_BUILD_ROOT%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%{site_perl}/*
%{perl_prefix}/man/man3/*
