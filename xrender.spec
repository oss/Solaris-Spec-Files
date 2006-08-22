Summary: xrender
Name: xrender
Version: 0.8.3
Release: 7
Copyright: GPL
Group: X11/Libraries
Source: http://fontconfig.org/release/xrender-0.8.3.tar.bz2
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: render

%description
xrender for Xft2 

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

./configure --prefix=/usr/local

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other) 
/usr/local/lib/libXrender.so*

%files devel
%defattr(-,root,other) 
/usr/local/include/X11/extensions/*
/usr/local/lib/libXrender.a
/usr/local/lib/pkgconfig/xrender.pc
