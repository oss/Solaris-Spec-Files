%include perl-header.spec

Summary: Perl API for WWW programming
Name: perl-module-libwww
Version: 5.48
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: libwww-perl-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: perl-module-libnet
Requires: perl-module-URI
# Requires: perl-module-Mime-Base64
Requires: perl-module-HTML-Parser
Requires: perl-module-Digest-MD5
BuildRequires: perl = %{perl_version}
BuildRequires: perl-module-libnet
BuildRequires: perl-module-URI
# BuildRequires: perl-module-Mime-Base64
BuildRequires: perl-module-HTML-Parser
BuildRequires: perl-module-Digest-MD5

%description
Libwww-perl is a collection of Perl modules which provides a simple
and consistent application programming interface (API) to the
World-Wide Web.  T he main focus of the library is to provide classes
and functions that allow you to write WWW clients, thus libwww-perl
said to be a WWW client library. The library also contain modules that
are of more general use and even classes that help you implement
simple HTTP servers.

%prep
%setup -q -n libwww-perl-%{version}

%build
/bin/echo "\n" | perl Makefile.PL
make
# make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README ChangeLog
%{site_perl_arch}/auto/libwww-perl/.packlist
%{site_perl}/*pm
%{site_perl}/*pod
%{site_perl}/HTML/*
%{site_perl}/WWW/*
%{site_perl}/HTTP/*
%{site_perl}/Bundle/*
%{site_perl}/LWP/*
%{site_perl}/File/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/bin/*
