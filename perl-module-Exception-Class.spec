%include perl-header.spec

Summary: 	This module allows you to declare hierarchies of exception classes for use in your code.
Name: 		perl-module-Exception-Class
Version: 	1.23
Release: 	1
Group: 		System Environment/Base
Copyright:	GPL/Artistic
Source: 	Exception-Class-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl
BuildRequires: 	perl
Requires: 	perl-module-Class-Data-Inheritable
Requires: 	perl-module-Devel-StackTrace

%description
This module allows you to declare hierarchies of exception classes for
use in your code.  It also provides a simple exception class that it
uses as the default base class for all other exceptions.

You may choose to use another base class for your exceptions.
Regardless, the ability to declare all your exceptions at compile time
is a fairly useful trick and helps push people towards more structured
use of exceptions.


%prep

%setup -q -n Exception-Class-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CFLAGS="-D__unix__" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS  CFLAGS

perl Makefile.PL
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Exception/Class.pm
%{site_perl_arch}/auto/Exception/Class
%{perl_prefix}/man/man3/*

%changelog
* Mon Jan 14 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.23-1
- Updated to the latest version 1.23.
