%include perl-header.spec

Summary: razor
Name: perl-module-razor
Version: 2.82
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: razor-agents-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements razor

%prep
%setup -q -n razor-agents-%{version}

%build
%{perl_binary} Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_pure_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%{perl_prefix}/man/man3/*
%{site_perl_arch}
