%include perl-header.spec

Summary: Copy files specified by URI
Name: perl-module-WebFS-FileCopy
Version: 1.04
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: WebFS-FileCopy-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: perl-module-URI >= 1.09
Requires: perl-module-libnet
Requires: perl-module-LWPng-alpha
BuildRequires: perl = %{perl_version}
BuildRequires: perl-module-URI >= 1.09
BuildRequires: perl-module-libnet
BuildRequires: perl-module-LWPng-alpha

%description
This is the WebFS::FileCopy package.  This module provides subroutines
for the getting, putting, copying, moving and deleting of files
located by URIs.  It also supports listing directories identified by
URI.  Currently, files for getting can use any URI protocol, such as
file, FTP, HTTP, etc.  For putting, only the file and FTP protocols
are currently supported.
   (from README)

%prep
%setup -q -n WebFS-FileCopy-%{version}

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
%doc README CHANGES
%{site_perl_arch}/auto/WebFS/FileCopy
%{site_perl}/WebFS/*
%{perl_prefix}/man/*/*
