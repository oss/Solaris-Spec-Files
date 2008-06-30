%include perl-header.spec

Summary: 	Allows you to declare hierarchies of exception classes for use in your code.
Name: 		perl-module-Exception-Class
Version: 	1.24
Release: 	1
Group: 		System Environment/Base
Copyright:	GPL/Artistic
Source: 	Exception-Class-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl
BuildRequires: 	perl, perl-module-Module-Build

Requires: perl-module-Scalar-List-Util
BuildRequires: perl-module-Scalar-List-Util

Requires: perl-module-Devel-StackTrace
BuildRequires: perl-module-Devel-StackTrace

Requires: perl-module-Test-Simple
BuildRequires: perl-module-Test-Simple

Requires: perl-module-Class-Data-Inheritable
BuildRequires: perl-module-Class-Data-Inheritable

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

%{pbuild}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pbuild_install}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc Changes LICENSE
%{site_perl}/Exception/Class.pm
%{site_perl_arch}/auto/Exception/Class
%{global_perl}/man/man3/*

%changelog
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.24-1
- Added some requirements, updated to version 1.24
* Mon Jan 14 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.23-1
- Updated to the latest version 1.23.
