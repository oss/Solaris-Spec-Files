%include perl-header.spec

Summary: Regexp::Common

Name: perl-module-Regexp-Common
Version: 2.113
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Regexp-Common-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Regexp::COmmon

%prep

%setup -q -n Regexp-Common-%{version}

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
