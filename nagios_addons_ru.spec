%define name 	nagios_addons_ru
%define version 0.5
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
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	nagios, nagios-plugins, nsca, curl

%description
Nagios is a program that will monitor hosts and 
services on your network.

Addons, such as allowing clients/servants to download changed
cfg files from a master and "massage" those changed cfg files 
being downloaded.

%prep

%setup 

%build

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/etc
install -m 0755 fix-hostcfg.pl $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 fix-nagioscfg.pl $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 fix-nagiosaddonscfg.pl $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 nagios-curl-hostname-cfg.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 nagios-curl-global-cfg.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 nagios-curl-local-cfg.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 NASOM.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 NAGIOS-bootstrap.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 c2utime $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 u2ctime $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 change-plugins.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 setupCFG.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin

install -m 0644 nagios_addons_ru.conf $RPM_BUILD_ROOT%{prefix}/nagios/etc/nagios_addons_ru.conf-example
install -m 0644 change-plugins.conf $RPM_BUILD_ROOT%{prefix}/nagios/etc/change-plugins.conf-example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc README
%{prefix}/nagios/bin/*
%config(noreplace)%{prefix}/nagios/etc/*
