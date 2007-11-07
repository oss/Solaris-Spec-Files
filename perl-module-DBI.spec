%include perl-header.spec

Summary: DBI

Name:		perl-module-DBI
Version:	1.601
Release:	1
Group:		System Environment/Base
Copyright:	GPL/Artistic
Source:		DBI-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
BuildRequires:	perl = %{perl_version}

%description
DBI

%prep

%setup -q -n DBI-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

perl Makefile.PL
make
#make test

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
/usr/perl5/bin/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.601-1
- Updated to latest version (1.601).

