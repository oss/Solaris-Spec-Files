%include perl-header.spec

Summary: Perl data structure stringifier
Name: perl-module-Data-Dumper
Version: 2.101
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Data-Dumper-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

%description
You may find this module useful if you:

   * are writing an application that must display perl data
     structures.

   * want to store some data structures to disk, in either a
     compact or perl readable format (Dumper outputs pure perl,
     so you don't have to invent your own portable data format, or
     parse it;  simply "do FILE" or read the data back in with 
     perl and eval() it).  See the MLDBM module for an example of
     one such use.

   * want a simple, yet powerful, persistence engine that can be
     quickly integrated into your application, and is a breeze to
     debug.

   * want a facility to make copies of data, or quickly find
     differences between data structures.

%prep
%setup -q -n Data-Dumper-%{version}

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
%{global_perl_arch}/auto/Data/Dumper
%{global_perl_arch}/Data/*
%{perl_prefix}/man/man3/*
