%include perl-header.spec

Summary: CGI module
Name: perl-module-CGI
Version: 2.76
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: CGI.pm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module helps you write CGI scripts for web servers.

%prep
%setup -q -n CGI.pm-%{version}

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
%doc README Changes cgi-lib_porting.html ANNOUNCE
%doc examples/*
%{global_perl_arch}/auto/CGI
%{global_perl}/CGI/*
%{perl_prefix}/man/*/*
