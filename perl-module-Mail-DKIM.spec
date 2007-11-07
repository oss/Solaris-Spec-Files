%include perl-header.spec

Summary:	Mail-DKIM
Name: 		perl-module-Mail-DKIM
Version: 	0.28
Release: 	1
Group: 		System Environment/Base
Copyright: 	Unknown
Source: 	Mail-DKIM-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version} perl-module-Digest-SHA perl-module-Error
BuildRequires: 	perl = %{perl_version} perl-module-Digest-SHA perl-module-Error

%description
This perl module implements Mail-DKIM

%prep
%setup -q -n Mail-DKIM-%{version}

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
%{site_perl}/Mail

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.28-1
- Upgraded to the latest version (0.28).

