%include machine-header.spec

Name: gc
Version: 6.0
Copyright: BSD-like
Group: Development/Libraries
Summary: Garbage collecting libraries
Release: 2
Source: gc%{version}.tar.gz
Provides: libgc.so.1
Provides: libgc.so
BuildRoot: /var/tmp/%{name}-root
%ifarch sparc64
%ifos solaris2.8
BuildRequires: gcc3
%endif
%endif

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
%ifarch sparc64
%ifos solaris2.8
CC=/usr/local/gcc-3.0.2/bin/sparcv9-sun-%{sol_os}-gcc ./configure --libdir=/usr/local/lib/64
%else
./configure
%endif
%endif

%ifnarch sparc64
./configure
%endif

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
%ifarch sparc64
%ifos solaris2.8
/usr/local/lib/64/libgc.so*
%else
/usr/local/lib/libgc.so*
%endif
%endif

%ifnarch sparc64
/usr/local/lib/libgc.so*
%endif

%files devel
%defattr(-,bin,bin)
/usr/local/include/*.h
/usr/local/man/man3/gc.3

%ifarch sparc64
%ifos solaris2.8
/usr/local/lib/64/libgc.a
/usr/local/lib/64/libgc.la
%else
/usr/local/lib/libgc.a
/usr/local/lib/libgc.la
%endif
%endif

%ifnarch sparc64
/usr/local/lib/libgc.a
/usr/local/lib/libgc.la
%endif

