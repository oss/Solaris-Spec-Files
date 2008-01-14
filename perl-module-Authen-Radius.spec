%include perl-header.spec

Summary: 	Radius authentication support for perl
Name: 		perl-module-Authen-Radius
Version: 	0.13
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	RadiusPerl-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
This perl module helps you write CGI scripts for web servers.

%prep
%setup -q -n Authen-Radius-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS  CFLAGS

perl Makefile.PL
gmake
# make test is interactive

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

umask 022
mkdir -p %{buildroot}%{site_perl_arch}/Authen

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/auto/Authen/Radius
/usr/perl5/man/man3/Authen::Radius.3
/usr/perl5/site_perl/5.6.1/Authen/Radius.pm


%changelog
* Mon Jan 14 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.13-1
- Updated to the latest version 0.13.
