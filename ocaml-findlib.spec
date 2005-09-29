Summary: OCaml findlib library
Name: ocaml-findlib
Version: 1.0.4
Release: 1
Group: Programming/Languages
License: LGPL
Requires: ocaml >= 3.08 zlib
BuildRequires: ocaml >= 3.08 zlib-devel sed
Source: findlib-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
The "findlib" software provides a scheme to manage reusable software components.
in the form of libraries, and includes tools that support this scheme. A.
library installed as a findlib component is also called a package. The point is.
that the findlib scheme allows it to store metainformation about the library,.
especially how it can be used in programs. The packages are kept in the.
filesystem hierarchy, but the directory structure is defined by findlib, and.
there is no way to deviate from this standard. The library contains functions.
to look the directory up that stores a package, to query metainformation about.
a package, and to retrieve dependency information about multiple packages..
There is also a tool that allows the user to enter queries on the command-line..
In order to simplify compilation and linkage, there are new frontends of the.
various OCaml compilers that can directly deal with packages...

%prep
%setup -q -n findlib-%{version}

%build
./configure -with-toolbox
make all

%install
make install prefix=$RPM_BUILD_ROOT

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/bin/ocamlfind
/usr/local/etc/findlib.conf
/usr/local/lib/ocaml/site-lib/*
/usr/local/lib/ocaml/topfind
/usr/local/man/man1/ocamlfind.1
/usr/local/man/man5/*
