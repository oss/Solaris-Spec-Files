Summary: xft2
Name: xft2
Version: 2.1.2
Release: 9
Copyright: GPL
Group: X11/Libraries
Source0: http://fontconfig.org/release/xft-2.1.2.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
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
%setup -q -n xft-%{version}

%build
PATH="/usr/local/bin:/usr/bin:/bin" \
LD_LIBRARY_PATH="/usr/local/lib" \
LD_RUN_PATH="/usr/local/lib" \
CFLAGS="-O3" \
./configure --prefix=/usr/local

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make
make install DESTDIR=$RPM_BUILD_ROOT
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/lib/libXft.so*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/libXft.so
/usr/local/lib/libXft.so.2
/usr/local/lib/libXft.so.2.1.1

%files devel
%defattr(-,root,other)
/usr/local/bin/xft-config
/usr/local/include/X11/Xft
/usr/local/lib/libXft.a
/usr/local/lib/pkgconfig/xft.pc
/usr/local/man/man3/Xft.3


