%include perl-header.spec

Summary: High-resolution time, sleep, and alarm
Name: perl-module-Time-HiRes
Version: 1.20
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Time-HiRes-0%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Time-HiRes implements usleep, ualarm, and gettimeofday for Perl, as
well as wrappers for time, sleep, and alarm that know about
non-integral numbers.

%prep
%setup -q -n Time-HiRes-0%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/auto/Time/HiRes
%{site_perl_arch}/Time/HiRes.pm
%{perl_prefix}/man/man3/*
