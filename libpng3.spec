Name: libpng3
Version: 1.2.1
Copyright: OpenSource
Group: Development/Libraries
Summary: The PNG library
Release: 6
Source: libpng-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
%ifnos solaris2.9
BuildRequires: zlib-devel
%endif
#Conflicts: vpkg-SFWpng
Provides: libpng 
Requires: zlib
BuildRequires: zlib-devel
%ifarch sparc64
Requires: zlib-sparc64
Provides: libpng3-sparc64
BuildRequires: gcc3
%endif
Obsoletes: libpng = 1.2.1

%description
PNG (Portable Network Graphics) is a lossless graphics format.  Unlike
GIF, it has alpha channels, gamma correction, 2-dimensional interlacing,
and up to 48-bit truecolor.  It also compresses 5-25% better than GIF.
The only features GIF has that PNG lacks are animations and Unisys
lawyers.  Install this library if you are writing software that needs
to manipulate PNG images or if you want to use software that uses libpng.

%package devel
Summary: %{name} include files, etc.
Requires: %{name}
Group: Development
%description devel
%{name} include files, etc.

%prep
%setup -q -n libpng-%{version}

%build
cp scripts/makefile.solaris makefile
%ifarch sparc64
LD_LIBRARY_PATH="/usr/local/lib/sparcv9"
LD_RUN_PATH="/usr/local/lib/sparcv9"
export LD_LIBRARY_PATH LD_RUN_PATH
make LD=/usr/ccs/bin/ld CC="/usr/local/gcc3/bin/gcc"
mkdir sparcv9
mv libpng.so* libpng.a sparcv9/
make clean
%endif
make LD=/usr/ccs/bin/ld

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man3
make install prefix=$RPM_BUILD_ROOT/usr/local
cp libpng.3 $RPM_BUILD_ROOT/usr/local/man/man3
cp libpngpf.3 $RPM_BUILD_ROOT/usr/local/man/man3
%ifarch sparc64
mkdir $RPM_BUILD_ROOT/usr/local/lib/sparcv9
cp sparcv9/libpng* $RPM_BUILD_ROOT/usr/local/lib/sparcv9/
%endif


%post
rm -f /usr/local/lib/libpng.so
ln -s /usr/local/lib/libpng.so.3 /usr/local/lib/libpng.so
%ifarch sparc64
rm /usr/local/lib/sparcv9/libpng.so
ln -s /usr/local/lib/sparcv9/libpng.so.3 /usr/local/lib/sparcv9/libpng.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
/usr/local/lib/libpng.so.*
%ifarch sparc64
/usr/local/lib/sparcv9/libpng.so.*
%endif

%files devel
%defattr(-,root,root)
/usr/local/man/man3/libpng.3
/usr/local/man/man3/libpngpf.3
/usr/local/include/png.h
/usr/local/include/pngconf.h
/usr/local/lib/libpng.a
%ifarch sparc64
/usr/local/lib/sparcv9/libpng.a
%endif
