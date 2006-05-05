Summary:	a simplified, portable interface to several low-level networking routines
Name:		libdnet
Version:	1.11
Release:        1
Copyright:	GPL
Group:		System/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Provides:	libdnet.1

%description
libdnet provides a simplified, portable interface to several low-level 
networking routines, including

    * network address manipulation
    * kernel arp(4) cache and route(4) table lookup and manipulation
    * network firewalling (IP filter, ipfw, ipchains, pf, PktFilter, ...)
    * network interface lookup and manipulation
    * IP tunnelling (BSD/Linux tun, Universal TUN/TAP device)
    * raw IP packet and Ethernet frame transmission 

Supported languages:

    * C, C++
    * Python
    * Perl, Ruby (see below) 

Supported platforms:

    * BSD (OpenBSD, FreeBSD, NetBSD, BSD/OS)
    * Linux (Redhat, Debian, Slackware, etc.)
    * MacOS X
    * Windows (NT/2000/XP)
    * Solaris
    * IRIX
    * HP-UX
    * Tru64 

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use {%name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/local/lib/libdnet.a
rm $RPM_BUILD_ROOT/usr/local/lib/libdnet.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/sbin/*
/usr/local/lib/*
/usr/local/man/man3/*
/usr/local/man/man8/*

%files devel
%defattr(-,root,root)
/usr/local/include/*

%changelog
* Fri Apr 07 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.11-1
- Initial Rutgers release
