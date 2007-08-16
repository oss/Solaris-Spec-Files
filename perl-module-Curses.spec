%include perl-header.spec

Summary:	Terminal screen handling and optimization.h 
Name:		perl-module-Curses
Version:	1.16 
Release:	1
Group:		System Environment/Base
Copyright:	GPL/Artistic
Source:		Curses-%{version}.tgz
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
BuildRequires:	perl = %{perl_version}

%description
This is a dynamic loadable curses module for perl.


%prep
%setup -q -n Curses-%{version}

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
%{site_perl_arch}/auto/*
%{site_perl_arch}/*pm
%{perl_prefix}/man/man3/*
