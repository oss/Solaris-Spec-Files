%include perl-header.spec

Summary: HTML-Parser

Name: perl-module-HTML-Parser
Version: 3.28
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Parser-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
HTML-Parser

%prep

%setup -q -n HTML-Parser-%{version}

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
