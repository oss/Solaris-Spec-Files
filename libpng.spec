%define major_ver 2

Name: libpng
Version: 1.0.12
Copyright: OpenSource
Group: Development/Libraries
Summary: The PNG library
Release: 2
Source: libpng-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: zlib-devel
Conflicts: vpkg-SFWpng

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
cp scripts/makefile.solaris makefile
make LD=/usr/ccs/bin/ld

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man3
make install prefix=$RPM_BUILD_ROOT/usr/local
cp libpng.3 $RPM_BUILD_ROOT/usr/local/man/man3
cp libpngpf.3 $RPM_BUILD_ROOT/usr/local/man/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
/usr/local/include/png.h
/usr/local/include/pngconf.h
/usr/local/lib/libpng.a
/usr/local/lib/libpng.so*
/usr/local/man/man3/libpng.3
/usr/local/man/man3/libpngpf.3
