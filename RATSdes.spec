%include perl-header.spec
%define cvsdate 20030725
Summary: RATS encryption module
Name: perl-module-RATSdes
Version: 0.%{cvsdate}
Release: 3
Group: System Environment/Base
Copyright: Rutgers University
Source: RATSdes-%{cvsdate}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: openssl
BuildRequires: perl = %{perl_version}
BuildRequires: openssl

%description

%prep
%setup -q -n RATSdes

%build
# Changed as per arichton's sherlockery

perl Makefile.PL CCFLAGS="-DOPENSSL_DES_LIBDES_COMPATIBILITY"
gmake
gmake test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/*/*
