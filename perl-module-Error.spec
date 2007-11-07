%include perl-header.spec

Summary: 	Error
Name: 		perl-module-Error
Version: 	0.17009
Release: 	1
Group: 		System Environment/Base
Copyright: 	Unknown
Source: 	Error-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
This perl module implements Error

%prep
%setup -q -n Error-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

%{perl_binary} Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%{perl_prefix}/man/man3/*
%{site_perl_arch}
%{site_perl}/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.17009-1
- Updated to latest version (0.17009).

