%include perl-header.spec

Summary: Uniform Resource Indentifier class for Perl
Name: perl-module-URI
Version: 1.35
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: URI-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: perl-module-MIME-Base64
BuildRequires: perl = %{perl_version}
BuildRequires: perl-module-MIME-Base64

%description
This package contains the URI.pm module with friends.  The module
implements the URI class.  Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

URI objects can be used to access and manipulate the various
components that make up these strings.  There are also methods to
combine URIs in various ways.

The URI class replaces the URI::URL class that used to be distributed
with libwww-perl.  This package contains an emulation of the old
URI::URL interface.  The emulated URI::URL implements both the old and
the new interface.

%prep
%setup -q -n URI-%{version}

%build
perl Makefile.PL
make
set +e; make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes rfc2396.txt
%{site_perl_arch}/auto/URI
%{site_perl}/URI
%{site_perl}/URI.pm
%{perl_prefix}/man/man3/*

%changelog
* Thur Aug 06 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.35-2
- Updated to newest version.
