%include machine-header.spec

%define prefix /usr/local/gcc3
%define stdc_version 5.0.4
%define gcc_version 3.3
%define overall_release 2

Name: gcc
Version: %{gcc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: The GNU C compiler
BuildRoot: %{_tmppath}/%{name}-root
Source: gcc-%{gcc_version}.tar.bz2
Requires: libstdc++-v3 = %{stdc_version}
Provides: gcc-cpp cpp
#Provides: libstdc++.so.%{stdc_version} libstdc++.so
BuildRequires: texinfo fileutils make
#%if %{max_bits} == 64
#BuildRequires: vpkg-SUNWarcx
#%endif
#Conflicts: vpkg-SFWgcc
Obsoletes: gcc3 gcc-cpp

%description
This package contains the entire gcc distribution -- it includes gcc,
g++, g77, gcj, and cpp. (libstdc++ is provided separately due to apt's
dependency on it)



%package -n libstdc++-v3
Version: %{stdc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++
Provides: libstdc++.so.%{stdc_version} libstdc++.so libstdc++

%description -n libstdc++-v3
This package contains just the libstdc++ libraries.  
package by all other distros. gcc3 requires this package

%package -n libstdc++-v3-devel
Version: %{stdc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++ devel
Provides: libstdc++-devel

%description -n libstdc++-v3-devel
c++ devel

%prep
%setup -q -n gcc-%{gcc_version}

%build

PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/bin:/bin"
LD_RUN_PATH="/usr/local/gcc3/lib:/usr/local/lib"
export PATH LD_RUN_PATH

%ifarch sparc64

mkdir obj-sparc64
cd obj-sparc64
LD_RUN_PATH="/usr/local/gcc3/lib/sparcv9:/usr/local/lib/sparcv9"
export LD_RUN_PATH

../configure --enable-shared --enable-threads --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --disable-libgcj --disable-libffi --disable-libjava --disable-nls --prefix=/usr/local/gcc3 sparcv9-sun-%{sol_os}

gmake || gmake

unset LD_RUN_PATH

echo Completed building sparcv9 part

cd ..

%endif

mkdir obj-sparc
cd obj-sparc
LD_RUN_PATH="/usr/local/gcc3/lib:/usr/local/lib"
export LD_RUN_PATH
../configure --enable-shared --enable-threads --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --disable-multilib --disable-libgcj --disable-libffi --disable-libjava --disable-nls --prefix=/usr/local/gcc3 sparc-sun-%{sol_os}


gmake || gmake
cd ..

%install
# PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
# export PATH
# cd %{build_subdir}
# umask 022

rm -rf %{buildroot}

# install sparcv9 parts if that's the platform we're on
%ifarch sparc64
cd obj-sparc64
gmake install prefix=%{buildroot}/usr/local/
cd ..
%endif

# always install sparcv7 parts
cd obj-sparc
gmake install prefix=%{buildroot}/usr/local/
cd ..


# let's move some files around...
cd %{buildroot}

# .la files make my tummy hurt
rm -f `find . -name \*.la`

# get rid of the dir file
rm usr/local/info/dir


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
/usr/local/bin
/usr/local/lib/gcc-lib
/usr/local/man/man*/*
/usr/local/info/*
/usr/local/lib/libfrtbegin.a
/usr/local/lib/libg*
/usr/local/lib/libiberty.a
/usr/local/lib/libobjc*
/usr/local/lib/libstdc++.a
/usr/local/lib/libsupc++.a
%ifarch sparc64
/usr/local/lib/sparcv7/libiberty.a
/usr/local/lib/sparcv9/libfrtbegin.a
/usr/local/lib/sparcv9/libg*
/usr/local/lib/sparcv9/libobjc*
/usr/local/lib/sparcv9/libstdc++.a
/usr/local/lib/sparcv9/libsupc++.a
%endif

%files -n libstdc++-v3
%defattr(-, root, bin)
/usr/local/lib/libstdc++.so.5*
%config(noreplace) /usr/local/lib/libstdc++.so
%ifarch sparc64
/usr/local/lib/sparcv9/libstdc++.so.5*
%config(noreplace) /usr/local/lib/sparcv9/libstdc++.so
%endif

%files -n libstdc++-v3-devel
%defattr(-, root, bin)
/usr/local/include/c++








