Summary: Provides booting services for network bootable devices using DHCP
Name: bootpd-dhcp
Version: 2.4
Release: 2
Copyright: CMU version freely distributable; has Rutgers modifications
Group: Applications/Internet
Source: bootpd_DHCP.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
BOOTPD is a useful adjunct to the nfs diskless boot EPROM code.

The alternatives for initiating a boot of a kernel across a network
are to use RARP protocol, or BOOTP protocol. BOOTP is more flexible;
it allows additional items of information to be returned to the
booting client; it also supports booting across gateways.

%prep
%setup -q -n bootpd_DHCP

%build
make clean
make

%install
rm -rf $RPM_BUILD_ROOT
for i in etc/init.d usr/local/sbin usr/local/man/man5 usr/local/man/man8 ; do
    mkdir -p $RPM_BUILD_ROOT/$i
done

for i in bootpd bootpef bootpgw bootptest ; do
    install -m 0755 $i $RPM_BUILD_ROOT/usr/local/sbin/$i
    if [ -f $i.5 ] ; then
	install -m 0644 $i.5 $RPM_BUILD_ROOT/usr/local/man/man5/$i.5
    elif [ -f $i.8 ] ; then
        install -m 0644 $i.8 $RPM_BUILD_ROOT/usr/local/man/man8/$i.8
    fi
done

install -m 0744 bootpd.rpm $RPM_BUILD_ROOT/etc/init.d/bootpd.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You need to edit and move /etc/init.d/bootpd.rpm .
EOF

%files
%defattr(-,root,other)
%doc Announce Changes Changes.Dynamic README README.Dynamic Problems ToDo
%doc ToDo.Dynamic Installation bootptab.Dynamic bootptab.cmu bootptab.mcs
/usr/local/sbin/*
/usr/local/man*/*
/etc/init.d/bootpd.rpm
