%include perl-header.spec

Summary: HTML parser module for Perl
Name: perl-module-HTML-Parser
Version: 3.10
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: HTML-Parser-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This is a collection of modules that parse and extract information
from HTML documents.  Bug reports and discussions about these modules
can be sent to the <libwww@perl.org> mailing list.  Remember to also
look at the HTML-Tree package that creates and extracts information from
HTML syntax trees.

%prep
%setup -q -n HTML-Parser-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/auto/HTML/Parser
%{site_perl_arch}/HTML/*
%{perl_prefix}/man/man3/*
