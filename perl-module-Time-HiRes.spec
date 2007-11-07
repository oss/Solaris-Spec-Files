%include perl-header.spec

Summary: 	Time::HiRes
Name: 		perl-module-Time-HiRes
Version: 	1.9708
Release: 	1
Group:		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	Time-HiRes-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
Perl module Time::HiRes

%prep

%setup -q -n Time-HiRes-%{version}

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
rm $RPM_BUILD_ROOT%{perl_prefix}/%{perl_version}/lib/sun4-solaris-64int/perllocal.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)

%{perl_prefix}/man/man3/Time::HiRes.3
%{site_perl_arch}/auto/Time/
%{site_perl_arch}/Time/HiRes.pm

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.9708-1
- Updated to latest version (1.9708).

