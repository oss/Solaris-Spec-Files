%include perl-header.spec

Summary: 	IO-Compress-Zlib perl module
Name: 		perl-module-IO-Compress-Zlib
Version: 	2.006
Release: 	1
Group: 		System Environment/Base
Copyright: 	Unknown
Source: 	IO-Compress-Zlib-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -qn IO-Compress-Zlib-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LIBXML_LIBS="-lxml2"
export PATH CC CXX CPPFLAGS LD LDFLAGS LIBXML_LIBS

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
%{site_perl}/IO
%{site_perl_arch}/*
%{perl_prefix}/man/man3/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.006-1
- Upgraded to the latest version (2.006).

