Summary: Library for manipulating gif images
Name: libungif
Version: 4.1.0
Release: 3
Group: Development/Libraries
Copyright: BSD-type
Source: libungif-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
This is libungif, a library for manipulating gif files in a manner
compatible with libgif, the gif library authored and maintainer by
Eric S. Raymond.  The observant builder of this package may in fact
notice that this package is mostly Eric S. Raymond's libgif with a few
changes (Please see the NEWS file)

%package devel
Summary: Header files and static libraries for libungif
Group: Development/Libraries

%description devel
This package contains the header files and static libraries for
libungif.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CPPFLAGS="-I/usr/local/include" \
 ./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/*
%doc BUGS AUTHORS COPYING README NEWS ONEWS NEWS README UNCOMPRESSED_GIF TODO
/usr/local/bin/*
/usr/local/lib/lib*.so*

%files devel
%defattr(-,bin,bin)
/usr/local/include/gif_lib.h
/usr/local/lib/lib*a
