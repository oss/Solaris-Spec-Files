%include perl-header.spec

Summary: ArchiveZip perl module
Name: perl-module-ArchiveZip
Version: 1.05
Release: 0
Group: System Environment/Base
Copyright: Unknown
Source: Archive-Zip-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Archive::Zip etc.

%prep

%setup -n Archive-Zip-%{version}

%build
perl Makefile.PL
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
%doc README Changes
%{site_perl}/*
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/bin/crc32
