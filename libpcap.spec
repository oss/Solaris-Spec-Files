Name:		libpcap
Version:	1.0.0
Release:        1
License:	GPL
Group:		System Environment/Libraries
Source:		http://www.tcpdump.org/release/libpcap-%{version}.tar.gz
Patch0:		libpcap-1.0.0-solaris_configure.patch
Patch1:		libpcap-1.0.0-solaris_shared.patch
URL:		http://www.tcpdump.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	autoconf automake

Summary:	Packet Capture library

%description
libpcap is a system-independent interface for user-level packet 
capture. libpcap provides a portable framework for low-level network 
monitoring. Applications include network statistics collection, 
security monitoring, network debugging, etc.

%package devel 
Group:		Applications/Libraries
Requires:	libpcap = %{version}-%{release}
Summary:        Headers and documentation for development with libpcap

%description devel
This package contains the header files and documentation for the
development of applications that use libpcap.

%package static
Group:          Applications/Libraries
Summary:        libpcap static library

%description static
This package contains the libpcap static library.

%prep
%setup -q

%patch0 -p0
%patch1 -p0

autoreconf

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=%{_prefix} --mandir=%{_mandir}

gmake -j3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}

gmake install DESTDIR=%{buildroot}
gmake install-shared DESTDIR=%{buildroot}

cd %{buildroot}%{_libdir}
ln -s libpcap.so.1.0.0 libpcap.so.1
ln -s libpcap.so.1 libpcap.so

/usr/local/bin/unhardlinkify.py %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc CHANGES CREDITS LICENSE README
%{_libdir}/libpcap.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libpcap.so
%{_bindir}/pcap-config
%{_mandir}/man*/*

%files static
%defattr(-, root, root)
%{_libdir}/libpcap.a

%changelog
* Wed May 20 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.0.0-1
- Updated to version 1.0.0
- Build shared library, move static library to own package
- Several minor changes to spec file
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.9.8-1
- Bump to 0.9.8
* Tue Dec 19 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.5-1
- Updated to 0.9.5, modernized spec file
