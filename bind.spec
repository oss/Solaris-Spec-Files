Name: bind
Version: 9.3.2
Copyright: BSD
Group: Applications/Internet
Summary: Berkeley name server
Release: 1
Source0: bind-%{version}.tar.gz
Source1: bind-ru.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: openssl
Requires: openssl

%description
BIND is the Internet Software Consortium's domain name server.

%prep
%setup -q  
%setup -q -D -a 1

%build
CC=cc PATH="/opt/SUNWspro/bin:${PATH}" \
./configure --prefix=/usr/local --with-openssl --enable-threads \
--enable-shared --enable-static --enable-largefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/lib
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/arpa
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/isc
mkdir -p $RPM_BUILD_ROOT/usr/local/bind/include/sys
mkdir -p $RPM_BUILD_ROOT/usr/local/lib
make install DESTDIR=$RPM_BUILD_ROOT
cd ru-bind
tar cf - etc var | (cd $RPM_BUILD_ROOT && tar xvf -)

# We need to remove hard links
cd $RPM_BUILD_ROOT
/usr/local/bin/unhardlinkify.py ./

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

You may also need to disable BIND that comes with Solaris.
EOF

%files
%defattr(-,bin,bin)
%dir /usr/local/include/bind9/
%dir /usr/local/include/isc/
%dir /usr/local/include/isccc/
%dir /usr/local/include/dns/
%dir /usr/local/include/dst/
%dir /usr/local/include/lwres/
%dir /usr/local/include/isccfg/
/usr/local/bind/*
/usr/local/sbin/*
/usr/local/bin/*
/usr/local/include/bind9/*
/usr/local/include/isc/*
/usr/local/include/isccc/*
/usr/local/include/dns/*
/usr/local/include/dst/*
/usr/local/include/lwres/*
/usr/local/include/isccfg/*
/usr/local/lib/*
/usr/local/man/*
/etc/init.d/named.rpm
/etc/rc2.d/S72bind.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm
