%include perl-header.spec

Summary: CGI modules for Perl
Name: perl-module-CGI-modules
Version: 2.76
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: CGI-modules-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl-module-libwww
Requires: perl-module-libwww
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
These are the CGI::* modules for use in perl scripts.

%prep
%setup -q -n CGI-modules-%{version}

%build
perl Makefile.PL
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
%doc doc/*
%{site_perl_arch}/auto/CGI
%{site_perl}/CGI/*
%{perl_prefix}/man/*/*
