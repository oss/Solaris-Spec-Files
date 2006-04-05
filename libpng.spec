%define major_ver 12

Name: libpng
Version: 1.2.8
Release: 1
Copyright: OpenSource
Group: Development/Libraries
Summary: The PNG library
Source: libpng-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
PNG (Portable Network Graphics) is a lossless graphics format.  Unlike
GIF, it has alpha channels, gamma correction, 2-dimensional interlacing,
and up to 48-bit truecolor.  It also compresses 5-25% better than GIF.
The only features GIF has that PNG lacks are animations and Unisys
lawyers.  Install this library if you are writing software that needs
to manipulate PNG images or if you want to use software that uses libpng.


%prep
%setup -q

%build
# We don't have a configure script, only precanned makefiles
#cp scripts/makefile.so9 makefile

# They have an error in their makefile, we need to correct that
sed 's/^CFLAGS=-I$(ZLIBINC) -O3/CFLAGS=-I$(ZLIBINC) -xO3/' \
  scripts/makefile.so9 > makefile

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man3
gmake install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
/usr/local/bin/*
/usr/local/include/libpng%{major_ver}/*.h
/usr/local/lib/*.a
/usr/local/lib/*.so.*
/usr/local/lib/pkgconfig/*.pc
/usr/local/man/man3/*
/usr/local/man/man5/*
