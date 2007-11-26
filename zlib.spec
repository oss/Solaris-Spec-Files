Name:		zlib
Version:	1.2.3
License:	zlib license
Group:		Development/Libraries
Summary:	Compression libraries
Release:	7
Source:		http://www.zlib.net/zlib-%{version}.tar.gz
Provides:	libz.so
BuildRoot:	%{_tmppath}/%{name}-root

%ifarch sparc64
Provides: %{name}-sparc64
%endif

%description
zlib is a general-purpose, lossless compression library that has
no restrictions on redistribution. 

%package devel
Summary: zlib headers and static libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
zlib-devel contains the static libraries and headers for zlib.

%prep
%setup -q

%build

%ifarch sparc64
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc -xarch=v9" CXX="CC -xarch=v9" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export PATH CC CXX CPPFLAGS LD LDFLAGS
# make sparcv9 .so files
   LDSHARED="/usr/ccs/bin/ld -G" \
   ./configure --shared
   gmake -j3
   mkdir sparcv9
   cp libz.so.* sparcv9/
   gmake clean
%endif

gmake clean
# make .so file(s)
./configure --shared
gmake -j3
# make .a files
./configure --prefix=/usr/local
gmake -j3

%install
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install prefix=%{buildroot}/usr/local
./configure --shared
gmake install prefix=%{buildroot}/usr/local
%ifarch sparc64
   mkdir -p %{buildroot}/usr/local/lib/sparcv9
   cp sparcv9/* %{buildroot}/usr/local/lib/sparcv9/

   cd %{buildroot}/usr/local/lib/sparcv9/
   ln -s libz.so.1.2.3 libz.so
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
%ifarch sparc64
   /usr/local/lib/sparcv9/lib*.so*
%endif

%files devel
%defattr(-,bin,bin)
%doc ChangeLog FAQ README algorithm.txt examples/
/usr/local/include/zlib.h
/usr/local/include/zconf.h
/usr/local/lib/libz.a
/usr/local/share/man/man3/zlib.3

%changelog
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.2.3-5
- Respinning 1.2.3 because apparently it doesn't exist anywhere in our repo
* Fri May 05 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.2.3-4
- Built the latest version of zlib.
