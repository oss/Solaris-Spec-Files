%include perl-header.spec

Summary: ExtUtils::ParseXS - converts Perl XS code into C code

Name: perl-module-ExtUtils-ParseXS
Version: 2.02
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: ExtUtils-ParseXS-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
    "ExtUtils::ParseXS" will compile XS code into C code by embedding the
    constructs necessary to let C functions manipulate Perl values and creates
    the glue necessary to let Perl access those functions. The compiler uses
    typemaps to determine how to map C function parameters and variables to Perl
    values.

    The compiler will search for typemap files called *typemap*. It will use the
    following search path to find default typemaps, with the rightmost typemap
    taking precedence.

            ../../../typemap:../../typemap:../typemap:typemap

%prep

%setup -q -n ExtUtils-ParseXS-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
# Note:
# %define pmake_install     make install PREFIX=%{buildroot}%{perl_prefix}
# and perl_prefix = /usr/perl5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{global_perl}/ExtUtils/*
%{global_perl_arch}/auto/ExtUtils/*
%{perl_prefix}/man/man3/*

# NOTE: 
# site_perl_arch is 
# /usr/perl5/site_perl/5.6.1/sun4-solaris-thread-multi
# site_perl is
# /usr/perl5/site_perl/5.6.1/
