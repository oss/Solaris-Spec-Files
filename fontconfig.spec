Summary: fontconfig
Name: fontconfig
Version: 2.2.0
Release: 4
Copyright: GPL
Group: Applications/Editors
Source: http://www.fontconfig.org/release/fontconfig-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: freetype2 >= 2.1.4-1 
BuildRequires: freetype2-devel >= 2.1.4-1 

%description
fontconfig

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development
%description devel
%{name} include files, etc.

%package doc
Summary: %{name} extra documentation
Requires: %{name}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q

%build
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
LDFLAGS="-R/usr/local/lib -L/usr/local/lib"
PATH="/usr/local/bin:$PATH"
CPPFLAGS="-I/usr/local/include"
CFLAGS="-O3"
export LD_LIBRARY_PATH PATH CPPFLAGS LDFLAGS CFLAGS
CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds --disable-xkb --with-confdir=/usr/local/etc/fonts --with-default-fonts=/usr/local/share/fonts --with-add-fonts=/usr/openwin/lib/X11/fonts --disable-docs --enable-fast-install
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/share/fonts
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/bin/* \
    $RPM_BUILD_ROOT/usr/local/lib/libfontconfig.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/fc-cache
/usr/local/bin/fc-list
/usr/local/etc/fonts/fonts.conf
/usr/local/etc/fonts/fonts.dtd
/usr/local/lib/libfontconfig.so*
/usr/local/man/man5/*
/usr/local/share/fonts

%files devel
%defattr(-,root,other)
/usr/local/include/fontconfig/fcfreetype.h
/usr/local/include/fontconfig/fcprivate.h
/usr/local/include/fontconfig/fontconfig.h
/usr/local/lib/pkgconfig/fontconfig.pc
/usr/local/lib/libfontconfig.a
/usr/local/man/man3/*


%files doc
%defattr(-,root,other)
/usr/local/share/doc/fontconfig