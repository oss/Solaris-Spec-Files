Summary: SMB server for UNIX systems
Name: samba
Version: 2.2.0
Release: 3
Group: Applications/Internet
License: GPL
Source: samba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
%description
Samba provides an SMB server which can be used to provide
network services to SMB (sometimes called "Lan Manager")
clients, including various versions of MS Windows, OS/2,
and other Linux machines. Samba also provides some SMB
clients, which complement the built-in SMB filesystem
in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame)
protocol.

Samba-2.2 features working NT Domain Control capability and 
includes the SWAT (Samba Web Administration Tool) that 
allows samba's smb.conf file to be remotely managed using your 
favourite web browser. For the time being this is being
enabled on TCP port 901 via inetd.

Users are advised to use Samba-2.2 as a Windows NT4
Domain Controller only on networks that do NOT have a Windows
NT Domain Controller. This release does NOT as yet have
Backup Domain control ability.

Please refer to the WHATSNEW.txt document for fixup information.
This binary release includes encrypted password support.

Please read the smb.conf file and ENCRYPTION.txt in the
docs directory for implementation details.

  [ from samba2.spec ]

%prep
%setup -q

%build
cd source
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --with-pam --with-smbclient
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/samba
cd source
make install BASEDIR=$RPM_BUILD_ROOT/usr/local/samba \
             prefix=$RPM_BUILD_ROOT/usr/local/samba

%post
cat <<EOF
smb.conf goes in /usr/local/samba/lib.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%doc examples/*
/usr/local/samba
