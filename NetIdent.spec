%include perl-header.spec

Summary: Ident client
Name: perl-module-Net-Ident
Version: 1.20
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Net-Ident-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Net::Ident is a module that looks up the username on the remote side
of a TCP/IP connection through the ident (auth/tap) protocol described
in RFC1413 (which supersedes RFC931). Note that this requires the
remote site to run a daemon (often called identd) to provide the
requested information, so it is not always available for all TCP/IP
connections.

%prep
%setup -q -n Net-Ident-%{version}

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
%{site_perl}/Net/*
%{site_perl_arch}/auto/Net/Ident
%{perl_prefix}/man/man3/*
