Summary:       C library for the arithmetic of complex numbers
Name:          mpc
Version:       0.8.2
Release:       1
License:       LGPLv2+
Group:         System Environment/Libraries
URL:           http://www.multiprecision.org/
Source:        http://www.multiprecision.org/mpc/download/mpc-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gmp-devel gmp-devel64 mpfr-devel

%description

Mpc is a C library for the arithmetic of complex numbers with arbitrarily
high precision and correct rounding of the result. It is built upon and
follows the same principles as Mpfr.

%package devel
Summary:       mpc development libraries
Group:         Development/Libraries
Requires:      mpc = %{version}-%{release}

%description devel
mpc-devel contains the documentation, headers and static libraries for
mpc.

%prep
%setup -q

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
rm -f $RPM_BUILD_ROOT/usr/local/lib/*/*.la
rm -f $RPM_BUILD_ROOT/usr/local/lib/*/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING.LIB AUTHORS NEWS TODO README ChangeLog
/usr/local/lib/lib*.so.*
/usr/local/share/info/mpc.info
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
* Tue Aug 10 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.8.2-1
- Initial Solaris build
