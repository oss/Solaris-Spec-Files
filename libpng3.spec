Name: libpng3
Version: 1.2.6
License: OpenSource
Group: Development/Libraries
Summary: The PNG library
Release: 1
Source: libpng-%{version}.tar.gz
Patch: libpng-%{version}-patch-pngwutil.diff
Patch1: %{name}-%{version}.diff
BuildRoot: /var/tmp/%{name}-root
Provides: libpng libpng3

#So, since this probably won't be the clearest thing to someone looking over it this is what is says. IF you are not on solaris 9 THEN buildrequire zlib-devel, and IF you are a 64bit machine additionally require zlib-sparc64 and provide libpng3-sparc64 ELSE (you are on solaris 9) require SUNWzlib and buildrequire SUNWzlib.

%ifnos solaris2.9
BuildRequires: zlib-devel

%ifarch sparc64
Requires: zlib-sparc64
Provides: libpng3-sparc64
%else
Requires: zlib
%endif

%else

%ifarch sparc64
Requires: vpkg-SUNWzlibx
BuildRequires: vpkg-SUNWzlibx
%else
Requires: vpkg-SUNWzlib
BuildRequires: vpkg-SUNWzlib
%endif

%endif

#Conflicts: vpkg-SFWpng

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
%patch -p1
%patch1 -p1

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH"
export PATH

#cp scripts/makefile.solaris makefile
cp scripts/makefile.so9 makefile

%ifarch sparc64
EXTRA_CFLAGS=-xarch=v9
EXTRA_LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export EXTRA_CFLAGS EXTRA_LDFLAGS

gmake
mkdir sparcv9
mv libpng*.so* libpng.a sparcv9/
gmake clean
%endif
EXTRA_CFLAGS=
EXTRA_LDFLAGS=
export EXTRA_CFLAGS EXTRA_LDFLAGS

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
gmake install DESTDIR=%{buildroot}
%ifarch sparc64
mkdir %{buildroot}/usr/local/lib/sparcv9
cp sparcv9/libpng* %{buildroot}/usr/local/lib/sparcv9/
%endif

%post
rm -f /usr/local/lib/libpng.so
ln -s /usr/local/lib/libpng.so.3 /usr/local/lib/libpng.so
%ifarch sparc64
rm -f /usr/local/lib/sparcv9/libpng.so
ln -s /usr/local/lib/sparcv9/libpng.so.3 /usr/local/lib/sparcv9/libpng.so
%endif

#%clean
#rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
/usr/local/lib/libpng*.so*
%ifarch sparc64
/usr/local/lib/sparcv9/libpng*.so*
%endif

%files devel
%defattr(-,root,root)
/usr/local/bin/libpng12-config
/usr/local/man/man3/*
/usr/local/man/man5/*
/usr/local/include/*.h
/usr/local/include/libpng12/*.h
/usr/local/lib/*.a
/usr/local/lib/pkgconfig/libpng12.pc
%ifarch sparc64
/usr/local/lib/sparcv9/*.a
%endif
