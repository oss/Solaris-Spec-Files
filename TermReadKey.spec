%include perl-header.spec

Summary: Perl module for terminal input-mode-changing
Name: perl-module-TermReadKey
Version: 2.14
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: TermReadKey-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
This module, ReadKey, provides ioctl control for terminals and Win32
consoles so the input modes can be changed (thus allowing reads of a
single character at a time), and also provides non-blocking reads of
stdin, as well as several other terminal related features, including
retrieval/modification of the screen size, and retrieval/modification
of the control characters.  Installation requires MakeMaker 3.5 or
higher (MakeMaker 3.7 is included with perl 5.001, so now is a good
time to upgrade if you haven't already.)

%prep
%setup -q -n TermReadKey-%{version}

%build
perl Makefile.PL
make
# no make test - it is interactive

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/auto/Term/ReadKey
%{site_perl_arch}/Term/ReadKey.pm
%{perl_prefix}/man/man3/*
