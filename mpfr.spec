Summary:       A C library for multiple-precision floating-point computations
Name:          mpfr
Version:       3.0.0
Release:       1
License:       LGPL
Group:         Development/Libraries
URL:           http://ftp.gnu.org/gnu/mpfr/
Source:        http://ftp.gnu.org/gnu/mpfr/mpfr-%{version}.tar.xz
Patch0:        mpfr-solaris-compile.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gmp-devel gmp-devel64
Requires:      gmp

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
Requires: mpfr = %{version}-%{release}

%description devel
mpfr-devel contains the documentation, headers and static libraries for
libmpfr.

%prep
%setup -q
%patch0 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/bin:/usr/bin:/usr/local/bin:/usr/local/teTeX/bin:$PATH"
export PATH

%ifarch sparc64

#### 64bit
ABI=64 PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" CFLAGS="-m64 -g -xs" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS ABI
./configure --prefix=/usr/local --enable-shared --enable-static \
  --libdir=/usr/local/lib/sparcv9 --bindir=/usr/local/bin/sparcv9 \
  --with-gmp-include=/usr/local/include/gmp64 \
  --with-gmp-lib=/usr/local/lib/sparcv9


gmake -j3
gmake check
gmake install DESTDIR=$RPM_BUILD_ROOT
gmake distclean

%endif

### 32bit (all builds)
# Unfortunately, there's hand-written v8plus assembly. ABI=32 => v8
# fails on this. We force it up to v8plus.

#ABI=32 CC=cc CFLAGS='-xarch=v8plus -g -xs' \
CC='cc' CFLAGS='-xildoff -g -xs' \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib' \
./configure --prefix=/usr/local --enable-shared --enable-static \
  --with-gmp-include=/usr/local/include/gmp32 \
  --with-gmp-lib=/usr/local/lib


gmake -j3

%check
gmake check

%install
gmake install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/usr/local/share/info/dir
rm -f $RPM_BUILD_ROOT/usr/local/lib/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/*.a
rm -fr $RPM_BUILD_ROOT/usr/local/share/doc/mpfr/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING BUGS AUTHORS COPYING.LESSER FAQ.html NEWS TODO 
/usr/local/lib/lib*.so.*
/usr/local/share/info/mpfr.info
%ifarch sparc64
/usr/local/lib/sparcv9/lib*.so.*
%endif

%files devel
%defattr(-,root,root,-)
/usr/local/include/*
%doc examples
/usr/local/lib/*.so
%ifarch sparc64
/usr/local/lib/sparcv9/*.so
%endif

%changelog
* Fri Aug 06 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 3.0.0-1
- Update to latest version
- Drop static libraries