%include perl-header.spec

Summary: Perl profiler
Name: perl-module-DProf
Version: 19990108
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: DProf-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This perl modules lets you profile the execution of a perl script.

%prep
%setup -q -n DProf-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes Todo
%{site_perl_arch}/Devel/DProf.pm
%{site_perl_arch}/auto/Devel/DProf
%{perl_prefix}/bin/*
%{perl_prefix}/man/*/*
