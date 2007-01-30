Summary: 	pilot-link
Name: 		pilot-link
Version: 	0.11.8
Release: 	1
Copyright: 	GPL
Group: 		System Environment/Libraries
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://pilot-link.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	readline5
BuildRequires: 	readline5-devel

%description
Software to interface with palm pilots.

%prep
%setup -q

%build
#LIBS="-lsocket -lnsl" LDFLAGS="-L/usr/local/lib -R/usr/local/lib /usr/local/lib/libstdc++.so.2.10.0" CC="gcc" ./configure --prefix=/usr/local
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include -I/usr/j2se/include/solaris"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc" CXX="g++"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CXX

./configure --prefix=/usr/local --without-perl --with-libpng=/usr/local
gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT

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
/usr/local/share/aclocal/pilot-link.m4
