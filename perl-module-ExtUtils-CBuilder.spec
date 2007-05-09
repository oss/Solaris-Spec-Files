%include perl-header.spec

Summary: ExtUtils-CBuilder
Name: perl-module-ExtUtils-CBuilder
Version: 0.18_01
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: ExtUtils-CBuilder-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements ExtUtils-CBuilder

%prep
%setup -q -n ExtUtils-CBuilder-%{version}

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
%{site_perl}/ExtUtils
