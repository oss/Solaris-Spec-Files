%include perl-header.spec

Summary: WWW::Mechanize

Name: perl-module-WWW-Mechanize
Version: 0.40
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: WWW-Mechanize-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
WWW::Mechanize

%prep

%setup -q -n WWW-Mechanize-%{version}

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
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*
