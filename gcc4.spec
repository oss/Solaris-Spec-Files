%include machine-header.spec

%define gcc_version 4.4.1
%define gcc_release 1
%define stdcxx_version 6.0.12
%define stdcxx_release 1

Name:		gcc
Version:	%{gcc_version}
Release:	%{gcc_release}
Group:          Development/Compilers
License:	GPL
URL:		http://gcc.gnu.org
Source:         ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.bz2
Patch:		gcc-4.4.1-libgcc_rpath.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  texinfo python bison gmp-devel64 mpfr-devel

Requires:	libstdc++-v6-devel = %{stdcxx_version}-%{stdcxx_release}
Requires:	gcc-libs = %{gcc_version}-%{gcc_release}

Obsoletes:	gcc3 gcc-cpp
Provides:       gcc-cpp cpp

Summary:        The GNU Compiler Collection

%description
This package contains the entire GCC distribution, 
which includes gcc, g++, gfortran, gcj, and cpp.

%package -n libstdc++-v6
Version:	%{stdcxx_version}
Release:	%{stdcxx_release}
Group:		Development/Libraries
Provides:	libstdc++
Conflicts:	libstdc++-v3, libstdc++-v4
Summary:        GNU libstdc++

%description -n libstdc++-v6
This package contains the GNU libstdc++ libraries.  

%package -n libstdc++-v6-devel
Version:	%{stdcxx_version}
Release:	%{stdcxx_release}
Group:		Development/Libraries
Requires:       libstdc++-v6 = %{stdcxx_version}-%{stdcxx_release}
Provides:	libstdc++-devel
Conflicts:	libstdc++-v3-devel, libstdc++-v4-devel
Summary:        GNU libstdc++ development files

%description -n libstdc++-v6-devel
This package contains files necessary to build C++ programs with GCC.

%package libs
Group:		Development/Libraries
Summary:        GCC libraries

%description libs
This package contains libraries needed by packages compiled using GCC.

%prep
%setup -q -n gcc-%{gcc_version}
%patch -p0

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib \
         -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
LD_RUN_PATH="/usr/local/lib:/usr/local/lib/sparcv9"
export PATH CC CXX CPPFLAGS LDFLAGS LD_RUN_PATH

# Note: gcc recommends building OUTSIDE the src tree,
# so this is what we do...

cd $RPM_BUILD_DIR
rm -rf gcc-%{gcc_version}-obj-sparc
mkdir gcc-%{gcc_version}-obj-sparc
cd gcc-%{gcc_version}-obj-sparc

../gcc-%{gcc_version}/configure 			\
	--prefix=%{_prefix}				\
	--mandir=%{_mandir}				\
	--infodir=%{_infodir}				\
	--enable-shared 				\
	--enable-threads 				\
	--with-ld=/usr/ccs/bin/ld 			\
	--with-as=/usr/ccs/bin/as 			\
	--disable-libgcj 				\
	--disable-libffi 				\
	--disable-libjava 				\
	--disable-nls 					\
	--with-gmp-include=%{_includedir}/gmp64 	\
        --with-gmp-lib=%{_libdir} 			\
        --with-mpfr-lib=%{_libdir} 			\
        --with-mpfr-include=%{_includedir}

gmake -j3

%install
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib \
         -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export PATH CC CXX CPPFLAGS LDFLAGS

rm -rf %{buildroot}

umask 022

cd $RPM_BUILD_DIR/%{name}-%{gcc_version}-obj-sparc
gmake install DESTDIR=%{buildroot}

# Remove libtool .la files
find %{buildroot} -name '*.la' -exec rm -f '{}' \;

# Remove dir file
rm -f %{buildroot}%{_infodir}/dir

# Remove libstdc++.so symlinks (needed until we stop using libstdc++ v2)
rm -f %{buildroot}%{_libdir}/libstdc++.so %{buildroot}%{_libdir}/sparcv9/libstdc++.so

