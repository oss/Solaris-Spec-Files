Name: bind
Version: 8.2.3
Copyright: BSD
Group: Applications/Internet
Summary: Berkeley name server
Release: 2
Source0: bind-src-8.2.3.tar.gz
Source1: bind-doc-8.2.3.tar.gz
Source2: bind-ru.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: bind-dnstools

%description
Bind is the Internet Software Consortium's domain name server.

%package dnstools
Summary: Bind dnstools
Group: Applications/Internet

%description dnstools
The bind-dnstools are addr, dig, dnsquery, host, nslookup, and nsupdate.

%package doc
Summary: Bind documentation
Group: Documentation

%description doc
Bind-doc is the documentation for ISC bind.

%prep
%setup -q -T -c -n bind
%setup -q -D -T -a 0 -n bind
%setup -q -D -T -a 1 -n bind
%setup -q -D -T -a 2 -n bind

%build
cd src
make

%install
cd src
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/arpa
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/isc
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/sys
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
make install DESTDIR=$RPM_BUILD_ROOT
cd ../ru-bind
tar cf - etc var | (cd $RPM_BUILD_ROOT && tar xvf -)

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
RPM installed these files on your system:

/etc/init.d/named.rpm
/etc/rc2.d/S72bind.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm

You should take the rpm extension off and customize them.  You also
should add directories /var/named/primary and /var/named/rutgers.
EOF

%files
%defattr(-,bin,bin)
%doc src/LICENSE src/LICENSE_RSA
/usr/local/sbin/named
/usr/local/sbin/named-xfer
/usr/local/sbin/ndc
/usr/local/sbin/irpd
/usr/local/sbin/dnskeygen
/usr/local/sbin/named-bootconf
/usr/local/bind
/etc/init.d/named.rpm
/etc/rc2.d/S72bind.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm

%files dnstools
%defattr(-,bin,bin)
/usr/local/bin/addr
/usr/local/bin/nslookup
/usr/local/bin/dig
/usr/local/bin/dnsquery
/usr/local/bin/host
/usr/local/bin/nsupdate
/usr/local/bin/mkservdb
/usr/local/lib/nslookup.help

%files doc
%defattr(-,bin,bin)
%doc doc
