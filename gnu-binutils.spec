%include machine-header.spec

Name: 		binutils
Version: 	2.18
Release: 	1
Copyright: 	GPL
Group: 		Development/Tools
Source: 	binutils-%{version}.tar.gz
Patch:		binutils-suncc.patch
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu> 
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires: 	python, texinfo
Summary: 	GNU binutils

%description
The GNU binutils are:  addr2line, ar, as, gasp, gprof, ld, nm,
objcopy, objdump, ranlib, readelf, size, strings, and strip.

Bear in mind that the Solaris binutils are much more reliable (and
work with the v9 architecture better).

strip is NOT INCLUDED in this package as it breaks sparc ELFs. 
Use Sun strip or settle with large binaries.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local/gnu
gmake
gmake info


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu
gmake install prefix=%{buildroot}/usr/local/gnu
gmake install-info prefix=%{buildroot}/usr/local/gnu
find %{buildroot} -name c++filt\* | xargs rm -f
rm `find "%{buildroot}" -name "strip"`
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./ 


%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/as.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/binutils.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/bfd.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/configure.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/gprof.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/ld.info
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info /usr/local/gnu/info/standards.info
fi


%preun
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
                /usr/local/gnu/info/as.info
        /usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
                /usr/local/gnu/info/bfd.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		/usr/local/gnu/info/binutils.info
        /usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
                /usr/local/gnu/info/configure.info
        /usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
                /usr/local/gnu/info/gprof.info
        /usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
                /usr/local/gnu/info/ld.info
        /usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
                /usr/local/gnu/info/standards.info
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
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 2.18-1
- Added binutils-suncc.patch, updated to version 2.18
* Mon Aug 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> 2.17-1
- Cleaned up spec file, updated to 2.17
