%include perl-header.spec

Summary: MailTools
Name: perl-module-MailTools
Version: 1.77
Release: 2
Group: System Environment/Base
Copyright: Unknown
Source: MailTools-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module implements MailTools

%prep
%setup -q -n MailTools-%{version}

%build
%{perl_binary} Makefile.PL
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
%doc README
#%{site_perl_arch}/../*/*
#%{site_perl_arch}/auto/Crypt/CBC
#%{perl_prefix}/man/*/*
#%{site_perl_arch}
%{site_perl}/Mail/*
%{site_perl}/auto/Mail/*
%{perl_prefix}/man/man3/*
%{site_perl_arch}/auto/Mail/.packlist

%changelog
* Thu Aug 16 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.77-2
- Updated to newest version.

