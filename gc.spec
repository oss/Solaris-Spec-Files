Name: gc
Version: 6.0
Copyright: BSD-like
Group: Development/Libraries
Summary: Garbage collecting libraries
Release: 1
Source: gc%{version}.tar.gz
Provides: libgc.so.1
Provides: libgc.so
BuildRoot: /var/tmp/%{name}-root

%description
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new. It is also used by
a number of programming language implementations that use C as
intermediate code.

%package devel
Summary: gc headers and static libraries
Group: Development/Libraries

%description devel
gc-devel contains the static libraries and headers for gc.

%prep
%setup -q -n gc%{version}

%build
./configure
sed s/'ALL_INTERIOR_POINTERS'/'NO_DEBUGGING=1 -DLARGE_CONFIG'/g Makefile > Makefile.ru
cp Makefile.ru Makefile
make
make install DESTDIR=%{buildroot}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/include
mkdir -p %{buildroot}/usr/local/man/man3
make install DESTDIR=%{buildroot}
cp include/*.h %{buildroot}/usr/local/include
cp doc/gc.man %{buildroot}/usr/local/man/man3/gc.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/libgc.so*

%files devel
%defattr(-,bin,bin)
/usr/local/include/*.h
/usr/local/lib/libgc.a
/usr/local/lib/libgc.la
/usr/local/man/man3/gc.3
