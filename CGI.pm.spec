%include perl-header.spec

Summary: CGI.pm - an easy-to-use Perl5 library for writing World Wide Web CGI scripts
Name: perl-module-CGI.pm
Version: 2.97
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: CGI.pm-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
You'll find very verbose documentation in the file cgi_docs.html,
located in the top level directory.  

Terser documentation is found in POD (plain old documentation) form in
CGI.pm itself.  When you install CGI, the MakeMaker program will
automatically install the manual pages for you (on Unix systems, type
"man CGI").


%prep

%setup -q -n CGI.pm-%{version}

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
%doc README Changes cgi-lib_porting.html cgi_docs.html examples
%{global_perl}/CGI/*
%{perl_prefix}/man/man3/*

