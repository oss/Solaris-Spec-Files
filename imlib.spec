Name: imlib
Version: 1.9.10
Release: 3
Copyright: LGPL
Group: X11/Libraries
Requires: libpng
Requires: zlib
Requires: libjpeg
Requires: libpng
Requires: libungif-devel
Requires: tiff
Requires: gtk+ >= 1.1
Summary: Image loading and rendering library for X11R6
Source: imlib-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: ImageMagick
BuildRequires: zlib-devel
BuildRequires: libpng
BuildRequires: libjpeg
BuildRequires: libungif-devel
BuildRequires: tiff
BuildRequires: ImageMagick

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

%package cfgeditor
Summary: Imlib configuration editor
Group: X11/Libraries
Requires: imlib = %{PACKAGE_VERSION}

%description cfgeditor
The imlib_config program allows you to control the way imlib uses
color and handles gamma correction/etc.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include" \
   LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
   LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
   ./configure --prefix=/usr/local --enable-shared --enable-static \
   --sysconfdir=/etc --enable-shm
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
mkdir -p $RPM_BUILD_ROOT/etc
make install prefix=$RPM_BUILD_ROOT/usr/local sysconfdir=$RPM_BUILD_ROOT/etc
cd $RPM_BUILD_ROOT
for i in etc/* ; do
    mv $i $i.rpm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You have to move /etc/imrc.rpm and  /etc/im-palette*.  

Imlib was built with shared-memory support.  You will probably have to
increase the amount of shared memory that Solaris allocates; try
adding the line

set shmsys:shminfo_shmseg=32

to /etc/system (and rebooting).

Alternately, disable shared memory usage with imlib_config.
EOF

%files cfgeditor
%defattr(-,bin,bin)
/usr/local/bin/imlib_config

%files devel
%defattr(-,bin,bin)
%doc doc/*.gif doc/*.html
/usr/local/bin/imlib-config
/usr/local/lib/*a
/usr/local/include/*
/usr/local/share/aclocal/*

%files
%defattr(-,bin,bin)
/usr/local/lib/lib*.so*
/usr/local/lib/pkgconfig/*
/etc/*.rpm
