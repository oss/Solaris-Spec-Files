%include perl-header.spec

Summary: Mail-SPF
Name: perl-module-Mail-SPF
Version: 2.004
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Mail-SPF-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements Mail-SPF

%prep
%setup -q -n Mail-SPF-%{version}

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