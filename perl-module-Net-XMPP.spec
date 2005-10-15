%include perl-header.spec

Summary: Net XMPP perl module
Name: perl-module-Net-XMPP
Version: 1.0
Release: 1
Group: System Environments/Base
License: LGPL
Source: Net-XMPP-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-XML-Stream, perl-module-Digest-SHA1, perl-module-Authen-SASL
BuildRequires: perl = %{perl_version}, perl-module-XML-Stream, perl-module-Digest-SHA1, perl-module-Authen-SASL

%description
Net::XMPP is a collection of Perl modules that provide a Perl Developer
access to the XMPP protocol.  Using OOP modules we provide a clean
interface to writing anything from a full client to a simple protocol
tester.

%prep

%setup -qn Net-XMPP-%{version}

%build
perl Makefile.PL
make
make test

%install
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm $RPM_BUILD_ROOT%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%{site_perl}/*
%{perl_prefix}/man/man3/*
