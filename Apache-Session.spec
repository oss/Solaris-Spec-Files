%include perl-header.spec

Summary: Apache-Session

Name: perl-module-Apache-Session
Version: 1.54
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Apache-Session-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description


%prep

%setup -q -n Apache-Session-%{version}

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
%doc README Changes
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
