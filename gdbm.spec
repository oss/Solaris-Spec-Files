Name: gdbm
Version: 1.8.3
Release: 3
Summary: The GNU database library
Source: gdbm-%{version}.tar.gz
Copyright: GPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-root

%description
From the documentation:

      GNU `dbm' (`gdbm')is a library of database functions that use
   extendible hashing and works similar to the standard UNIX `dbm'
   functions.  These routines are provided to a programmer needing to
   create and manipulate a hashed database. (`gdbm' is *NOT* a complete
   database package for an end user.)

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
make

%install
./mkinstalldirs $RPM_BUILD_ROOT/usr/local/lib $RPM_BUILD_ROOT/usr/local/include $RPM_BUILD_ROOT/usr/local/man/man3 $RPM_BUILD_ROOT/usr/local/info

/bin/sh ./libtool install -c libgdbm.la $RPM_BUILD_ROOT/usr/local/lib/libgdbm.la
install -c gdbm.h $RPM_BUILD_ROOT/usr/local/include/gdbm.h
install -c ./gdbm.3 \
	$RPM_BUILD_ROOT/usr/local/man/man3/gdbm.3
install -c ./gdbm.info \
	$RPM_BUILD_ROOT/usr/local/info/gdbm.info
install -c ./dbm.h \
	$RPM_BUILD_ROOT/usr/local/include/dbm.h
install -c ./ndbm.h \
	$RPM_BUILD_ROOT/usr/local/include/ndbm.h

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
            --entry="* Gdbm: (gdbm).          GNU dbm" \
	    /usr/local/info/gdbm.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	    /usr/local/info/gdbm.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/lib/lib*a
/usr/local/lib/lib*.so*

%defattr(644,bin,bin)
/usr/local/include/*
/usr/local/man/man3/gdbm.3
/usr/local/info/gdbm.info
