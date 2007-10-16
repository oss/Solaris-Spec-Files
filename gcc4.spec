%include machine-header.spec

%define stdc_version 6.0.9
%define gcc_version 4.2.2
%define gcc_release 1
%define stdc_release 9

Name:		gcc
Version:	%{gcc_version}
Release:	%{gcc_release}
License:	GPL
Group:		Development/Languages
Summary:	The GNU Compiler Collection
BuildRoot:	%{_tmppath}/%{name}-root
Source:		gcc-%{gcc_version}.tar.bz2
Requires:	libstdc++-v6 = %{stdc_version}, libstdc++-v6-devel = %{stdc_version}, gcc-libs = %{gcc_version}
Provides:	gcc-cpp cpp
BuildRequires:	texinfo fileutils make python bison
Obsoletes:	gcc3 gcc-cpp
%description
This package contains the entire gcc distribution -- it includes gcc,
g++, g77, gcj, and cpp. (libstdc++ is provided separately due to apt
having a dependency on it)

%package -n libstdc++-v6
Version:	%{stdc_version}
Release:	%{stdc_release}
License:	GPL
Group:		Development/Languages
Summary:	GNU libstdc++
Provides:	libstdc++.so.%{stdc_version} libstdc++.so libstdc++
Conflicts:	libstdc++-v3, libstdc++-v4
%description -n libstdc++-v6
This package contains just the libstdc++ libraries.  
package by all other distros. gcc3 requires this package

%package -n libstdc++-v6-devel
Version:	%{stdc_version}
Release:	%{stdc_release}
License:	GPL
Group:		Development/Languages
Summary:	GNU libstdc++ devel
Provides:	libstdc++-devel
Conflicts:	libstdc++-v3-devel, libstdc++-v4-devel
%description -n libstdc++-v6-devel
c++ devel

%package libs
Summary: gcc libs
Group: Development/Libraries
%description libs
Libraries needed by packages compiled by gcc

%prep
%setup -q -n gcc-%{gcc_version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export PATH CC CXX CPPFLAGS LD LDFLAGS

# Note: gcc recommends building OUTSIDE the src tree,
# so this is what we do...

cd ..
rm -rf %{name}-%{gcc_version}-obj-sparc
mkdir %{name}-%{gcc_version}-obj-sparc
cd %{name}-%{gcc_version}-obj-sparc

LD_RUN_PATH="/usr/local/lib:/usr/local/lib/sparcv9"
export LD_RUN_PATH

../%{name}-%{gcc_version}/configure \
	--enable-shared \
	--enable-threads \
	--with-ld=/usr/ccs/bin/ld \
	--with-as=/usr/ccs/bin/as \
	--disable-libgcj \
	--disable-libffi \
	--disable-libjava \
	--disable-nls

gmake -j2

#unset LD_RUN_PATH

cd ../%{name}-%{gcc_version}

%install
PATH="/usr/local/gnu/bin:/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export PATH CC CXX CPPFLAGS LD LDFLAGS

umask 022

cd ../%{name}-%{gcc_version}-obj-sparc
gmake install DESTDIR=%{buildroot}
cd ../%{name}-%{gcc_version}

# let's move some files around...
cd %{buildroot}

# .la files make my tummy hurt
rm -f `find . -name \*.la`

# get rid of the dir file
rm %{buildroot}/usr/local/info/dir

# hardlink badness GO AWAY
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./

cd %{buildroot}/usr/local/lib/
rm -f libstdc++.so
cd sparcv9/
rm -f libstdc++.so

%post
echo "Adding info files to index..."
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals fastjar gccint; do
	echo "."
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	    /usr/local/info/$i.info  &> /dev/null
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
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals fastjar gccint; do
	echo "."
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
            /usr/local/info/$i.info &> /dev/null
    done
    echo "Finished!"
fi

%clean
rm -rf %{buildroot}
rm -rf /usr/local/src/rpm-packages/BUILD/%{name}-%{gcc_version}-obj-sparc

%files 
%defattr(-, root, bin)
%doc COPYING
/usr/local/bin/*
/usr/local/info/*.info
/usr/local/man/man1/*.1
/usr/local/man/man7/*.7
/usr/local/lib/*.a
/usr/local/libexec/gcc/*/%{gcc_version}/*
/usr/local/lib/gcc/*/%{gcc_version}/*
/usr/local/lib/libgomp.spec
/usr/local/lib/sparcv9/*.a
/usr/local/lib/sparcv9/libgomp.spec

%files -n libstdc++-v6
%defattr(-, root, bin)
/usr/local/lib/libstdc++.so.*
/usr/local/lib/sparcv9/libstdc++.so.*

%files -n libstdc++-v6-devel
%defattr(-, root, bin)
/usr/local/include/c++/%{gcc_version}/*

%files libs
%defattr(-, root, bin)
/usr/local/lib/libg*.so*
/usr/local/lib/libobjc.so*
/usr/local/lib/libssp.so*
/usr/local/lib/sparcv9/libg*.so*
/usr/local/lib/sparcv9/libobjc.so*
/usr/local/lib/sparcv9/libssp.so*

%changelog
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
