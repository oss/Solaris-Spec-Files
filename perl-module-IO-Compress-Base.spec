%include perl-header.spec

Summary: 	IO-Compress-Base perl module
Name: 		perl-module-IO-Compress-Base
Version: 	2.008
Release: 	1
Group: 		System Environment/Base
Copyright: 	Unknown
Source: 	IO-Compress-Base-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -q -n IO-Compress-Base-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LIBXML_LIBS="-lxml2"
export PATH CC CXX CPPFLAGS LD LDFLAGS LIBXML_LIBS

perl Makefile.PL
gmake
gmake test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
rm %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/File
%{site_perl}/IO
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

%changelog
* Fri Jan 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.008-1
- Updated to latest version
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.006-1
- Upgraded to the latest version (2.006).

