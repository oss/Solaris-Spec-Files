Name: libpcap
Version: 0.7.1
Release: 0
Summary: Packet capture library
Source: http://www.tcpdump.org/release/libpcap-0.7.1.tar.gz
Copyright: GPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-root

%description
Packet capture library written by the Tcpdump Group.

%prep
%setup -q

%build
./configure --prefix=/usr/local
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/lib/libpcap.a
/usr/local/include/*
/usr/local/man/man3/pcap.3
