%include perl-header.spec

Summary: Test::Inline

Name: perl-module-Test-Inline
Version: 0.15
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Test-Inline-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Test::Inline

%prep

%setup -q -n Test-Inline-%{version}

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
%{perl_prefix}/*
