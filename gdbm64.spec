%include machine-header.spec

Name: gdbm64
Version: 1.8.0
Release: 5
Summary: The GNU database library
Source: gdbm-1.8.0.tar.gz
Copyright: GPL
Group: System Environment/Libraries
%ifarch sparc64
BuildRequires: gcc3
%else
#BuildRequires: %{max_bits} == 64
%endif
Requires: gdbm
BuildRoot: /var/tmp/%{name}-root

%description
From the documentation:

      GNU `dbm' (`gdbm')is a library of database functions that use
   extendible hashing and works similar to the standard UNIX `dbm'
   functions.  These routines are provided to a programmer needing to
   create and manipulate a hashed database. (`gdbm' is *NOT* a complete
   database package for an end user.)

This package of gdbm provides 64-bit libraries for sparcv9 applications.

%prep
%setup -q -n gdbm-1.8.0

%build

CC=/usr/local/gcc-3.0.2/bin/sparcv9-sun-%{sol_os}-gcc ./configure --prefix=/usr/local --libdir=/usr/local/lib/64
make

%install
./mkinstalldirs $RPM_BUILD_ROOT/usr/local/lib/64

/bin/sh ./libtool install -c libgdbm.la $RPM_BUILD_ROOT/usr/local/lib/64/libgdbm.la

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
/usr/local/lib/64/lib*a
/usr/local/lib/64/lib*.so*
