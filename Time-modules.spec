%include perl-header.spec

Summary: Time-modules
Name: perl-module-Time-modules
Version: 2003.0211
Release: 5
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Time-modules-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
%if %{which_perl} == "REPOSITORY"
Requires: perl-module-ExtUtils-MakeMaker
BuildRequires: perl-module-ExtUtils-MakeMaker
%endif
Provides: perl-module-Time-CTime
Provides: perl-module-Time-DaysInMonth
Provides: perl-module-Time-JulianDay
Provides: perl-module-Time-ParseDate
Provides: perl-module-Time-Timezone
Obsoletes: perl-module

%description
This package has all this bunch of fun modules:
Time::CTime
Time::DaysInMonth
Time::JulianDay
Time::Parsedate
Time::Timezone

%prep

%setup -q -n Time-modules-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README CHANGELOG
%{site_perl}/Time/*
%{site_perl_arch}/auto/Time-modules
%{perl_prefix}/man/man3/*
