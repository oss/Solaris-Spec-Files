Name: zlib
Version: 1.1.4
Copyright: freely distributable
Group: Development/Libraries
Summary: Compression libraries
Release: 7
Source: http://prdownloads.sourceforge.net/libpng/zlib-1.1.4.tar.gz
Provides: libz.so
#Provides: libz.so vpkg-SUNWzlib
#Obsoletes: vpkg-SUNWzlib
%ifarch sparc64
BuildRequires: gcc3 
Provides: %{name}-sparc64
%endif
BuildRoot: /var/tmp/%{name}-root

%description
Zlib is a general-purpose, lossless compression library that has
no restrictions on redistribution. 

%package devel
Summary: zlib headers and static libraries
Group: Development/Libraries

%description devel
Zlib-devel contains the static libraries and headers for zlib.

%prep
%setup -q

%build
%ifarch sparc64
PATH="/usr/local/gcc3/bin:$PATH" \
CC="/usr/local/gcc3/bin/gcc" \
LDSHARED="/usr/ccs/bin/ld -G" \
./configure --shared
make
mkdir sparcv9
cp libz.so.* sparcv9/
make clean
%endif
make clean
./configure --shared
make
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
./configure --shared
make install prefix=$RPM_BUILD_ROOT/usr/local

%ifarch sparc64
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
cp sparcv9/* $RPM_BUILD_ROOT/usr/local/lib/sparcv9/
%endif

%post
ln -s /usr/local/lib/libz.so.1 /usr/local/lib/libz.so
%ifarch sparc64
ln -s /usr/local/lib/sparcv9/libz.so.1 /usr/local/lib/sparcv9/libz.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so.*
%ifarch sparc64
/usr/local/lib/sparcv9/lib*.so.*
%endif

%files devel
%defattr(-,bin,bin)
/usr/local/include/zlib.h
/usr/local/include/zconf.h
/usr/local/lib/libz.a

