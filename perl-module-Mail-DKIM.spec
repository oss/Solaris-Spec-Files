%include perl-header.spec

Summary: Mail-DKIM
Name: perl-module-Mail-DKIM
Version: 0.24
Release: 1
Group: System Environment/Base
Copyright: Unknown
Source: Mail-DKIM-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version} perl-module-Digest-SHA perl-module-Error
BuildRequires: perl = %{perl_version} perl-module-Digest-SHA perl-module-Error

%description
This perl module implements Mail-DKIM

%prep
%setup -q -n Mail-DKIM-%{version}

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
%{site_perl}/Mail
