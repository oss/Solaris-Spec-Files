%include perl-header.spec

Summary: Perl module that formats arrays
Name: perl-module-Data-ShowTable
Version: 3.3
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Data-ShowTable-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
ShowTable.pm, version 3.3, is a Perl 5 module which defines
subroutines to print arrays of data in a nicely formatted listing,
using one of four possible formats: simple table, boxed table, list
style, and HTML-formatting (for World-Wide-Web output).  See the
documentation on ShowTable.pm for details on the formatting.

The program "showtable" reads data in a variety of formats from a file
or STDIN, optimally columnizes the data, and then feeds the array of
data to the ShowTable module for display.  Showtable can parse its own
output as input (except for HTML).  Individual or ranges of columns
may be selected for display, either by name or by index.

%prep
%setup -q -n Data-ShowTable-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes Copyright GNU-LICENSE
%{site_perl_arch}/auto/Data/ShowTable
%{site_perl}/Data/*
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/bin/*
