%include perl-header.spec

Summary: Time-modules
Name: perl-module-Time-modules
Version: 2003.0211
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Time-modules-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Time::Parsedate and other classics

%prep

%setup -q -n Time-modules-%{version}

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
%doc README CHANGELOG
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
