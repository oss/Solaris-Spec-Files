%include machine-header.spec

%define prefix /usr/local/gcc-3.2
%define stdc_version 5.0.1
%define gcc_version 3.2.1
%define overall_release 5

Name: gcc3
Version: %{gcc_version}
Release: %{overall_release}
Copyright: GPL
Group: Development/Languages
Summary: The GNU C compiler
BuildRoot: %{_tmppath}/%{name}-root
Source: gcc-%{gcc_version}.tar.bz2
Requires: libstdc++-v3 = %{stdc_version}
Provides: cpp
#Provides: libstdc++.so.%{stdc_version} libstdc++.so
BuildRequires: texinfo fileutils make
#%if %{max_bits} == 64
#BuildRequires: vpkg-SUNWarcx
#%endif
#Conflicts: vpkg-SFWgcc

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
Provides: libstdc++.so.%{stdc_version} libstdc++.so

%description -n libstdc++-v3
This package contains just the libstdc++ libraries.  
package by all other distros. gcc3 requires this package



%prep
%setup -q -n gcc-%{gcc_version}

#%define build_subdir  obj-sparc-solaris

PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/bin:/bin"
LD_RUN_PATH="/usr/local/gcc3/lib:/usr/local/lib"
export PATH LD_RUN_PATH

%ifarch sparc64

./configure --enable-shared --enable-threads --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --disable-libgcj --disable-libffi --disable-libjava --disable-nls sparcv9-sun-%{sol_os}

cd sparcv9-sun-solaris*
ln -s ../include/ ./
cd ../gcc
ln -s config/sparc* config/dbxelf.h config/elfos.h config/svr4.h ./
cd ..

%else

./configure --enable-shared --enable-threads --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --disable-multilib --disable-libgcj --disable-libffi --disable-libjava --disable-nls sparc-sun-%{sol_os}

cd sparc-sun-solaris*
ln -s ../include/ ./
cd ../gcc
ln -s config/sparc config/dbxelf.h config/elfos.h config/svr4.h ./
cd ..

%endif


#worked for sparc64 a while ago: ./configure --prefix=%{prefix} --enable-shared --enable-threads --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --disable-libgcj --disable-libffi --disable-libjava sparc-sun-%{sol_os}

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
# PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin"
# export PATH
# cd %{build_subdir}
# umask 022

rm -rf %{buildroot}

#mkdir -p %{buildroot}%{prefix} %{buildroot}/usr/local/lib

make install prefix=%{buildroot}/usr/local
mkdir -p %{buildroot}/usr/local/gcc-3.2.1
ln -sf gcc-3.2.1 %{buildroot}/usr/local/gcc3
mv %{buildroot}/usr/local/bin %{buildroot}/usr/local/gcc3/
mv %{buildroot}/usr/local/lib %{buildroot}/usr/local/gcc3/
mv %{buildroot}/usr/local/man %{buildroot}/usr/local/gcc3/
mv %{buildroot}/usr/local/info %{buildroot}/usr/local/gcc3/

mkdir %{buildroot}/usr/local/lib
mv %{buildroot}/usr/local/gcc3/lib/libstdc*.so* %{buildroot}/usr/local/lib

#cd %{buildroot}
#rm -rf %{buildroot}/usr/lib
#rm -rf %{buildroot}/usr/local/lib
#mv bin include info lib man share %{buildroot}/usr/local/
#mv %{buildroot}/usr/local/bin/gcc %{buildroot}/usr/local/bin/gcc3


# cp %{buildroot}%{prefix}/lib/libstdc++.so.%{stdc_version} \
#   %{buildroot}/usr/lib/libstd++.so.%{stdc_version}
# rm -f %{buildroot}%{prefix}/info/dir
# RETDIR=/usr/local/src/rpm-packages/BUILD/gcc-3.2/
# export RETDIR
# cd %{buildroot}
# mkdir -p usr/local/
# rm -rf usr/local/gcc3
# ln -sf usr/local/gcc-%{gcc_version} usr/local/gcc3
# cd %{buildroot}
# find ./ -type f | grep -v cpp | sed "s/.//" > /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-gcc
# find ./ -type l | grep -v cpp | sed "s/.//" >> /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-gcc
# find ./ -name "cpp" -type f | sed "s/.//" > /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-cpp
# find ./ -name "cpp" -type l | sed "s/.//" >> /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-cpp
# find ./ -name "libstdc++*" -type f | sed "s/.//" > /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-libstdc
# find ./ -name "libstdc++*" -type l | sed "s/.//" >> /usr/local/src/rpm-packages/BUILD/gcc-3.0.4/filelist-libstdc


