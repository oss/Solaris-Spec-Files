%include machine-header.spec

Name: binutils
Version: 2.14
Release: 5
Copyright: GPL
Group: Development/Tools
Source: binutils-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Summary: GNU binutils
Requires: gcc
%description
The GNU binutils are:  addr2line, ar, as, gasp, gprof, ld, nm,
objcopy, objdump, ranlib, readelf, size, strings, and strip.

Bear in mind that the Solaris binutils are much more reliable (and
work with the v9 architecture better).

strip is NOT INCLUDED in this package as it breaks sparc ELFs. 
Use Sun's strip or settle with large binaries.

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
rm `find "$RPM_BUILD_ROOT" -name "strip"`
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./ 



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
/usr/local/gnu/bin/addr2line
/usr/local/gnu/bin/ar
/usr/local/gnu/bin/as
/usr/local/gnu/bin/gprof
/usr/local/gnu/bin/ld
/usr/local/gnu/bin/nm
/usr/local/gnu/bin/objcopy
/usr/local/gnu/bin/objdump
/usr/local/gnu/bin/ranlib
/usr/local/gnu/bin/readelf
/usr/local/gnu/bin/size
/usr/local/gnu/bin/strings
/usr/local/gnu/%{sparc_arch}/bin/*
/usr/local/gnu/%{sparc_arch}/lib/ldscripts/*
/usr/local/gnu/info/as.info
/usr/local/gnu/info/bfd.info
/usr/local/gnu/info/bfd.info-1
/usr/local/gnu/info/bfd.info-2
/usr/local/gnu/info/bfd.info-3
/usr/local/gnu/info/bfd.info-4
/usr/local/gnu/info/bfd.info-5
/usr/local/gnu/info/bfd.info-6
/usr/local/gnu/info/bfd.info-7
/usr/local/gnu/info/bfd.info-8
/usr/local/gnu/info/bfd.info-9
/usr/local/gnu/info/binutils.info
/usr/local/gnu/info/configure.info
/usr/local/gnu/info/configure.info-1
/usr/local/gnu/info/configure.info-2
/usr/local/gnu/info/configure.info-3
/usr/local/gnu/info/gprof.info
/usr/local/gnu/info/gprof.info-1
/usr/local/gnu/info/gprof.info-2
/usr/local/gnu/info/gprof.info-3
/usr/local/gnu/info/ld.info
