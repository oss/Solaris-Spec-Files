Summary:	The Python language interpeter
Name:		python
Version:	2.5.1
Release:	1
Group:		Development/Languages
License:	BSD type
Source:		Python-%{version}.tar.bz2
#Patch:		python-conf.patch
#Patch0:	python25-ffi.patch
BuildRoot:	/var/tmp/%{name}-root
Requires:	tcl-tk, tcl, readline5, db, gdbm, gmp, ncurses, sqlite, db4, expat, openssl
BuildRequires:	tcl, tcl-tk, readline5-devel, db, gdbm, gmp-devel, ncurses-devel, sqlite-devel, db4, expat-devel, openssl

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
#%patch0 -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -mt" CXX="CC -mt" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/include/ncursesw -I/usr/local/include/readline" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -lncursesw" \
LD_PRELOAD="/usr/local/ssl/lib/libcrypto.so" \
LANG="C"
export PATH CC CXX CPPFLAGS LD LDFLAGS LD_PRELOAD LANG

cp Modules/Setup.dist Modules/Setup

cat << EOF >> Modules/Setup
_curses _cursesmodule.c -lncursesw
_curses_panel _curses_panel.c -lpanel -lncursesw

readline readline.c -lreadline -lncursesw -I/usr/local/include/readline -L/usr/local/lib

_socket socketmodule.c

SSL=/usr/local/ssl
_ssl _ssl.c \
       -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
       -L$(SSL)/lib -lssl -lcrypto

crypt cryptmodule.c # -lcrypt  # crypt(3); needs -lcrypt on some systems

sunaudiodev sunaudiodev.c

_tkinter _tkinter.c tkappinit.c -DWITH_APPINIT \
       -L/usr/local/lib \
       -I/usr/local/include \
       -I/usr/openwin/include \
       -ltk8.4 -ltcl8.4 \
       -L/usr/openwin/lib \
       -lX11

gdbm gdbmmodule.c -I/usr/local/include -L/usr/local/lib -lgdbm

#DB=/usr/local/BerkeleyDB3.3
#DBLIBVER=3.3
#DBINC=$(DB)/include
#DBLIB=$(DB)/lib
#_bsddb _bsddb.c -I$(DBINC) -L$(DBLIB) -ldb-$(DBLIBVER)

cStringIO cStringIO.c
cPickle cPickle.c

fpectl fpectlmodule.c -R/opt/SUNWspro/lib -lsunmath -lm

EXPAT_DIR=/usr/local
pyexpat pyexpat.c -DHAVE_EXPAT_H -I$(EXPAT_DIR)/lib -L$(EXPAT_DIR) -lexpat

EOF

./configure --with-threads --prefix=/usr/local --without-gcc

mv Makefile Makefile.wrong
sed -e 's/-I. -I$(srcdir)\/Include/-I. -I$(srcdir)\/Include -I\/usr\/local\/include -I\/usr\/local\/include\/ncursesw -I\/usr\/local\/include\/readline/g' Makefile.wrong > Makefile
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

%changelog
* Mon Aug 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.1-2
- Updated to 2.5.1
* Wed Jan 31 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.5-2
- Updated to 2.5

