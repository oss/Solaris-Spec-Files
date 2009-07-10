%define ltdlver_full 7.2.0
%define ltdlver_major 7

Name:		libtool
Version:	2.2.6
Release:	1
Group:		Development/Utilities
License:	GPL
URL:		http://www.gnu.org/software/libtool
Source:		ftp://ftp.gnu.org/gnu/libtool/libtool-%{version}a.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	m4

Summary:	A generic library support script

%description
GNU libtool is a generic library support script. Libtool hides the complexity 
of using shared libraries behind a consistent, portable interface. 

%package devel
Summary:	Libtool development files
Group:		Development/Utilities
Requires:	libtool = %{version}-%{release}

%description devel
This package contains files needed to build applications that use the libtool 
ltdl library.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
export PATH CC CXX

%ifarch sparc64
CFLAGS="-xtarget=ultra -xarch=v9 -g -xs" CXXFLAGS="${CFLAGS}"
CPPFLAGS="-I/usr/local/include/sparcv9"
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export CFLAGS CXXFLAGS CPPFLAGS LDFLAGS

./configure --disable-static

gmake -j3

mkdir sparcv9
cp libltdl/.libs/*.so.* sparcv9/

gmake clean
%endif

CFLAGS="-g -xs" CXXFLAGS="${CFLAGS}"
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export CFLAGS CXXFLAGS CPPFLAGS LDFLAGS

./configure			\
	--prefix=%{_prefix}	\
	--infodir=%{_infodir}	\
	--disable-static

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

%ifarch sparc64
%{__install} -d %{buildroot}%{_libdir}/sparcv9
%{__install} -m 0755 sparcv9/libltdl.so.%{ltdlver_full} %{buildroot}%{_libdir}/sparcv9/

cd %{buildroot}%{_libdir}/sparcv9
ln -s libltdl.so.%{ltdlver_full} libltdl.so.%{ltdlver_major}
ln -s libltdl.so.%{ltdlver_major} libltdl.so
%endif

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ] ; then
    %{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/libtool.info
fi

%preun
if [ -x %{_bindir}/install-info ] ; then
    %{_bindir}/install-info --info-dir=%{_infodir} --delete %{_infodir}/libtool.info
fi

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS THANKS
%doc ChangeLog* NEWS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/*
%dir %{_datadir}/libtool
%{_datadir}/libtool/config/
%{_datadir}/aclocal/*
%ifarch sparc64
%{_libdir}/sparcv9/*.so.*
%endif

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_datadir}/libtool/libltdl/
%{_libdir}/*.so
%ifarch sparc64
%{_libdir}/sparcv9/*.so
%endif

%changelog
* Fri Jul 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.2.6-1
- Updated to version 2.2.6 
- Changes/Fixes
* Fri Feb 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.5.26-2
- removed install-info post and pre scripts
* Mon Feb 04 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.5.26-1
- updated to latest version and changed libltdl.so.3.1.5 to 3.1.6 
* Mon Aug 27 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.24-3
- Created break out packages
* Mon Aug 27 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.5.24-2
- Fixed 64-bit binaries
* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.5.24-1
- Bump to 1.5.24
* Thu Dec 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5.22-2
- Got rid of static libraries from file
- Put proper build flags in place
* Tue Jun 27 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> 1.5.22-1
 - Updated to the latest version
