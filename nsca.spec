%define name nsca
%define version 2.7.2
%define release 2 
%define prefix /usr/local 

Summary:	Daemon and client program for sending passive check results across the network 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	nagios, nagios-plugins

%description

Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This addon allows you to send passive service check results from remote 
hosts to a central monitoring host that runs Nagios. The client can be 
used as a standalone program or can be integrated with remote Nagios 
servers that run an ocsp command to setup a distributed monitoring 
environment.


%prep
%setup -q 

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export LDFLAGS
./configure 
make all

%install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/etc/nagios
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/bin
mkdir -p ${RPM_BUILD_ROOT}/etc/init.d

install -m 0644 sample-config/nsca.cfg ${RPM_BUILD_ROOT}%{prefix}/etc/nagios/nsca.cfg-example
install -m 0644 sample-config/send_nsca.cfg ${RPM_BUILD_ROOT}%{prefix}/etc/nagios/send_nsca.cfg-example
install -m 0755 src/nsca ${RPM_BUILD_ROOT}%{prefix}/bin
install -m 0755 src/send_nsca ${RPM_BUILD_ROOT}%{prefix}/bin
install -m 0755 init-script ${RPM_BUILD_ROOT}/etc/init.d/nsca

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc Changelog SECURITY README  
%config(noreplace)%{prefix}/etc/nagios/*
%{prefix}/bin/*
%config(noreplace)%attr(-,root,root)/etc/init.d/*

%changelog
* Tue Dec 09 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.7.2-2
- Changed file locations to match Linux.
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.7.2-1
- Updated to 2.7.2
* Wed Feb 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.7.1-1
- Updated to 2.7.1
* Tue Feb 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.5-1
- Updated to 2.5
