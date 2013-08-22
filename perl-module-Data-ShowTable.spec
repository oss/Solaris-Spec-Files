%include perl-header.spec

%define real_name Data-ShowTable

Name:		perl-module-Data-ShowTable
Version:	4.1
Release:	1
Summary:	Show data in nicely formatted columns

Group:		Development/Libraries
License:	GPLv2+
URL:		http://search.cpan.org/dist/Data-ShowTable/
Source0:	Data-ShowTable-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

BuildRequires:	perl, perl-module-ExtUtils-MakeMaker


%description
ShowTable.pm, version 4.1, is a Perl 5 module which defines subroutines
to print arrays of data in a nicely formatted listing, using one of
four possible formats: simple table, boxed table, list style, and
HTML-formatting (for World-Wide-Web output).  See the documentation on
ShowTable.pm for details on the formatting.

The program "showtable" reads data in a variety of formats from a file
or STDIN, optimally columnizes the data, and then feeds the array of
data to the ShowTable module for display.  Showtable can parse its own
output as input (except for HTML).  Individual or ranges of columns may
be selected for display, either by name or by index.

In other words, showtable is a data formatting program.  Using the
'-html' option, showtable can accept ASCII tablular data and format it
appropriately for display through a Web-browser.


%prep
%setup -q -n %{real_name}-%{version}


%build
perl Makefile.PL
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes Copyright README
%{perl_prefix}/bin/showtable
%{perl_prefix}/man/man1/showtable.1
%{perl_prefix}/man/man3/Data::ShowTable.3
%{site_perl}/Data/ShowTable.pm


%changelog
* Thu Aug 15 2013 Matt Robinson <mwr54@nbcs.rutgers.edu> - 4.1-1
- First build for Rutgers Solaris
