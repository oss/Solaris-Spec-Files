%include perl-header.spec

Summary: Class-Container - Glues object frameworks together transparently

Name: perl-module-Class-Container
Version: 0.10
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Class-Container-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
    This class facilitates building frameworks of several classes that
    inter-operate. It was first designed and built for "HTML::Mason", in 
which
    the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and 
several
    other objects must create each other transparently, passing the 
appropriate
    parameters to the right class, possibly substituting other 
subclasses for
    any of these objects.

    The main features of "Class::Container" are:

    *   Explicit declaration of containment relationships (aggregation, 
factory
        creation, etc.)

    *   Declaration of constructor parameters accepted by each member in 
a class
        framework

    *   Transparent passing of constructor parameters to the class that 
needs
        them

    *   Ability to create one (automatic) or many (manual) contained 
objects
        automatically and transparently


%prep

%setup -q -n Class-Container-%{version}

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
%doc README Changes 
%{site_perl}/Class/Container.pm
%{site_perl_arch}/auto/Class/Container
%{perl_prefix}/man/man3/*
