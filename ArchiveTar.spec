%include perl-header.spec

Summary: ArchiveTar perl module
Name: perl-module-ArchiveTar
Version: 0.23
Release: 0
Group: System Environment/Base
Copyright: Unknown
Source: Archive-Tar-%{version}.tgz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Archive::Tar etc.

%prep

%setup -n Archive-Tar-%{version}

%build
perl Makefile.PL
make
# Needs Test::More from Perl 5.8, sorry
#make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/bin/ptar
%{perl_prefix}/man/man3/*

