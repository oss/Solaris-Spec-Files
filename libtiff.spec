Summary: Tag Image File Format (TIFF) graphics library
Name: libtiff
Version: 3.5.7
Release: 0
Group: Development/Libraries
License: BSD-type
Source: ftp://ftp.remotesensing.org/pub/libtiff/tiff-v3.5.7.tar.gz
BuildRoot: /var/tmp/%{name}-root
Obsoletes: tiff
Provides: tiff

%description
This software provides support for the Tag Image File Format (TIFF), a
widely used format for storing image data. The latest version of the
TIFF specification is available on-line in several different formats,
as are a number of Technical Notes (TTN's).

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
%setup -q -n tiff-v%{version}

%build
PATH="/usr/openwin/bin:/usr/bin:/usr/ccs/bin:/usr/local/bin:/opt/SUNWspro/bin:/usr/sbin"
export PATH
./configure < /dev/null   # interactive no more!
make

%install
rm -rf $RPM_BUILD_ROOT
for i in include lib bin man/man1 man/man3 ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done

for i in tiff.h tiffio.h tiffconf.h; do
    install -m 0444 libtiff/$i $RPM_BUILD_ROOT/usr/local/include
done

install -m 0444 libtiff/libtiff.a $RPM_BUILD_ROOT/usr/local/lib
/usr/ccs/bin/strip libtiff/libtiff.so
install -m 0555 libtiff/libtiff.so $RPM_BUILD_ROOT/usr/local/lib

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

%files devel
%defattr(-,root,other)
/usr/local/lib/*.a
/usr/local/man/man3/*
/usr/local/include/*


