Summary: The Python language interpeter
Name: python
Version: 1.6
Release: 5
Group: Development/Languages
Copyright: BSD type
Source: Python-%{version}.tar.gz
Patch: python-conf.patch
BuildRoot: /var/tmp/%{name}-root
Requires: tcl-tk, tcl, readline, db, gdbm, gmp
BuildRequires: tcl, tcl-tk, readline-devel, db, gdbm, gmp-devel

%description
Python is an interpreted, object-oriented, high-level programming
language with dynamic semantics.  Its high-level built in data
structures, combined with dynamic typing and dynamic binding, make it
very attractive for rapid application development, as well as for use
as a scripting or glue language to connect existing components
together.  Python's simple, easy to learn syntax emphasizes
readability and therefore reduces the cost of program maintenance.
Python supports modules and packages, which encourages program
modularity and code reuse.  The Python interpreter and the extensive
standard library are available in source or binary form without charge
for all major platforms, and can be freely distributed.

Often, programmers fall in love with Python because of the increased
productivity it provides.  Since there is no compilation step, the
edit-test-debug cycle is incredibly fast. Debugging Python programs is
easy: a bug or bad input will never cause a segmentation fault.
Instead, when the interpreter discovers an error, it raises an
exception.  When the program doesn't catch the exception, the
interpreter prints a stack trace. A source level debugger allows
inspection of local and global variables, evaluation of arbitrary
expressions, setting breakpoints, stepping through the code a line at
a time, and so on. The debugger is written in Python itself,
testifying to Python's introspective power. On the other hand, often
the quickest way to debug a program is to add a few print statements
to the source: the fast edit-test-debug cycle makes this simple
approach very effective.

  (from python documentation)

%prep
%setup -q -n Python-%{version}
%patch -p1

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CPPFLAGS="-I/usr/local/include" ./configure --with-threads
make
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/python%{version}/Tools
make install prefix=$RPM_BUILD_ROOT/usr/local

cd Tools
find . | cpio -pdm $RPM_BUILD_ROOT/usr/local/lib/python%{version}/Tools

cd $RPM_BUILD_ROOT
mkdir bin
mkdir usr/bin
ln -s ../usr/local/bin/python bin/python
ln -s ../local/bin/python usr/bin/python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Misc/*
/usr/local/man/man1/*
/usr/local/include/python%{version}
/usr/local/lib/python%{version}
/usr/local/bin/*
/usr/bin/python
/bin/python
