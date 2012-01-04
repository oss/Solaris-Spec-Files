Name:		tcpdump
Version:	4.2.1
Release:	1
Source: 	http://www.tcpdump.org/release/tcpdump-%{version}.tar.gz
Patch:		noINET6.patch
URL:		http://www.tcpdump.org
License: 	BSD
Group:		Applications/Networking
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libpcap-devel

Summary:	Dumps network packet information

%description
Tcpdump is a program to capture packets from a network and dump their headers.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}:/usr/ccs/bin"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--disable-smb       \
	--disable-ipv6
	

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc CHANGES CREDITS LICENSE README
%{_sbindir}/*
%{_mandir}/man1/*

%changelog
* Wed Jan 04 2012 Kaitlin Poskaitis <kap263@nbcs.rutgers.edu> - 4.2.1
- Updated to version 4.2.1
* Wed May 20 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.0.0-1
- Updated to version 4.0.0
- Several spec file changes

* Tue Oct 09 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.9.8
- Bump to 3.9.8
