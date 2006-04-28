%include machine-header.spec


%define stdc_version 6.0.8
%define gcc_version 4.0.3
%define overall_release 4


Name: gcc
Version: %{gcc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: The GNU Compiler Collection
BuildRoot: %{_tmppath}/%{name}-root
Source: gcc-%{gcc_version}.tar.gz
Requires: libstdc++-v6 = %{stdc_version} libstdc++-v6-devel = %{stdc_version} gcc-libs = %{gcc_version}
Provides: gcc-cpp cpp
BuildRequires: texinfo fileutils make python
Obsoletes: gcc3 gcc-cpp
%description
This package contains the entire gcc distribution -- it includes gcc,
g++, g77, gcj, and cpp. (libstdc++ is provided separately due to apt
having a dependency on it)


%package -n libstdc++-v6
Version: %{stdc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++
Provides: libstdc++.so.%{stdc_version} libstdc++.so libstdc++
Conflicts: libstdc++-v3, libstdc++-v4
%description -n libstdc++-v6
This package contains just the libstdc++ libraries.  
package by all other distros. gcc3 requires this package


%package -n libstdc++-v6-devel
Version: %{stdc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++ devel
Provides: libstdc++-devel
Conflicts: libstdc++-v3-devel, libstdc++-v4-devel
%description -n libstdc++-v6-devel
c++ devel


%package libs
Summary: gcc libs
Group: Development/Libraries
%description libs
Libraries needed by packages compiled by gcc


%prep

PATH="/usr/sfw/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin:/bin"
LD_RUN_PATH="/usr/local/lib/sparcv9:/usr/local/lib"
export PATH LD_RUN_PATH

%setup -q -n gcc-%{gcc_version}


%build

PATH="/usr/sfw/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin:/bin"
LD_RUN_PATH="/usr/local/lib/sparcv9:/usr/local/lib"
export PATH LD_RUN_PATH

%ifarch sparc64
   mkdir obj-sparc64
   cd obj-sparc64

   LD_RUN_PATH="/usr/local/lib/sparcv9:/usr/local/lib"
   export LD_RUN_PATH

  ../configure --enable-shared --enable-threads --with-ld=/usr/local/gnu/bin/ld \
                --with-as=/usr/local/gnu/bin/as --disable-multilib --disable-libgcj \
                --disable-libffi --disable-libjava \
                --disable-nls \
                --bindir=/usr/local/bin/sparcv9 \
		--libdir=/usr/local/lib/sparcv9 \

   gmake

   echo Completed building sparcv9 part

   cd ..
%endif

mkdir obj-sparc
cd obj-sparc
LD_RUN_PATH="/usr/local/lib"
export LD_RUN_PATH

../configure --enable-shared --enable-threads --with-ld=/usr/ccs/bin/ld \
             --with-as=/usr/ccs/bin/as --disable-multilib --disable-libgcj \
             --disable-libffi --disable-libjava \
             --disable-nls sparc-sun-%{sol_os}

gmake


%install
PATH="/usr/sfw/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
export PATH
umask 022

# install sparcv9 parts if that's the platform we're on
%ifarch sparc64
   cd obj-sparc64
   gmake install DESTDIR=%{buildroot}
   cd ..
%endif

# always install sparcv8 parts
cd obj-sparc
gmake install DESTDIR=%{buildroot}
cd ..

# let's move some files around...
cd %{buildroot}

# .la files make my tummy hurt
rm -f `find . -name \*.la`

# get rid of the dir file
rm %{buildroot}/usr/local/info/dir

# hardlink badness GO AWAY
cd %{buildroot}/usr/local
/usr/local/bin/unhardlinkify.py ./


%post
echo -n Adding info files to index...
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals fastjar gccint; do
	echo -n .
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	    /usr/local/info/$i.info  &> /dev/null
    done
    echo
fi


%preun
echo -n Removing info files from index...
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals fastjar gccint; do
	echo -n .
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
            /usr/local/info/$i.info &> /dev/null
    done
    echo
fi


%clean
rm -rf %{buildroot}


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
%ifarch sparc64
   /usr/local/lib/sparcv9/*.a
%endif



%files -n libstdc++-v6
%defattr(-, root, bin)
/usr/local/lib/libstdc++.so.*
%config(noreplace) /usr/local/lib/libstdc++.so
%ifarch sparc64
   /usr/local/lib/sparcv9/libstdc++.so.*
   %config(noreplace) /usr/local/lib/sparcv9/libstdc++.so
%endif


%files -n libstdc++-v6-devel
%defattr(-, root, bin)
/usr/local/include/c++/%{gcc_version}/*


%files libs
%defattr(-, root, bin)
/usr/local/lib/libg*.so*
/usr/local/lib/libobjc.so*
%ifarch sparc64
   /usr/local/lib/sparcv9/libg*.so*
   /usr/local/lib/sparcv9/libobjc.so*
%endif


%changelog
* Wed Apr 26 2006 Rob Zinkov
- cleaned up spec file
* Fri Mar 03 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 3.4.5-4
- Added a version number to the gcc-libs dep
- Added a Conflict against libstdc++-v3
* Wed Feb 22 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 3.4.5-1
- Upgraded to the latest version of gcc3
- Major library change between gcc-3.3 and gcc-3.4, so -v3 became -v4
- Tweaked the spec file
