%include perl-header.spec

Summary: Perl interfaces to common network protocols
Name: perl-module-libnet
Version: 1.0703
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: libnet-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
libnet is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the client side of various
protocols used in the internet community.

For details of each protocol please refer to the RFC. RFC's can be
found a various places on the WEB, for a staring point look at:

    http://www.yahoo.com/Computers_and_Internet/Standards/RFCs/

The RFC implemented in this distribution are

Net::FTP        RFC959          File Transfer Protocol
Net::SMTP       RFC821          Simple Mail Transfer Protocol
Net::Time       RFC867          Daytime Protocol
Net::Time       RFC868          Time Protocol
Net::NNTP       RFC977          Network News Transfer Protocol
Net::POP3       RFC1939         Post Office Protocol 3
Net::SNPP       RFC1861         Simple Network Pager Protocol

The distribution also contains a module (Net::PH) which facilitates
comunicate with with servers using the CCSO Nameserver Server-Client
Protocol.

%prep
%setup -q -n libnet-%{version}

%build
/bin/echo "\n" | perl Makefile.PL
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
%doc README ChangeLog
%{site_perl_arch}/auto/Net/.packlist
%{site_perl}/Net/*
%{perl_prefix}/man/man3/*
