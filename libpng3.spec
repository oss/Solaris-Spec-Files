Name: libpng3
Version: 1.2.1
Copyright: OpenSource
Group: Development/Libraries
Summary: The PNG library
Release: 0
Source: libpng-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
%ifnos solaris2.9
BuildRequires: zlib-devel
%endif
#Conflicts: vpkg-SFWpng

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
make LD=/usr/ccs/bin/ld

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man3
make install prefix=$RPM_BUILD_ROOT/usr/local
cp libpng.3 $RPM_BUILD_ROOT/usr/local/man/man3
cp libpngpf.3 $RPM_BUILD_ROOT/usr/local/man/man3

%post
ln -s /usr/local/lib/libpng.so.3 /usr/local/lib/libpng.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE
/usr/local/lib/libpng.so.*

%files devel
%defattr(-,root,root)
/usr/local/man/man3/libpng.3
/usr/local/man/man3/libpngpf.3
/usr/local/include/png.h
/usr/local/include/pngconf.h
/usr/local/lib/libpng.a
