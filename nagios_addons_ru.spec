%define name 	nagios_addons_ru
%define version 1.0.0
%define release 3
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
Packager:       David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	nagios, nagios-plugins, nsca, curl

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
mkdir -p $RPM_BUILD_ROOT%{prefix}/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/libexec/eventhandlers
install -m 0755 nasom $RPM_BUILD_ROOT%{prefix}/sbin
install -m 0755 submit_check_result $RPM_BUILD_ROOT%{prefix}/nagios/libexec/eventhandlers


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc
%{prefix}/sbin/nasom
%{prefix}/nagios/libexec/eventhandlers/submit_check_result
%dir %{prefix}/nagios/libexec/eventhandlers

%changelog
* Thu Apr 2 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.0-3
- updates to nasom and submit_check_result
- changed path to /usr/local/sbin/nasom
- changed path to /usr/local/nagios/libexec/eventhandlers/submit_check_result

* Mon Mar 30 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.0-1
- Removed old scripts, added new nasom and submit_check_result. 

* Tue Nov 07 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.5.1-1
- Added a Jabber notification script
