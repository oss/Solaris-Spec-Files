%include perl-header.spec

Summary: Perl support for the SNMP protocol
Name: perl-module-Net-SNMP
Version: 3.60
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Net-SNMP-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
The module Net::SNMP implements an object oriented interface to the
Simple Network Management Protocol.  Perl applications can use the
module to retrieve or update information on a remote host using the
SNMP protocol.  Net::SNMP is implemented completely in Perl, requires
no compiling, and uses only standard Perl modules.  Both SNMPv1 and
SNMPv2c (Community-Based SNMPv2) are supported by the module.  The
Net::SNMP module assumes that the user has a basic understanding of
the Simple Network Management Protocol and related network management
concepts.
  (from the manpage)

%prep
%setup -q -n Net-SNMP-3.6

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc Changes examples/* README
%{site_perl_arch}/auto/Net/SNMP
%{site_perl}/Net/SNMP.pm
%{perl_prefix}/man/*/*
