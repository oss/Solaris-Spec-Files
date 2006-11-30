%include perl-header.spec

Summary: ArchiveTar perl module
Name: perl-module-ArchiveTar
Version: 1.30
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Archive-Tar-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-IO-String >= 1.08, perl-module-IO-Zlib >= 1.04, perl-module-Test-Harness >= 2.64
BuildRequires: perl = %{perl_version}, perl-module-IO-String >= 1.08, perl-module-IO-Zlib >= 1.04, perl-module-Test-Harness >= 2.64, perl-module-ExtUtils-MakeMaker >= 6.31

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
%doc README
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/bin/*
%{perl_prefix}/man/*

