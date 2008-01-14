%include perl-header.spec

Summary:	version
Name:		perl-module-version
Version:	0.74
Release:	1
Group:		System Environment/Base
Copyright:	Unknown
Source: 	version-%{version}.tar.gz
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
BuildRequires:	perl = %{perl_version}

%description
This perl module implements version

%prep
%setup -q -n version-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS 
%{perl_binary} Makefile.PL
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_pure_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%{perl_prefix}/man/man3/*
%{site_perl_arch}

%changelog
* Mon Jan 14 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.74-1
- Updated to latest version (0.74)
