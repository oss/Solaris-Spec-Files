Name: bind
Version: 9.2.1
Copyright: BSD
Group: Applications/Internet
Summary: Berkeley name server
Release: 1
Source0: bind-9.2.1.tar.gz
Source1: bind-ru.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Bind is the Internet Software Consortium's domain name server.

%prep
%setup -q  
%setup -q -D -a 1

%build
./configure
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
/usr/local/bind/*
/usr/local/sbin/*
/usr/local/bin/*
/usr/local/include/isc/*
/usr/local/include/isccc/*
/usr/local/include/dns/*
/usr/local/include/dst/*
/usr/local/include/lwres/*
/usr/local/include/isccfg/cfg.h
/usr/local/include/isccfg/check.h
/usr/local/include/isccfg/log.h
/usr/local/lib/*
/usr/local/man/*
/etc/init.d/named.rpm
/etc/rc2.d/S72bind.rpm
/etc/named.conf.sample.rpm
/var/named/root.hints.get.rpm
