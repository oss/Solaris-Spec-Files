Summary: Tag Image File Format (TIFF) graphics library
Name: libtiff
Version: 3.7.4
Release: 1
Group: Development/Libraries
License: BSD-type
Source: tiff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
#Obsoletes: tiff
#can't obsolete due to sun vpkg
Provides: tiff
%ifarch sparc64
Provides: %{name}-sparc64
BuildRequires: gcc >= 3.0
%endif

%description
This software provides support for the Tag Image File Format (TIFF), a
widely used format for storing image data. The latest version of the
TIFF specification is available on-line in several different formats,
as are a number of Technical Notes (TTNs).

Included in this software distribution is a library, libtiff, for
reading and writing TIFF, a small collection of tools for doing simple
manipulations of TIFF images on UNIX systems, and documentation on the
library and tools. A small assortment of TIFF-related software for
UNIX that has been contributed by others is also included.

%package devel
Summary: %{name} include files, etc.
Requires: %{name}
Group: Development
%description devel
%{name} include files, etc.

%prep
%setup -q -n tiff-%{version}

%build

./configure < /dev/null   # interactive no more!
make

%ifarch sparc64
mkdir -p sparc32
cp libtiff/libtiff.so sparc32/
make clean
LD_LIBRARY_PATH="/usr/local/lib/sparcv9"
LD_RUN_PATH="/usr/local/lib/sparcv9"
LD=/usr/ccs/bin/ld 
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
#CC="/usr/local/gcc3/bin/gcc"
CC="gcc"
export LD_LIBRARY_PATH LD_RUN_PATH LD CC LDFLAGS
./configure < /dev/null   # interactive no more!
mv tools/Makefile tools/Makefile.stupid
cat tools/Makefile.stupid | sed "s/\/usr\/local\/lib/\/usr\/local\/lib\/sparcv9/g" > tools/Makefile
make
%endif

%install
rm -rf $RPM_BUILD_ROOT
for i in include lib bin man/man1 man/man3 ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done

for i in tiff.h tiffio.h tiffconf.h tiffvers.h; do
    install -m 0444 libtiff/$i $RPM_BUILD_ROOT/usr/local/include
done

install -m 0444 libtiff/libtiff.a $RPM_BUILD_ROOT/usr/local/lib
/usr/ccs/bin/strip libtiff/libtiff.so

%ifarch sparc64
/usr/ccs/bin/strip sparc32/libtiff.so
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
install -m 0555 libtiff/libtiff.so $RPM_BUILD_ROOT/usr/local/lib/sparcv9
install -m 0555 sparc32/libtiff.so $RPM_BUILD_ROOT/usr/local/lib
%else
install -m 0555 libtiff/libtiff.so $RPM_BUILD_ROOT/usr/local/lib
%endif

for i in fax2tiff fax2ps gif2tiff pal2rgb ppm2tiff rgb2ycbcr thumbnail \
         ras2tiff tiff2bw tiff2rgba tiff2ps tiffcmp tiffcp tiffdither \
         tiffdump tiffinfo tiffmedian tiffsplit ; do
    /usr/ccs/bin/strip tools/$i
    install -m 0555 tools/$i $RPM_BUILD_ROOT/usr/local/bin
done

for i in `find man -name \*1` ; do
    install -m 0444 $i $RPM_BUILD_ROOT/usr/local/man/man1
done

for i in `find man -name \*3t` ; do
    f=`basename $i t`
    install -m 0444 $i $RPM_BUILD_ROOT/usr/local/man/man3/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/*.so
/usr/local/bin/*
/usr/local/man/man1/*
%ifarch sparc64
/usr/local/lib/sparcv9/*.so
%endif

%files devel
%defattr(-,root,other)
/usr/local/lib/*.a
/usr/local/man/man3/*
/usr/local/include/*


