Name: imlib
Version: 1.9.15
Release: 1
Copyright: LGPL
Group: X11/Libraries
Requires: libpng3
Requires: zlib
Requires: libjpeg
Requires: libungif-devel
Requires: tiff
Requires: gtk+ >= 1.1
Summary: Image loading and rendering library for X11R6
Source: imlib-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: ImageMagick
#BuildRequires: zlib-devel
BuildRequires: libpng3-devel
#BuildRequires: libjpeg-devel
BuildRequires: libungif-devel
BuildRequires: tiff
BuildRequires: ImageMagick >= 5.5.3 ImageMagick-devel >= 5.5.3
Provides: imlib-cfgeditor

%description
Imlib is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexability and
speed.

%package devel
Summary: Imlib headers, static libraries and documentation
Group: X11/Libraries
Requires: imlib = %{PACKAGE_VERSION}

%description devel
Headers, static libraries and documentation for Imlib.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
   ./configure --prefix=/usr/local --enable-shared --enable-static \
   --sysconfdir=/etc --enable-shm
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/etc
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
cd $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
Imlib was built with shared-memory support.  You will probably have to
increase the amount of shared memory that Solaris allocates; try
adding the line

set shmsys:shminfo_shmseg=32

to /etc/system (and rebooting).
EOF

%files devel
%defattr(-,bin,bin)
%doc doc/*.gif doc/*.html
/usr/local/bin/imlib-config
/usr/local/lib/*a
/usr/local/include/*
/usr/local/share/aclocal/*
/usr/local/man/man1/imlib-config.1

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/lib/pkgconfig/*
%config(noreplace) /etc/*
