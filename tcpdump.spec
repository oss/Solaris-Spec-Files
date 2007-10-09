Name: tcpdump
Version: 3.9.8
Release: 1
Summary: Packet capture library
Source: http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Copyright: BSD
Group: Networking
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpcap

%description
Program to sniff your network by The Tcpdump Group.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

# SMB still has buggy issues as of 3.9.8

./configure \
	--prefix=/usr/local \
	--disable-smb

gmake -j3

%install
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/sbin/tcpdump
/usr/local/share/man/man1/tcpdump.1

%changelog
* Tue Oct 09 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.9.8
- Bump to 3.9.8
