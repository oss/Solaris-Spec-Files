%include machine-header.spec

Summary: The GNU MP Library
Name: gmp
Version: 4.0.1
Release: 1
Copyright: GPL
Group: Development/Libraries
Source: gmp-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

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

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" ./configure --enable-shared \
  --enable-static --enable-mpbsd host=%{sparc_arch}
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

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

%files devel
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/info/gmp.info*
/usr/local/lib/*a
