%include perl-header.spec

Summary: File-Spec

Name: perl-module-File-Spec
Version: 0.82
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: File-Spec-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
File-Spec

%prep

%setup -q -n File-Spec-%{version}

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
%doc README CHANGES
%{perl_prefix}/*
