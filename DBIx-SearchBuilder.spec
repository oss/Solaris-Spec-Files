%include perl-header.spec

Summary: DBIx-SearchBuilder

Name: perl-module-DBIx-SearchBuilder
Version: 0.80
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: DBIx-SearchBuilder-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
DBIx-SearchBuilder

%prep

%setup -q -n DBIx-SearchBuilder-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
