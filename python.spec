Summary: The Python language interpeter
Name: python
Version: 2.5
Release: 1
Group: Development/Languages
License: BSD type
Source: Python-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: tcl-tk, tcl, readline, db, gdbm, gmp, sqlite
BuildRequires: tcl, tcl-tk, readline, db, gdbm, gmp-devel, sqlite-devel

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
CC="cc -mt" CXX="CC -mt" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="${LDFLAGS} -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD_PRELOAD="/usr/local/ssl/lib/libcrypto.so" \
LANG="C"
export CC CXX LDFLAGS CPPFLAGS LD_PRELOAD LANG

#cat << EOF >> Modules/Setup
#
#### Custom stuff starts here
##_curses _cursesmodule.c -lcurses -ltermcap
#
##sunaudiodev sunaudiodev.c
#
#_tkinter _tkinter.c tkappinit.c -DWITH_APPINIT \
#-L/usr/local/lib \
#-I/usr/local/include \
#-I/usr/openwin/include \
#-ltk8.4 -ltcl8.4 \
#-L/usr/openwin/lib \
#-lX11
#
#EOF

./configure --prefix=/usr/local --with-threads --without-gcc
make
#make test

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
