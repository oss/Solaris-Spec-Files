%include perl-header.spec

Summary: IO::stringy - I/O on in-core objects like strings and arrays
Name: perl-module-IO-stringy
Version: 2.110
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: IO-stringy-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

Provides: perl-module-IO-Atomatic-File
Provides: perl-module-IO-Clever
Provides: perl-module-IO-InnerFile
Provides: perl-module-IO-Lines
Provides: perl-module-IO-Scalar
Provides: perl-module-IO-ScalarArray
Provides: perl-module-IO-Stringy
Provides: perl-module-IO-Wrap
Provides: perl-module-IO-WrapTie

%description
    This toolkit primarily provides modules for performing both traditional
    and object-oriented i/o) on things *other* than normal filehandles; in
    particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

    In the more-traditional IO::Handle front, we have IO::AtomicFile which
    may be used to painlessly create files which are updated atomically.

    And in the "this-may-prove-useful" corner, we have IO::Wrap, whose
    exported wraphandle() function will clothe anything that's not a blessed
    object in an IO::Handle-like wrapper... so you can just use OO syntax
    and stop worrying about whether your function's caller handed you a
    string, a globref, or a FileHandle.

%prep

%setup -q -n IO-stringy-%version

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
%doc README
%{site_perl}/IO/*
%{site_perl_arch}/auto/IO/Stringy/.packlist
%{perl_prefix}/man/man3/*
