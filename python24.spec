Summary: The Python language interpeter
Name: python
Version: 2.4.4
Release: 1
Group: Development/Languages
License: BSD type
Source: Python-%{version}.tar.bz2
#Patch: python-conf.patch
BuildRoot: /var/tmp/%{name}-root
Requires: tcl-tk, tcl, readline, db, gdbm, gmp, ncurses
BuildRequires: tcl, tcl-tk, readline, db, gdbm, gmp-devel, ncurses-devel

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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -mt" CXX="CC -mt" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/include/ncursesw" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
LD_PRELOAD="/usr/local/ssl/lib/libcrypto.so" \
LANG="C"
export PATH CC CXX CPPFLAGS LD LDFLAGS LD_PRELOAD LANG

cp Modules/Setup.dist Modules/Setup

echo "_curses _cursesmodule.c -lncursesw" >> Modules/Setup
echo "_curses_panel _curses_panel.c -lpanel -lncursesw" >> Modules/Setup

./configure --with-threads --prefix=/usr/local --without-gcc

mv Makefile Makefile.wrong
sed -e 's/-I. -I$(srcdir)\/Include/-I. -I$(srcdir)\/Include -I\/usr\/local\/include -I\/usr\/local\/include\/ncursesw/g' Makefile.wrong > Makefile
rm Makefile.wrong

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
