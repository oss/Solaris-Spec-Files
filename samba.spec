Summary: SMB server for UNIX systems
Name: samba
Version: 3.0.0 
Release: 1
Group: Applications/Internet
License: GPL
Source: samba-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openldap-devel

%description
Samba provides an SMB server which can be used to provide
network services to SMB (sometimes called "Lan Manager")
clients, including various versions of MS Windows, OS/2,
and other Linux machines. Samba also provides some SMB
clients, which complement the built-in SMB filesystem
in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame)
protocol.


%prep
%setup -q

%build
cd source
#not really needed
# force ./configure to see sun ld before gnu ld
#PATH="/usr/ccs/bin:/usr/local/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin:/usr/local/gnu/bin" 
#LD=/usr/ccs/bin/ld
#export PATH
#export LD
#CC='/usr/local/bin/gcc' CXX='/usr/local/bin/gcc' CPPFLAGS='-I/usr/local/include -I/usr/sfw/include' LDFLAGS='-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib' ./configure

CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/cc' CPPFLAGS='-I/usr/local/include -I/usr/sfw/include' LDFLAGS='-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib' ./configure

gmake

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
