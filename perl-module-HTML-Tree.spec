%include perl-header.spec

Summary: 	HTML-Tree
Name: 		perl-module-HTML-Tree
Version: 	3.23
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	HTML-Tree-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl
BuildRequires: 	perl
Provides: 	perl-module-HTML-Element
Provides: 	perl-module-HTML-TreeBuilder

%description
This distribution contains a suite of modules for representing,
creating, and extracting information from HTML syntax trees; there is
also relevent documentation.  These modules used to be part of the
libwww-perl distribution, but are now unbundled in order to facilitate
a separate development track.  Bug reports and discussions about these
modules can still be sent to the <libwww@perl.org> mailing list, or to
<sburke@cpan.org>.

%prep

%setup -q -n HTML-Tree-%{version}

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
%{site_perl}/HTML/*
%{site_perl_arch}/auto/HTML-Tree
%{perl_prefix}/man/man3/*

%changelog
* Mon Jan 14 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 3.23-1
- Updated to the latest version 3.23.
