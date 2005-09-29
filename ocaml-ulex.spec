Summary: An OCaml lexer generator for Unicode
Name: ocaml-ulex
Version: 0.7
Release: 1
Group: Programming/Languages
License: MIT-like
Requires: ocaml >= 3.08 zlib
BuildRequires: ocaml >= 3.08 zlib-devel sed
Source: ulex-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
- ulex is a lexer generator.

- it is implemented as an OCaml syntax extension:
  lexer specifications are embedded in regular OCaml code.

- the lexers work with a new kind of "lexbuf" that supports Unicode;
  a single lexer can work with arbitrary encodings of the input stream.

%prep
%setup -q -n ulex-%{version}

%build
make all

%install
mkdir -p $RPM_BUILD_ROOT/`ocamlc -where`
sed -e 's#^	ocamlfind install ulex\(.*\)#	ocamlfind install -destdir $(RPM_BUILD_ROOT)/`ocamlc -where` ulex \1#' Makefile > Makefile.ru
mv Makefile Makefile.orig
mv Makefile.ru Makefile

make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/lib/ocaml/ulex/*
