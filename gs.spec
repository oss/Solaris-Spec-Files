%define libpng_ver 1.2.1
%define jpeg_ver   6b
%define zlib_ver   1.1.4

Name: gs
Version: 6.53
Copyright: AFPL
Group: Applications/Publishing
Summary: Aladdin Ghostscript
Release: 1
Source0: ghostscript-%{version}.tar.bz2
Source1: libpng-%{libpng_ver}.tar.gz
Source2: jpegsrc.v%{jpeg_ver}.tar.gz
Source3: zlib-%{zlib_ver}.tar.gz
Source4: ghostscript-fonts-std-6.0.tar.gz
Patch: gs.patch
Requires: gs-fonts
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpng
Requires: libpng
Conflicts: vpkg-SFWgs
Provides: ghostscript

%description 
Aladdin Ghostscript lets you print or view postscript files without a
postscript printer.  You need to install gs-fonts if you want to use
Ghostscript.

%package fonts
Summary: Ghostscript fonts
Group: Applications/Publishing

%description fonts
Gs-fonts contains the fonts used by Ghostscript.  

%prep
%setup -q -n ghostscript-%{version}
%setup -q -D -T -a 1 -n ghostscript-%{version}
%setup -q -D -T -a 2 -n ghostscript-%{version}
%setup -q -D -T -a 3 -n ghostscript-%{version}
%setup -q -D -T -a 4 -n ghostscript-%{version}

# The patch configures the makefile properly.
#%patch -p1

cp src/unix-gcc.mak makefile

%build
ln -s jpeg-%{jpeg_ver} jpeg
ln -s zlib-%{zlib_ver} zlib
ln -s libpng-%{libpng_ver} libpng
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
tar cf - fonts | (cd $RPM_BUILD_ROOT/usr/local/share/ghostscript && tar xf -)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/*
/usr/local/share/ghostscript/%{version}
/usr/local/bin/*
/usr/local/man/man1/*

%files fonts
%defattr(-,root,root)
/usr/local/share/ghostscript/fonts/*
