%include perl-header.spec

Summary: Radius authentication support for perl
Name: perl-module-Authen-Radius
Version: 0.05
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: RadiusPerl-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl module helps you write CGI scripts for web servers.

%prep
%setup -q -n RadiusPerl-%{version}

%build
perl Makefile.PL
make
# make test is interactive

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

umask 022
mkdir -p %{buildroot}%{site_perl_arch}/Authen
install -m 0644 Authen/Radius.pm \
    %{buildroot}%{site_perl_arch}/Authen/Radius.pm

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/Authen/Radius.pm
%{site_perl_arch}/auto/Authen/Radius
