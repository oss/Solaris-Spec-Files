%include perl-header.spec

Summary: Perl interface to filesystem quotas
Name: perl-module-Quota
Version: 1.5.1
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Quota-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
The Quota module provides access to file system quotas.  The quotactl
system call or ioctl is used to query or set quotas on the local host,
or queries are submitted via RPC to a remote host.  Mount tables can
be parsed with getmntent and paths can be translated to device files
(or whatever the actual quotactl implementations needs as argument) of
the according file system.
  (from the man page)


%prep
%setup -q -n Quota-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS
perl Makefile.PL
make
# make test is interactive

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc contrib
%doc README CHANGES
%{site_perl_arch}/auto/Quota
%{site_perl_arch}/Quota.pm
%{perl_prefix}/man/*/*

%changelog
* Thu Aug 16 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.51-3
- Updated to newest version.

