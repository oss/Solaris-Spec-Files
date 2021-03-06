Summary: Objective Caml compiler
Name: ocaml
Version: 3.08.4
Release: 1
Group: Programming/Languages
License: QPL
Requires: tcl >= 8.4.0, tcl-tk >= 8.4.0
BuildRequires: tcl >= 8.4.0, tcl-tk >= 8.4.0
Source0: ocaml-%{version}.tar.bz2
Source1: ocaml-3.08-refman.dvi.gz
BuildRoot: /var/tmp/%{name}-root

%description
Objective Caml is an implementation of the ML language, based on the
Caml Light dialect extended with a complete class-based object system
and a powerful module system in the style of Standard ML.

Objective Caml comprises two compilers. One generates bytecode which is
then interpreted by a C program. This compiler runs quickly, generates
compact code with moderate memory requirements, and is portable to
essentially any 32 or 64 bit Unix platform. Performance of generated
programs is quite good for a bytecoded implementation:  almost twice as
fast as Caml Light 0.7. This compiler can be used either as a
standalone, batch-oriented compiler that produces standalone programs,
or as an interactive, toplevel-based system.

The other compiler generates high-performance native code for a number
of processors. Compilation takes longer and generates bigger code, but
the generated programs deliver excellent performance, while retaining
the moderate memory requirements of the bytecode compiler.

  [ from README ]

%prep
%setup -q
gzip -dc %{SOURCE1} > ocaml-%{version}-refman.dvi
chmod 644 ocaml-%{version}-refman.dvi

%build
./configure -tkdefs "-I/usr/local/include" -tklibs "-L/usr/local/lib -ltk8.4 -ltcl8.4 -R/usr/local/lib" -ccopt "cc" -libopt "-L/usr/local/lib -R/usr/local/lib -I/usr/local/include"
make world
make bootstrap

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install PREFIX=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE ocaml-%{version}-refman.dvi
/usr/local/bin/*
/usr/local/lib/ocaml
/usr/local/man/man1/*
/usr/local/man/man3/*
