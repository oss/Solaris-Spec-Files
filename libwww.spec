%include perl-header.spec

Summary: Perl API for WWW programming
Name: perl-module-libwww
Version: 5.69
Release: 1
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

# The shit load of modules that this package provides
Provides: perl-module-Bundle-LWP
Provides: perl-module-File-Listing
Provides: perl-module-HTML-Form
Provides: perl-module-HTTP-Cookies
Provides: perl-module-HTTP-Cookies-Microsoft
Provides: perl-module-HTTP-Cookies-Netscape
Provides: perl-module-HTTP-Daemon
Provides: perl-module-HTTP-Date
Provides: perl-module-HTTP-Headers
Provides: perl-module-HTTP-Headers-Auth
Provides: perl-module-HTTP-Headers-ETag
Provides: perl-module-HTTP-Headers-Util
Provides: perl-module-HTTP-Message
Provides: perl-module-HTTP-Negotiate
Provides: perl-module-HTTP-Request
Provides: perl-module-HTTP-Request-Common
Provides: perl-module-HTTP-Response
Provides: perl-module-HTTP-Status
Provides: perl-module-LWP
Provides: perl-module-LWP-Authen-Basic
Provides: perl-module-LWP-Authen-Digest
Provides: perl-module-LWP-Authen-Ntlm
Provides: perl-module-LWP-ConnCache
Provides: perl-module-LWP-Debug
Provides: perl-module-LWP-DebugFile
Provides: perl-module-LWP-MediaTypes
Provides: perl-module-LWP-MemberMixin
Provides: perl-module-LWP-Protocol
Provides: perl-module-LWP-Protocol-GHTTP
Provides: perl-module-LWP-Protocol-data
Provides: perl-module-LWP-Protocol-file
Provides: perl-module-LWP-Protocol-ftp
Provides: perl-module-LWP-Protocol-gopher
Provides: perl-module-LWP-Protocol-http
Provides: perl-module-LWP-Protocol-http10
Provides: perl-module-LWP-Protocol-https
Provides: perl-module-LWP-Protocol-https10
Provides: perl-module-LWP-Protocol-mailto
Provides: perl-module-LWP-Protocol-nntp
Provides: perl-module-LWP-Protocol-nogo
Provides: perl-module-LWP-RobotUA
Provides: perl-module-LWP-Simple
Provides: perl-module-LWP-UserAgent
Provides: perl-module-Net-HTTP
Provides: perl-module-Net-HTTP-NB
Provides: perl-module-Net-HTTPS
Provides: perl-module-WWW-RobotRules
Provides: perl-module-WWW-RobotRules-AnyDBM_File


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
%{site_perl}/Net/* 
%{perl_prefix}/man/man1/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/bin/*
