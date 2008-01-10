%include perl-header.spec

Summary: get pathname of current working directory
Name: perl-module-Cwd
Version: 2.21
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Cwd-%{version}.tar.gz
Packager: David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module provides functions for determining the pathname of the current working directory. It is recommended that getcwd (or another *cwd() function) be used in all code to ensure portability.

%prep
%setup -q -n Cwd-%{version} 

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS
perl Makefile.PL
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
cd %{buildroot}
rm usr/perl5/5.6.1/lib/sun4-solaris-64int/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%{global_perl_arch}/auto/Cwd
%{global_perl_arch}/Cwd.pm
%{perl_prefix}/man/man3/*

%changelog
* Thu Jan 10 2008 David Diffenbaugh <davediff@nbcs.rutger.edu> - 2.21-1
- Updated to latest Version
* Thu Jan 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.06-1 
- First Rutgers Release
