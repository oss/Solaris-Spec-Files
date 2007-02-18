Summary: A C library for multiple-precision floating-point computations
Name: mpfr
Version: 2.2.1
Release: 1
Copyright: LGPL
Group: Development/Libraries
Source: mpfr-%{version}.tar.bz2
# Grab the latest from http://www.mpfr.org/mpfr-2.2.1/patches and rename it
Patch0: mpfr-2.2.1-latest.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: gmp-devel
Requires: gmp

%description

The MPFR library is a C library for multiple-precision floating-point
computations with correct rounding. MPFR has continuously been
supported by the INRIA and the current main authors come from the
CACAO and Arenaire project-teams at Loria (Nancy, France) and LIP
(Lyon, France) respectively; see more on the credit page. MPFR is
based on the GMP multiple-precision library.

The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a
well-defined semantics. It copies the good ideas from the
ANSI/IEEE-754 standard for double-precision floating-point arithmetic
(53-bit mantissa).

MPFR is free. It is distributed under the GNU Lesser General Public
License (GNU Lesser GPL). The library has been registered in France by
the Agence de Protection des Programmes under the number IDDN FR 001
120020 00 R P 2000 000 10800, on 15 March 2000. This license
guarantees your freedom to share and change MPFR, to make sure MPFR is
free for all its users. Unlike the ordinary General Public License,
the Lesser GPL enables developers of non-free programs to use MPFR in
their programs. If you have written a new function for MPFR or
improved an existing one, please share your work!

%package devel
Summary: mpfr development libraries
Group: Development/Libraries
Requires: mpfr = %{version}

%description devel
mpfr-devel contains the documentation, headers and static libraries for
libmpfr.

%prep
%setup -q

%patch0 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/bin:/usr/bin:/usr/local/bin"
export PATH

#%ifarch sparc64
#
##### 64bit
#ABI=64 LDFLAGS='-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9' \
#CC=cc CFLAGS="-xarch=v9 -xildoff -g -xs" \
#./configure --prefix=/usr/local --enable-shared --enable-static \
#  --libdir=/usr/local/lib/sparcv9 --bindir=/usr/local/bin/sparcv9 \
#  --with-gmp-include=/usr/local/include \
#  --with-gmp-lib=/usr/local/lib
#
#make
#make check
#make install DESTDIR=$RPM_BUILD_ROOT
#make distclean
#
#%endif

### 32bit (all builds)
# Unfortunately, there's hand-written v8plus assembly. ABI=32 => v8
# fails on this. We force it up to v8plus.

#ABI=32 CC=cc CFLAGS='-xarch=v8plus -g -xs' \
CC='cc' CFLAGS='-xildoff -g -xs' \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
./configure --prefix=/usr/local --enable-shared --enable-static \
  --with-gmp-include=/usr/local/include \
  --with-gmp-lib=/usr/local/lib


make
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING
/usr/local/lib/lib*.so*
#%ifarch sparc64
#/usr/local/lib/sparcv9/lib*.so*
#%endif

%files devel
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/*.a
#%ifarch sparc64
#/usr/local/lib/sparcv9/*.a
#%endif