# Unhardlinkify
unhardlinkify.py %{buildroot}

%clean
rm -rf %{buildroot}

%post
echo "Adding info files to index..."
if [ -x %{_bindir}/install-info ] ; then
    for i in gcc gccinstall libgomp cpp gfortran gcj cppinternals gccint; do
	echo "."
	%{_bindir}/install-info --info-dir=%{_infodir} \
	    %{_infodir}/$i.info > /dev/null 2>&1
    done
    echo "Finished!"
fi

cat<<EOF

============================================
NOTE: GCC is no longer two separate binaries
groupings for 32 and 64 bit. It is now
configured with multilib and you only need to
use /usr/local/bin/gcc with the proper flags
to build either.
============================================

EOF

%preun
echo "Removing info files from index..."
if [ -x %{_bindir}/install-info ] ; then
    for i in gcc gccinstall libgomp cpp gfortran gcj cppinternals gccint; do
	echo "."
        %{_bindir}/install-info --delete --info-dir=%{_infodir} \
            %{_infodir}/$i.info > /dev/null 2>&1
    done
    echo "Finished!"
fi

%files 
%defattr(-, root, root)
%doc README* COPYING* ChangeLog* 
%doc NEWS MAINTAINERS LAST_UPDATED
%{_bindir}/*
%{_infodir}/*.info
%{_mandir}/man*/*
%{_libexecdir}/gcc/
%{_libdir}/gcc/
%{_libdir}/*.a
%{_libdir}/sparcv9/*.a
%{_libdir}/libgomp.spec
%{_libdir}/sparcv9/libgomp.spec

%files -n libstdc++-v6
%defattr(-, root, root)
%{_libdir}/libstdc++.so.*
%{_libdir}/sparcv9/libstdc++.so.*

%files -n libstdc++-v6-devel
%defattr(-, root, root)
%{_includedir}/c++/%{gcc_version}/
#%{_libdir}/libstdc++.so
#%{_libdir}/sparcv9/libstdc++.so

%files libs
%defattr(-, root, root)
%{_libdir}/libg*.so*
%{_libdir}/libobjc.so*
%{_libdir}/libssp.so*
%{_libdir}/sparcv9/libg*.so*
%{_libdir}/sparcv9/libobjc.so*
%{_libdir}/sparcv9/libssp.so*

%changelog
* Tue Aug 25 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.1-1
- Updated to gcc 4.4.1 and libstdc++ 6.0.12
- Added gcc-4.4.1-libgcc_rpath.patch
* Wed Jun 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.4.0-1
- Updated to gcc 4.4.0 and libstdc++ 6.0.11 
- Cleaned up spec file
* Thu Jan 29 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.3.3-1
- updated to 4.3.3. and removed patches
* Tue Sep 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.3.2-1
- updated to 4.3.2 and removed patches
* Tue Jul 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.3.1-2
- added Requires for mpfr and gmp
* Tue Jul 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.3.1-1
- updated to 4.3.1, added patches to fix some sun cc specific issues 
* Fri Oct 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.2-1
- Bump 4.2.2
* Thu Oct 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.1-6
- Removed libstdc++.so
* Tue Oct 02 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.1-4
- Touch ups
* Sat Sep 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.1-2
- Attempting possible sparcv9 linker fix
- Trying out multilib
* Fri Aug 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.1-1
- Bumping to 4.2.1 and libstdc++ 6.0.9
- Uncleaing Rob's clean
* Wed Apr 26 2006 Rob Zinkov
- cleaned up spec file
* Fri Mar 03 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 3.4.5-4
- Added a version number to the gcc-libs dep
- Added a Conflict against libstdc++-v3
* Wed Feb 22 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 3.4.5-1
- Upgraded to the latest version of gcc3
- Major library change between gcc-3.3 and gcc-3.4, so -v3 became -v4
- Tweaked the spec file
