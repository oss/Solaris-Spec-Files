%include perl-header.spec
%define module_name Getopt-Long

Summary: Getopt::Long
Name: perl-module-%{module_name}
Version: 2.36
Release: 2
Group: System Environment/Base
License: Perl (Artistic and GPL-2)
Source: %{module_name}-%{version}.tar.gz
URL: http://search.cpan.org/~jv/%{module_name}-%{version}/lib/Getopt/Long.pm
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Module Getopt::Long implements an extended getopt function called
GetOptions(). This function implements the POSIX standard for command
line options, with GNU extensions, while still capable of handling
the traditional one-letter options.
In general, this means that command line options can have long names
instead of single letters, and are introduced with a double dash '--'.

Optionally, Getopt::Long can support the traditional bundling of
single-letter command line options.

Getopt::Long::GetOptions() is part of the Perl 5 distribution. It is
the successor of newgetopt.pl that came with Perl 4. It is fully
upward compatible. In fact, the Perl 5 version of newgetopt.pl is just
a wrapper around the module.

%prep
%setup -qn %{module_name}-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f `/usr/local/gnu/bin/find %{buildroot} -iname perllocal.pod`
rm -f %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc Announce CHANGES INSTALL README examples/
%{global_perl}/Getopt/*
%{global_perl}/newgetopt.pl
%{global_perl_arch}/auto/*
%{perl_prefix}/man/man3/*

%changelog
* Thu Aug 16 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.36-2
- Upgraded to the latest version.
* Mon Apr 24 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 2.35-1
- Upgraded to the latest version.
