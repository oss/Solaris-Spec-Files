%include machine-header.spec

Name: binutils
Version: 2.11
Release: 2
Copyright: GPL
Group: Development/Tools
Source: binutils-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: GNU binutils
Requires: gcc
%description
The GNU binutils are:  addr2line, ar, as, gasp, gprof, ld, nm,
objcopy, objdump, ranlib, readelf, size, strings, and strip.

Bear in mind that the Solaris binutils are much more reliable (and
work with the v9 architecture better).

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make
make info

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/gnu
make install prefix=$RPM_BUILD_ROOT/usr/local/gnu
make install-info prefix=$RPM_BUILD_ROOT/usr/local/gnu
find $RPM_BUILD_ROOT -name c++filt\* | xargs rm -f

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/binutils.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/ld.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/as.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/gasp.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/gprof.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/binutils.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/ld.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/as.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/gasp.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/gprof.info
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING COPYING.LIB README
/usr/local/gnu/bin/*
/usr/local/gnu/%{sparc_arch}/bin/*
/usr/local/gnu/%{sparc_arch}/lib/ldscripts/*
/usr/local/gnu/info/binutils.*
/usr/local/gnu/info/ld.*
/usr/local/gnu/info/as.*
/usr/local/gnu/info/gasp.*
/usr/local/gnu/info/gprof.*
