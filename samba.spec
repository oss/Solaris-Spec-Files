Summary: SMB server for UNIX systems
Name: samba
Version: 3.0.4
Release: 0
Group: Applications/Internet
License: GPL
Source0: samba-%{version}.tar.bz2
Source1: samba.initd
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openldap-devel rpm-devel
BuildConflicts: heimdal-devel
Requires: samba-common
Patch0: samba-3.0.2a-picsuffix.patch

%description
Samba provides an SMB server which can be used to provide
network services to SMB (sometimes called "Lan Manager")
clients, including various versions of MS Windows, OS/2,
and other Linux machines. Samba also provides some SMB
clients, which complement the built-in SMB filesystem
in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame)
protocol.

%package common
Group: Applications/Internet
Summary: Core and Configuration for Samba
%description common
Core and Configuration for Samba

%package server
Group: Applications/Internet
Summary: Samba server and associated man pages
Requires: samba samba-client
%description server
Samba server and associated man pages

%package client
Group: Applications/Internet
Summary: Samba client
Requires: samba
%description client
Samba client

%package doc
Group: Applications/Internet
Summary: Samba docs
Requires: samba
%description doc
Samba docs

%package swat
Group: Applications/Internet
Summary: Samba swat
Requires: samba
%description swat
Samba swat

%prep
%setup -q

%patch0 

%build
cd source
# POBAD_CC is a hack for some sparcv9 libtool badness. we compile 32bit...
CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/cc' CPPFLAGS='-I/usr/local/include -I/usr/sfw/include' LDFLAGS='-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib' ./configure --with-ldap --with-piddir=/var/run --localstatedir=/var/local/samba
gmake

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/samba

mkdir -p $RPM_BUILD_ROOT/usr/local/share/samba
cp -r examples $RPM_BUILD_ROOT/usr/local/share/samba
cp -r docs $RPM_BUILD_ROOT/usr/local/share/samba

mkdir -p $RPM_BUILD_ROOT/var/local/samba
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/samba

rm -rf var

cd source
make install DESTDIR=$RPM_BUILD_ROOT

%post
cat <<EOF
smb.conf goes in /usr/local/samba/lib.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
#empty

%files common
%defattr(-,root,root)
/usr/local/samba/lib/*
/usr/local/samba/include/*
/var/local/samba
/usr/local/samba/man/man5/smb.conf.5
/usr/local/samba/man/man5/lmhosts.5
/usr/local/samba/man/man7/samba.7

%files server
%defattr(-,root,root)
%attr(700,root,root)/usr/local/samba/private
%attr(755,root,root)/etc/init.d/samba
/usr/local/samba/bin/smbcontrol
/usr/local/samba/sbin/smbd
/usr/local/samba/sbin/nmbd
/usr/local/samba/sbin/winbindd
/usr/local/samba/man/man8/nmbd.8
/usr/local/samba/man/man8/smbd.8
/usr/local/samba/man/man8/winbindd.8



%files client
%defattr(-,root,root)
/usr/local/samba/bin/findsmb
/usr/local/samba/bin/net
/usr/local/samba/bin/nmblookup
/usr/local/samba/bin/ntlm_auth
/usr/local/samba/bin/pdbedit
/usr/local/samba/bin/profiles
/usr/local/samba/bin/rpcclient
/usr/local/samba/bin/smbcacls
/usr/local/samba/bin/smbclient
/usr/local/samba/bin/smbcquotas
/usr/local/samba/bin/smbpasswd
/usr/local/samba/bin/smbspool
/usr/local/samba/bin/smbstatus
/usr/local/samba/bin/smbtar
/usr/local/samba/bin/smbtree
/usr/local/samba/bin/tdbbackup
/usr/local/samba/bin/tdbdump
/usr/local/samba/bin/testparm
/usr/local/samba/bin/testprns
/usr/local/samba/bin/wbinfo
/usr/local/samba/man/man1/editreg.1
/usr/local/samba/man/man1/findsmb.1
/usr/local/samba/man/man1/log2pcap.1
/usr/local/samba/man/man1/nmblookup.1
/usr/local/samba/man/man1/ntlm_auth.1
/usr/local/samba/man/man1/profiles.1
/usr/local/samba/man/man1/rpcclient.1
/usr/local/samba/man/man1/smbcacls.1
/usr/local/samba/man/man1/smbclient.1
/usr/local/samba/man/man1/smbcontrol.1
/usr/local/samba/man/man1/smbcquotas.1
/usr/local/samba/man/man1/smbsh.1
/usr/local/samba/man/man1/smbstatus.1
/usr/local/samba/man/man1/smbtar.1
/usr/local/samba/man/man1/smbtree.1
/usr/local/samba/man/man1/testparm.1
/usr/local/samba/man/man1/testprns.1
/usr/local/samba/man/man1/vfstest.1
/usr/local/samba/man/man1/wbinfo.1
/usr/local/samba/man/man5/smbpasswd.5
/usr/local/samba/man/man8/mount.cifs.8
/usr/local/samba/man/man8/net.8
/usr/local/samba/man/man8/pdbedit.8
/usr/local/samba/man/man8/smbmnt.8
/usr/local/samba/man/man8/smbmount.8
/usr/local/samba/man/man8/smbpasswd.8
/usr/local/samba/man/man8/smbspool.8
/usr/local/samba/man/man8/smbumount.8
/usr/local/samba/man/man8/tdbbackup.8



%files doc
%defattr(-,root,root)
%doc /usr/local/share/samba/docs/*
%doc /usr/local/share/samba/examples/*
/usr/local/samba/man/*

%files swat
%defattr(-,root,root)
/usr/local/samba/sbin/swat
/usr/local/samba/swat/*


%changelog

* Tue Dec 23 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Too much 
