Summary: The GNU MP Library
Name: gmp
Version: 4.1.2
Release: 0
Copyright: GPL
Group: Development/Libraries
Source: gmp-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
GNU MP is a library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers.  It has a rich set of
functions, and the functions have a regular interface.

gmp is used by librep, among other packages.

%package devel
Summary: GNU MP headers
Group: Development/Libraries
Requires: gmp = %{version}

%description devel
gmp-devel contains the documentation, headers and static libraries for
libgmp.

%prep
%setup -q

%build

# The compile is incredibly clued. 64-bit is automatic where supported. 
# Unfortunately it doesn't go into sparcv9.

%ifarch sparc64

### 64bit
LDFLAGS='-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9' CC=cc \
./configure --enable-shared --enable-static --enable-mpbsd \
--libdir=/usr/local/lib/sparcv9 --bindir=/usr/local/bin/sparcv9

make
#make check
make install DESTDIR=$RPM_BUILD_ROOT
make distclean

%endif

### 32bit (all builds)
# Unfortunately, there's hand-written v8plus assembly. ABI=32 => v8
# fails on this. We force it up to v8plus.

ABI=32 CC=cc CFLAGS='-xtarget=native -xarch=v8plus -xO4' \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' ./configure \
--enable-shared --enable-static --enable-mpbsd


make
#make check

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/gmp.info
fi

%preun devel
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gmp.info
fi

%files
%defattr(-,bin,bin)
%doc COPYING
/usr/local/lib/lib*.so*
%ifarch sparc64
/usr/local/lib/sparcv9/lib*.so*
%endif

%files devel
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/info/gmp.info*
/usr/local/lib/*.a
%ifarch sparc64
/usr/local/lib/sparcv9/*.a
%endif

# *.la is known unpackaged (and should be unpackaged!)
