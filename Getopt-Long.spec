%include perl-header.spec

Summary: Getopt::Long
Name: perl-module-Getopt-Long
Version: 2.33
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Getopt-Long-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
Module Getopt::Long implements an extended getopt function called
GetOptions(). This function implements the POSIX standard for command
line options, with GNU extensions, while still capable of handling
the traditional one-letter options.
In general, this means that command line options can have long names
instead of single letters, and are introduced with a double dash `--'.

Optionally, Getopt::Long can support the traditional bundling of
single-letter command line options.

Getopt::Long::GetOptions() is part of the Perl 5 distribution. It is
the successor of newgetopt.pl that came with Perl 4. It is fully
upward compatible. In fact, the Perl 5 version of newgetopt.pl is just
a wrapper around the module.


%prep

%setup -q -n Getopt-Long-%{version}

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
%{global_perl}/Getopt/Long.pm
%{global_perl}/newgetopt.pl
%{global_perl_arch}/auto/Getopt/Long
%{perl_prefix}/man/man3/*
