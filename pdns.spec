%define mysql_version 3.23.55

Summary: PowerDNS
Name: pdns
Version: 2.9.7
Release: 2ru
Copyright: GPL
Group: Internet/DNS
Source: http://downloads.powerdns.com/releases/pdns-2.9.7.tar.gz
URL: http://www.powerdns.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Provides: PowerDNS
Requires: mysql = %{mysql_version} bash
BuildRequires: mysql = %{mysql_version} mysql-devel = %{mysql_version}
%description
The PowerDNS Nameserver is a modern, advanced and high performance authoritative-only nameserver. It is written from scratch and conforms to all relevant DNS standards documents. Furthermore, PowerDNS interfaces with almost any database.

%prep
%setup -q

%build
LDFLAGS="/usr/local/lib/libstdc++.so.2.10.0"
export LDFLAGS
CC="gcc" ./configure --prefix=/usr/local --with-modules="gmysql" --with-mysql=/usr/local/mysql-%{mysql_version}/

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local $RPM_BUILD_ROOT/etc/init.d
make install DESTDIR=$RPM_BUILD_ROOT
sed "s/\/bin\/sh/\/bin\/bash/" pdns/pdns > $RPM_BUILD_ROOT/etc/init.d/pdns
chmod 755 $RPM_BUILD_ROOT/etc/init.d/pdns
mv $RPM_BUILD_ROOT/usr/local/etc/pdns.conf-dist $RPM_BUILD_ROOT/usr/local/etc/pdns.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
/etc/init.d/pdns
/usr/local/lib/*
/usr/local/bin/*
/usr/local/sbin/pdns_server
%config(noreplace)/usr/local/etc/pdns.conf
/usr/local/man/man8/*



