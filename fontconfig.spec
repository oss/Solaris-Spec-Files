Summary: fontconfig
Name: fontconfig
Version: 2.3.95
Release: 3
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local \
            --disable-nls \
	    --enable-expat \
            --with-add-fonts=/usr/openwin/lib/X11/fonts \
            --disable-docs

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

%files devel
%defattr(-,root,other)
/usr/local/include/fontconfig/fcfreetype.h
/usr/local/include/fontconfig/fcprivate.h
/usr/local/include/fontconfig/fontconfig.h
/usr/local/lib/pkgconfig/fontconfig.pc
/usr/local/lib/libfontconfig.a

