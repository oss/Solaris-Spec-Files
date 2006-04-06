Summary: pkg-config
Name: pkgconfig
Version: 0.20
Release: 1
Source: pkg-config-%{version}.tar.gz
Copyright: GPL
Group: Libraries
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
pkgconfig

%prep
%setup -q -n pkg-config-%{version}

%build
#CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc" 
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

./configure --prefix=/usr/local --disable-nls --disable-rebuilds

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/pkg-config
/usr/local/man/man1/pkg-config.1
/usr/local/share/aclocal/pkg.m4

%changelog
* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.6.2-2
- Updated to version 0.20
