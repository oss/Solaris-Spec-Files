%include perl-header.spec

Summary:	Convert UUlib perl module
Name:		perl-module-Convert-UUlib
Version:	1.09
Release:	1
Group:		System Environment/Base
Copyright:	GPL
Source:		Convert-UUlib-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
BuildRequires:	perl = %{perl_version}

%description
Yet another allegedly useful module from CPAN.

%prep

%setup -n Convert-UUlib-%{version}

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
