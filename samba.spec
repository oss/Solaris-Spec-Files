%define smb_prefix %{_prefix}/samba

##########################################################
#
# NOTE: In order for build to finish properly the file
# unhardlinkify.py must exist in your path. It can be
# found on cvs in remote-rpm if you're looking for it.
#
#########################################################


Summary:	SMB server for UNIX systems
Name:		samba
Version:	3.2.4
Release:	1
Group:		Applications/Internet
License:	GPL
Source0:	samba-%{version}.tar.gz
Source1:	samba.initd
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	openldap-devel >= 2.4, rpm-devel
BuildConflicts:	heimdal-devel
Requires:	samba-common = %{version}-%{release}
Conflicts:	samba-client < %{version}-%{release}, samba-client > %{version}-%{release}
Conflicts:	samba-server < %{version}-%{release}, samba-server > %{version}-%{release}

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
Requires: %{name} = %{version}-%{release}

%description common
Core and Configuration for Samba

%package server
Group: Applications/Internet
Summary: Samba server and associated man pages
Requires: %{name} = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}

%description server
Samba server and associated man pages

%package client
Group: Applications/Internet
Summary: Samba client
Requires: %{name} = %{version}-%{release}

%description client
Samba client

%package doc
Group: Applications/Internet
Summary: Samba docs
Requires: %{name} = %{version}-%{release}

%description doc
Samba docs

%package swat
Group: Applications/Internet
Summary: Samba swat
Requires: %{name} = %{version}-%{release}

%description swat
Samba swat

%prep
%setup -q

%build
cd source
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC='cc' CXX='CC'
CPPFLAGS='-I/usr/local/include'
LDFLAGS='-L/usr/local/lib -R/usr/local/lib'
export PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=%{smb_prefix} --mandir=%{smb_prefix}/man \
	--with-ldap --with-piddir=/var/run --localstatedir=%{_var}/samba

gmake

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/samba
cp -r examples %{buildroot}%{_datadir}/samba
cp -r docs %{buildroot}%{_datadir}/samba

mkdir -p %{buildroot}%{_var}/samba
mkdir -p %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/samba

rm -rf var

cd source
make install DESTDIR=%{buildroot}

cd %{buildroot}
python /usr/local/bin/unhardlinkify.py ./

%post
cat << EOF
smb.conf goes in %{smb_prefix}/lib
EOF

%clean
rm -rf %{buildroot}

%files
#empty

%files common
%defattr(-,root,root)
%dir %{smb_prefix}
%{smb_prefix}/lib
%{smb_prefix}/include
%{_var}/samba
%dir %{smb_prefix}/bin
%{smb_prefix}/bin/ldbadd
%{smb_prefix}/bin/ldbdel
%{smb_prefix}/bin/ldbedit
%{smb_prefix}/bin/ldbmodify
%{smb_prefix}/bin/ldbsearch
%dir %{smb_prefix}/sbin
%dir %{smb_prefix}/man
%dir %{smb_prefix}/man/man1
%dir %{smb_prefix}/man/man5
%dir %{smb_prefix}/man/man7
%dir %{smb_prefix}/man/man8
%{smb_prefix}/man/man5/smb.conf.5
%{smb_prefix}/man/man5/lmhosts.5
%{smb_prefix}/man/man7/samba.7
%{smb_prefix}/man/man7/libsmbclient.7
%{smb_prefix}/man/man8/vfs*.8
%{smb_prefix}/man/man8/eventlogadm.8

%files server
%defattr(-,root,root)
%attr(700,root,root) %{smb_prefix}/private
%attr(755,root,root) /etc/init.d/samba
%{smb_prefix}/bin/smbcontrol
%{smb_prefix}/sbin/smbd
%{smb_prefix}/sbin/nmbd
%{smb_prefix}/sbin/winbindd
%{smb_prefix}/man/man7/pam_winbind.7
%{smb_prefix}/man/man8/nmbd.8
%{smb_prefix}/man/man8/smbd.8
%{smb_prefix}/man/man8/winbindd.8
%{smb_prefix}/man/man8/idmap*.8

%files client
%defattr(-,root,root)
%{smb_prefix}/bin/findsmb
%{smb_prefix}/bin/net
%{smb_prefix}/bin/nmblookup
%{smb_prefix}/bin/ntlm_auth
%{smb_prefix}/bin/pdbedit
%{smb_prefix}/bin/profiles
%{smb_prefix}/bin/rpcclient
%{smb_prefix}/bin/smbcacls
%{smb_prefix}/bin/smbclient
%{smb_prefix}/bin/smbcquotas
%{smb_prefix}/bin/smbpasswd
%{smb_prefix}/bin/smbspool
%{smb_prefix}/bin/smbstatus
%{smb_prefix}/bin/smbtar
%{smb_prefix}/bin/smbtree
%{smb_prefix}/bin/tdbbackup
%{smb_prefix}/bin/tdbdump
%{smb_prefix}/bin/testparm
%{smb_prefix}/bin/wbinfo
%{smb_prefix}/bin/eventlogadm
%{smb_prefix}/bin/smbget
%{smb_prefix}/bin/tdbtool
%{smb_prefix}/man/man1/*
%{smb_prefix}/man/man5/smbpasswd.5
%{smb_prefix}/man/man5/smbgetrc.5
%{smb_prefix}/man/man8/net.8
%{smb_prefix}/man/man8/pdbedit.8
%{smb_prefix}/man/man8/smbpasswd.8
%{smb_prefix}/man/man8/smbspool.8
%{smb_prefix}/man/man8/tdb*.8
%{smb_prefix}/man/man8/*cifs*.8

%files doc
%defattr(-,root,root)
%docdir %{_datadir}/samba/docs
%docdir %{_datadir}/samba/examples
%{_datadir}/samba/docs
%{_datadir}/samba/examples

%files swat
%defattr(-,root,root)
%{smb_prefix}/sbin/swat
%{smb_prefix}/swat
%{smb_prefix}/man/man8/swat.8

%changelog
* Tue Oct 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.2.4-1
- Made some changes to the spec file, built against openldap 2.4, and updated to version 3.2.4
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.0.30-1
- Updated to version 3.0.30
* Tue Sep 04 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.0.25c-1
- Added conflicts in order to ensure sub-package coherency
- Bump to 3.0.25c
* Fri May 19 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Require explicit same version.
* Wed May 09 2007 David Lee Halik <dhalik@nbcs.rutgers.edu>
 - Release bump because of number mismatch
* Tue Dec 23 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Too much 
