%include perl-header.spec

Summary: 	Unix Syslog perl module
Name: 		perl-module-Unix-Syslog
Version: 	1.0
Release: 	1
Group: 		System Environment/Base
Copyright: 	Unknown
Source: 	Unix-Syslog-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -q -n Unix-Syslog-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

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
%doc README Changes
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0-1
- Updated to latest version (1.0).

