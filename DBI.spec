%include perl-header.spec

Summary: Database interface module for Perl
Name: perl-module-DBI
Version: 1.30
Release: 1ru
Group: System Environment/Base
Copyright: GPL/Artistic
Source: DBI-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
The DBI is a database access module for the Perl programming language.
It defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database
being used.


%prep
%setup -q -n DBI-%{version}

%build
%{perl_binary} Makefile.PL
PATH="/opt/SUNWspro/bin:$PATH"
export PATH
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/auto/DBI
%{site_perl_arch}/DBI
%{site_perl_arch}/DBD
%{site_perl_arch}/DBI.pm
#%{site_perl_arch}/Win32/*
%{site_perl_arch}/Bundle/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/bin/*
