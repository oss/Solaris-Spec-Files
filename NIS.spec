%include perl-header.spec

Summary: NIS interface for Perl
Name: perl-module-NIS
Version: a2
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: NIS-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This is a snapshot release of the NIS interface to Perl 5.  There are two
parts to the interface: the raw component (Net::NIS), and the
object-oriented component (Net::NIS::Table).

The NIS interface only implements the NIS API, so there is no write
access to the NIS databases.

%prep
%setup -q -n NIS-%{version}

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
%doc README
%{site_perl_arch}/auto/Net/NIS
%{site_perl_arch}/Net/*.pod
%{site_perl_arch}/Net/NIS.pm
%{site_perl_arch}/Net/NIS
%{perl_prefix}/man/man3/*
