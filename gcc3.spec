%include machine-header.spec

%define prefix /usr/local/gcc-3.0.4
%define stdc_version 3.0.4
%define gcc_version 3.0.4

Name: gcc3
Version: %{gcc_version}
Release: 5
Copyright: GPL
Group: Development/Languages
Summary: The GNU C compiler
BuildRoot: %{_tmppath}/%{name}-root
Source: gcc-%{gcc_version}.tar.gz
Requires: libstdc++ = %{gcc_version}-%{release}
Provides: cpp
#Provides: libstdc++.so.%{stdc_version} libstdc++.so
BuildRequires: texinfo fileutils make
#%if %{max_bits} == 64
#BuildRequires: vpkg-SUNWarcx
#%endif
#Conflicts: vpkg-SFWgcc

%description
This package contains the entire gcc distribution -- it includes gcc,
g++, g77, gcj, cpp, and libstdc++.



%package -n libstdc++
Version: %{stdc_version}
Release: 3
Copyright: GPL
Group: Development/Languages
Summary: GNU libstdc++
Provides: libstdc++.so.%{stdc_version} libstdc++.so
Obsoletes: libstdc++-v3

%description -n libstdc++
This package contains just the libstdc++ libraries.  
package by all other distros. gcc3 requires this package



%prep
%setup -q -n gcc-%{gcc_version}

#%define build_subdir  obj-sparc-solaris

%ifarch sparc64
./configure --prefix=%{prefix} --enable-shared --enable-threads --with-as=/usr/local/gnu/bin/as --with-ld=/usr/local/gnu/bin/ld sparcv9-sun-%{sol_os}
%else
./configure --prefix=%{prefix} --enable-shared --enable-threads --with-as=/usr/local/gnu/bin/as --with-ld=/usr/local/gnu/bin/ld
%endif


%build
#PATH="/usr/local/bin:/usr/ccs/bin:/usr/bin:/usr/local/gnu/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
#export PATH
#rm -rf %{build_subdir}
#mkdir -p %{build_subdir}
#cd %{build_subdir}
#%ifarch sparc64
#./configure --prefix=%{prefix} --enable-shared --enable-threads \
#  sparcv9-sun-%{sol_os} --with-as=/usr/local/gnu/bin/as \
#  --with-ld=/usr/local/gnu/bin/ld
#%else
#./configure --prefix=%{prefix} --enable-shared --enable-threads \
#  --with-as=/usr/local/gnu/bin/as  --with-ld=/usr/local/gnu/bin/ld
#%endif

make

%install
#PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
#export PATH
#cd %{build_subdir}
#umask 022
#rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix} %{buildroot}/usr/lib
make install prefix=%{buildroot}%{prefix}
cp %{buildroot}%{prefix}/lib/libstdc++.so.%{stdc_version} \
   %{buildroot}/usr/lib/libstd++.so.%{stdc_version}
rm -f %{buildroot}%{prefix}/info/dir

RETDIR=/usr/local/src/rpm-packages/BUILD/gcc-3.0.4/
export RETDIR

cd %{buildroot}
mkdir -p usr/local/
rm -rf usr/local/gcc3
ln -sf usr/local/gcc-%{gcc_version} usr/local/gcc3

cd %{buildroot}
#find ./ -type f | grep -v cpp | sed "s/.//" > /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-gcc
#find ./ -type l | grep -v cpp | sed "s/.//" >> /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-gcc
#find ./ -name "cpp" -type f | sed "s/.//" > /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-cpp
#find ./ -name "cpp" -type l | sed "s/.//" >> /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-cpp
find ./ -name "libstdc++*" -type f | sed "s/.//" > /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-libstdc
find ./ -name "libstdc++*" -type l | sed "s/.//" >> /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-libstdc


%post
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals ; do
        /usr/local/bin/install-info --info-dir=%{prefix}/info \
 	     %{prefix}/info/$i.info
    done
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
    for i in gcc cpp g77 gcj cppinternals ; do
        /usr/local/bin/install-info --delete --info-dir=%{prefix}/info \
	    %{prefix}/info/$i.info
    done
fi

#%post -n cpp
#if [ -x /usr/local/bin/install-info ] ; then
#    /usr/local/bin/install-info --info-dir=%{prefix}/info \
#       %{prefix}/info/cpp.info
#fi

#%preun -n cpp
#if [ -x /usr/local/bin/install-info ] ; then
#    /usr/local/bin/install-info --delete --info-dir=%{prefix}/info \
#       %{prefix}/info/cpp.info
#fi


%clean
rm -rf %{buildroot}

%files #-f filelist-gcc
%defattr(-, root, bin)
%doc COPYING
%{prefix}
/usr/local/gcc3
/usr/lib/*

%files -n libstdc++ -f filelist-libstdc
%defattr(-, root, bin)
#/usr/lib/*.so*
#%{prefix}/lib/libstdc++.so*
#%ifarch sparc64
#%{prefix}/lib/sparcv7/libstdc++.so*
#%endif
