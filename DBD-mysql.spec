%include perl-header.spec

Summary: DBD-mysql

Name: perl-module-DBD-mysql
Version: 2.1026
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: DBD-mysql-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
DBD-mysql

%prep

%setup -q -n DBD-mysql-%{version}

%build
perl Makefile.PL --cflags=-I/usr/local/mysql/include/mysql --libs=-L/usr/local/mysql/lib/mysql 
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
