%define name nsca
%define version 1.2.0 
%define release 1 
%define prefix /usr/local 

Summary: Daemon and client program for sending passive check results across the network 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
Patch0: nsca.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: netsaint, netsaint-plugins

%description

NetSaint is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. NetSaint runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to NetSaint.

This addon allows you to send passive service check results from remote hosts to a central monitoring host that runs NetSaint. The client can be used as a standalone program or can be integrated with remote NetSaint servers that run an ocsp command to setup a distributed monitoring environment.


%prep
%setup 

%patch0 -p1

%build

./configure 
make all

%install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/bin
mkdir -p ${RPM_BUILD_ROOT}/etc/init.d

install -m 660 send_nsca.cfg ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc/send_nsca.cfg
install -m 660 nsca.cfg ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc/nsca.cfg
install -m 755 src/send_nsca ${RPM_BUILD_ROOT}%{prefix}/netsaint/bin
install -m 755 src/nsca ${RPM_BUILD_ROOT}%{prefix}/netsaint/bin
install -m 755 init-script ${RPM_BUILD_ROOT}/etc/init.d/nsca

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%doc Changelog SECURITY README  
%config(noreplace)%{prefix}/netsaint/etc/*
%{prefix}/netsaint/bin/*
%config(noreplace)%attr(-,root,root)/etc/init.d/*
