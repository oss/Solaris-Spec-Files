Summary: ISC DHCPd
Name: dhcp
Version: 3.0pl1
Release: 0ru
Group: Applications/Internet
Copyright: Unique
Source: ftp://ftp.isc.org/isc/dhcp/dhcp-latest.tar.gz
Source1: dhcp-init.d
Source2: dhcpd.conf
BuildRoot: /var/tmp/%{name}-root

%description
DHCP Server


%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  DFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include"
CC="cc" ./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/share $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/usr/sbin $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/usr/local
mv $RPM_BUILD_ROOT/sbin/* $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/etc/init.d/
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/dhcpd
chmod 755 $RPM_BUILD_ROOT/etc/init.d/dhcpd
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/local/etc/

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat<<EOF

EOF

%files
%defattr(-,root,bin)
/usr/local/share/man/man4/*
/usr/local/share/man/man3/*
/usr/local/share/man/man1m/*
/usr/local/share/man/man1/*
/usr/local/lib/*
/usr/local/include/omapip/*
/usr/local/include/isc-dhcp/*
/usr/local/include/dhcpctl.h
/usr/local/sbin/dhcpd
/usr/local/sbin/dhcrelay
/usr/local/bin/omshell
/usr/local/sbin/dhclient
/usr/local/sbin/dhclient-script
%config(noreplace)/usr/local/etc/dhcpd.conf
%config(noreplace)/etc/init.d/dhcpd
