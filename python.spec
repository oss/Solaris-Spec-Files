Summary: The Python language interpeter
Name: python
Version: 2.4.3
Release: 1
Group: Development/Languages
License: BSD type
Source: Python-%{version}.tar.bz2
#Patch: python-conf.patch
BuildRoot: /var/tmp/%{name}-root
Requires: tcl-tk, tcl, readline, db, gdbm, gmp
BuildRequires: tcl, tcl-tk, readline, db, gdbm, gmp-devel

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

%prep
%setup -q -n Python-%{version}

%build
CC="cc" CXX="CC" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include" \
./configure --with-threads --prefix=/usr/local
make
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
python /usr/local/bin/unhardlinkify.py .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc Misc/*
/usr/local/man/man1/*
/usr/local/include/python*
/usr/local/lib/python*
/usr/local/bin/*
