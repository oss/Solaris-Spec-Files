%include perl-header.spec

Summary: Perl NNTP client
Name: perl-module-NNTPClient
Version: 0.37
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: NNTPClient-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module implements a client interface to NNTP, enabling a Perl 5
application to talk to NNTP servers.  It uses the OOP (Object Oriented
Programming) interface introduced with Perl 5.
  (from README)

%prep
%setup -q -n NNTPClient-%{version}

%build
perl Makefile.PL
make
# make test contacts the news server

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%doc demos/*
%{site_perl_arch}/auto/News/NNTPClient
%{site_perl}/News/*
%{perl_prefix}/man/*/*

