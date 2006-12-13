%include perl-header.spec
%define cvsdate 20030725
Summary: RATS encryption module
Name: perl-module-RATSdes
Version: 0.%{cvsdate}
Release: 4
Group: System Environment/Base
Copyright: Rutgers University
Source: RATSdes-%{cvsdate}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: openssl >= 0.9.8
BuildRequires: perl = %{perl_version}
BuildRequires: openssl >= 0.9.8

%description

%prep
%setup -q -n RATSdes

%build
# Changed as per arichton's sherlockery
#export PATH=$PATH:/usr/bin:/usr/ccs/bin:/usr/local/gnu/bin:/opt/SUNWspro/bin
perl Makefile.PL CCFLAGS="-DOPENSSL_DES_LIBDES_COMPATIBILITY" CC="/opt/SUNWspro/bin/cc"
make clean
perl Makefile.PL CCFLAGS="-DOPENSSL_DES_LIBDES_COMPATIBILITY" CC="/opt/SUNWspro/bin/cc"
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
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/*/*
