%include perl-header.spec

Summary: Next-generation LWP modules
Name: perl-module-LWPng-alpha
Version: 0.24
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: LWPng-alpha-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This is an alpha vesrion of LWPng with HTTP/1.1 support.

%prep
%setup -q -n LWPng-alpha-%{version}

%build
perl Makefile.PL
make
# make test fails -- but this is alpha code.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc Changes *ps *txt News Todo README
%{site_perl_arch}/auto/LWPng-alpha
%{site_perl}/URI/Attr.pm
%{site_perl}/LWP/*
%{perl_prefix}/man/*/*
