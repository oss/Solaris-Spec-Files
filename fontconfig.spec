Summary: fontconfig
Name: fontconfig
Version: 2.3.2
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: http://www.fontconfig.org/release/fontconfig-%{version}.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
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

%prep
%setup -q

%build
LDFLAGS="-R/usr/local/lib -L/usr/local/lib"
PATH="/opt/SUNWspro/bin:/usr/local/bin:/usr/local/gnu/bin:$PATH"
CPPFLAGS="-I/usr/local/include"
CC="cc" CXX="CC"
export PATH CPPFLAGS LDFLAGS CC CXX
./configure --prefix=/usr/local \
            --disable-nls \
            --with-confdir=/usr/local/etc/fonts \
            --with-default-fonts=/usr/local/share/fonts \
            --with-add-fonts=/usr/openwin/lib/X11/fonts \
            --disable-docs \
            --with-expat

gmake


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/usr/local/share/fonts

gmake install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/*
/usr/local/etc/fonts/*
/usr/local/lib/libfontconfig.so*
/usr/local/share/fonts
/usr/local/man/man1/fc-match.1

%files devel
%defattr(-,root,other)
/usr/local/include/fontconfig/fcfreetype.h
/usr/local/include/fontconfig/fcprivate.h
/usr/local/include/fontconfig/fontconfig.h
/usr/local/lib/pkgconfig/fontconfig.pc
/usr/local/lib/libfontconfig.a

