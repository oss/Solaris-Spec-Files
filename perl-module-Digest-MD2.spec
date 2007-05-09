%include perl-header.spec

Summary: Digest-MD2
Name: perl-module-DigestMD2
Version: 2.03
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Digest-MD2-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Digest-MD2

%prep
%setup -q -n Digest-MD2-%{version}

%build
%{perl_binary} Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%{perl_prefix}/man/man3/*
%{site_perl_arch}
