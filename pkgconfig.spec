Summary: pkg-config
Name: pkgconfig
Version: 0.15.0
Release: 3
Copyright: GPL
Group: Libraries
Source: http://www.freedesktop.org/software/pkgconfig/releases/pkgconfig-0.15.0.tar.gz
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
glib

%prep
%setup -q -n pkgconfig-%{version}

%build
CC="gcc" ./configure --prefix=/usr/local --disable-nls --disable-rebuilds


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



