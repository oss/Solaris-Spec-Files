%define name 	nagios_addons_ru
%define version 1.0.0
%define release 1
%define prefix /usr/local

Summary:	Host/service/network monitoring program addons
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.nagios.org
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	nagios, nagios-plugins, nsca, curl, perl-module-Net-Jabber

%description
Nagios is a program that will monitor hosts and 
services on your network.

Addons, such as allowing clients/servants to download changed
cfg files from a master and "massage" those changed cfg files 
being downloaded. Also, a custom Jabber notification script.

%prep
%setup 

%build

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers
install -m 0755 nasom $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 submit_check_result $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc README
%{prefix}/nagios/bin/*
%{prefix}/nagios/sbin/eventhandlers/submit_check_result

%changelog
* Mon Mar 30 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.0-1
- Removed old scripts, added new nasom and submit_check_result. 

* Tue Nov 07 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.5.1-1
- Added a Jabber notification script
