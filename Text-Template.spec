%include perl-header.spec

Summary: Text-Template

Name: perl-module-Text-Template
Version: 1.43
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Text-Template-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Text-Template

%prep

%setup -q -n Text-Template-%{version}

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
%doc README
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