#%post
#if [ -x /usr/local/bin/install-info ] ; then
#    for i in gcc cpp g77 gcj cppinternals ; do
#        /usr/local/bin/install-info --info-dir=%{prefix}/info \
# 	     %{prefix}/info/$i.info
#    done
#fi

#%preun
#if [ -x /usr/local/bin/install-info ] ; then
#    for i in gcc cpp g77 gcj cppinternals ; do
#        /usr/local/bin/install-info --delete --info-dir=%{prefix}/info \
#	    %{prefix}/info/$i.info
#    done
#fi

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

%files 
%defattr(-, root, bin)
%doc COPYING
/usr/local/gcc3
/usr/local/gcc-%{gcc_version}/bin/c++
/usr/local/gcc-%{gcc_version}/bin/c++filt
/usr/local/gcc-%{gcc_version}/bin/cpp
/usr/local/gcc-%{gcc_version}/bin/g++
/usr/local/gcc-%{gcc_version}/bin/g77
/usr/local/gcc-%{gcc_version}/bin/gcc
/usr/local/gcc-%{gcc_version}/bin/gccbug
/usr/local/gcc-%{gcc_version}/bin/gcj
/usr/local/gcc-%{gcc_version}/bin/gcjh
/usr/local/gcc-%{gcc_version}/bin/gcov
/usr/local/gcc-%{gcc_version}/bin/grepjar
/usr/local/gcc-%{gcc_version}/bin/jar
/usr/local/gcc-%{gcc_version}/bin/jcf-dump
/usr/local/gcc-%{gcc_version}/bin/jv-scan
/usr/local/gcc-%{gcc_version}/bin/sparc*
/usr/local/include/c++/3.2.1
/usr/local/gcc-%{gcc_version}/info
#/usr/local/info/cpp.info*
#/usr/local/info/cppinternals.info
#/usr/local/info/g77.info*
#/usr/local/info/gcc.info*
#/usr/local/info/gccint.info*
#/usr/local/info/gcj.info*
#/usr/local/lib/charset.alias
/usr/local/gcc-%{gcc_version}/lib/gcc-lib/*
/usr/local/gcc-%{gcc_version}/lib/libfrtbegin.a
/usr/local/gcc-%{gcc_version}/lib/libg2c.a
/usr/local/gcc-%{gcc_version}/lib/libg2c.la
/usr/local/gcc-%{gcc_version}/lib/libg2c.so
/usr/local/gcc-%{gcc_version}/lib/libg2c.so.0
/usr/local/gcc-%{gcc_version}/lib/libg2c.so.0.0.0
/usr/local/gcc-%{gcc_version}/lib/libgcc*
/usr/local/gcc-%{gcc_version}/lib/libiberty.a
/usr/local/gcc-%{gcc_version}/lib/libobjc.a
/usr/local/gcc-%{gcc_version}/lib/libobjc.la
/usr/local/gcc-%{gcc_version}/lib/libobjc.so
/usr/local/gcc-%{gcc_version}/lib/libobjc.so.1
/usr/local/gcc-%{gcc_version}/lib/libobjc.so.1.0.0
/usr/local/gcc-%{gcc_version}/lib/libstdc++.a
/usr/local/gcc-%{gcc_version}/lib/libstdc++.la
/usr/local/gcc-%{gcc_version}/lib/libsupc++.a
/usr/local/gcc-%{gcc_version}/lib/libsupc++.la
%ifarch sparc64
/usr/local/gcc-%{gcc_version}/lib/sparc*
%endif
/usr/local/gcc-%{gcc_version}/man
#/usr/local/man/man1/cpp.1
#/usr/local/man/man1/g++.1
#/usr/local/man/man1/g77.1
#/usr/local/man/man1/gcc.1
#/usr/local/man/man1/gcj.1
#/usr/local/man/man1/gcjh.1
#/usr/local/man/man1/gcov.1
#/usr/local/man/man1/gij.1
#/usr/local/man/man1/jcf-dump.1
#/usr/local/man/man1/jv-convert.1
#/usr/local/man/man1/jv-scan.1
#/usr/local/man/man1/rmic.1
#/usr/local/man/man1/rmiregistry.1
#/usr/local/man/man7/fsf-funding.7
#/usr/local/man/man7/gfdl.7
#/usr/local/man/man7/gpl.7


%files -n libstdc++-v3
%defattr(-, root, bin)
/usr/local/lib/libstdc++.so.5.0.1
/usr/local/lib/libstdc++.so.5
%config(noreplace) /usr/local/lib/libstdc++.so