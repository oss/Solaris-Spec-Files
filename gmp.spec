Summary:	The GNU MP Library
Name:		gmp
Version:	4.2.3
Release:	1
Copyright:	GPL
Group:		Development/Libraries
Source:		gmp-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

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

%package devel64
Summary: GNU MP headers
Group: Development/Libraries
Requires: gmp = %{version}

%description devel64
gmp-devel contains the documentation, headers and static libraries for
libgmp64.

%prep
%setup -q

%build

### 32bit (all builds)
# Unfortunately, there's hand-written v8plus assembly. ABI=32 => v8
# fails on this. We force it up to v8plus.

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
LIBXML_LIBS="-lxml2" \
ABI=32 CFLAGS='-xarch=v8plus -g -xs'
export PATH CC CXX CPPFLAGS LD LDFLAGS LIBXML_LIBS ABI CFLAGS

./configure \
	--enable-shared \
	--enable-static \
	--enable-mpbsd

gmake -j3
gmake check
gmake install DESTDIR=$RPM_BUILD_ROOT
gmake distclean

# The compile is incredibly clued. 64-bit is automatic where supported. 
# Unfortunately it doesn't go into sparcv9.

%ifarch sparc64

### 64bit
ABI=64 LDFLAGS='-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/lib/sparcv9 -R/usr/lib/sparcv9' \
CC=cc CFLAGS="-xarch=v9 -g -xs" \
./configure --enable-shared --enable-static --enable-mpbsd \
--libdir=/usr/local/lib/sparcv9 --bindir=/usr/local/bin/sparcv9 \
--includedir=/usr/local/include/gmp64

gmake -j3
gmake check
mkdir -p $RPM_BUILD_ROOT/usr/local/include/gmp32
mv $RPM_BUILD_ROOT/usr/local/include/gmp.h $RPM_BUILD_ROOT/usr/local/include/gmp32
mv $RPM_BUILD_ROOT/usr/local/include/mp.h $RPM_BUILD_ROOT/usr/local/include/gmp32

%endif

%install
gmake install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/include/gmp64
mv $RPM_BUILD_ROOT/usr/local/include/*.h $RPM_BUILD_ROOT/usr/local/include/gmp64

rm -rf %{buildroot}/usr/local/info/dir
rm -rf %{buildroot}/usr/local/lib/*.la
rm -rf %{buildroot}/usr/local/lib/sparcv9/*.la

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
/usr/local/include/gmp32/*
/usr/local/info/gmp.info*
/usr/local/lib/*.a

# *.la is known unpackaged (and should be unpackaged!)

%files devel64
%defattr(-,bin,bin)
/usr/local/include/gmp64/*
/usr/local/lib/sparcv9/*.a

%changelog
* Mon Aug 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.2.3-1
- bump
* Sat Oct 20 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.2-1
- Bump to 4.2.2
