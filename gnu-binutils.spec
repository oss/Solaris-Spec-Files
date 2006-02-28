%include machine-header.spec

Name: binutils
Version: 2.16.1
Release: 2
Copyright: GPL
Group: Development/Tools
Source: binutils-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: python
Summary: GNU binutils
%description
The GNU binutils are:  addr2line, ar, as, gasp, gprof, ld, nm,
objcopy, objdump, ranlib, readelf, size, strings, and strip.

Bear in mind that the Solaris binutils are much more reliable (and
work with the v9 architecture better).

strip is NOT INCLUDED in this package as it breaks sparc ELFs. 
Use Sun strip or settle with large binaries.

%prep
%setup -q


%build
./configure --prefix=/usr/local/gnu
make
make info


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
make install prefix=%{buildroot}/usr/local/gnu
make install-info prefix=%{buildroot}/usr/local/gnu
find %{buildroot} -name c++filt\* | xargs rm -f
rm `find "%{buildroot}" -name "strip"`
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
rm -rf %{buildroot}


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
/usr/local/gnu/info/*
/usr/local/gnu/include/*
/usr/local/gnu/lib/*
/usr/local/gnu/man/*
/usr/local/gnu/share/*


%changelog
* Mon Feb 27 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 2.16.1-2
- Removed gcc as a requirement, because it is not (or is no longer)