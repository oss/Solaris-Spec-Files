Summary: pilot-link
Name: pilot-link
Version: 0.11.7
Release: 1
Copyright: GPL
Group: System Environment/Libraries
Source: %{name}-%{version}.tar.gz
URL: http://pilot-link.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Robert Renaud <rrenaud@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: readline
BuildRequires: readline

%description
Software to interface with palm pilots.

%prep
%setup -q

%build

LIBS="-lsocket -lnsl" LDFLAGS="-L/usr/local/lib -R/usr/local/lib /usr/local/lib/libstdc++.so.2.10.0" CC="gcc" ./configure --prefix=/usr/local
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/lib/*
/usr/local/include/*
/usr/local/man/man1/*
/usr/local/man/man7/*
/usr/local/share/pilot-link/*




