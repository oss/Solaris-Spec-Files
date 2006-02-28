Summary: xft2
Name: xft2
Version: 2.1.7
Release: 1
Copyright: GPL
Group: X11/Libraries
Source0: http://xlibs.freedesktop.org/release/libXft-2.1.7.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: xrender
BuildRequires: xrender-devel

%description
xft2 

%package devel
Summary: %{name} include files, etc.
Requires: %{name} %{buildrequires}
Group: Development
%description devel 
%{name} include files, etc.

%prep
%setup -q -n libXft-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/libXft.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/libXft.so
/usr/local/lib/libXft.so.2
/usr/local/lib/libXft.so.2.1.2

%files devel
%defattr(-,root,other)
/usr/local/bin/xft-config
/usr/local/include/X11/Xft
/usr/local/lib/libXft.a
/usr/local/lib/pkgconfig/xft.pc
/usr/local/man/man3/Xft.3

%changelog
* Tue Feb 21 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.7-1
- Updated to 2.1.7
