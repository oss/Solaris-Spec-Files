Name: zlib
Version: 1.1.4
Copyright: freely distributable
Group: Development/Libraries
Summary: Compression libraries
Release: 1
Source: http://prdownloads.sourceforge.net/libpng/zlib-1.1.4.tar.gz
Provides: libz.so.1
Provides: libz.so
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/include/zlib.h
/usr/local/include/zconf.h
/usr/local/lib/libz.a

