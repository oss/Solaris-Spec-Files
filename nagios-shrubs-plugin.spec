%define name nagios-shrubs-plugin
%define version 0.1
%define release 3
%define prefix /usr/local 

Summary: Glue program (plugin) for checking output (result) of the check-backups{,-netapp} programs.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios, nagios-plugins, shrubs

%description

Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

Glue program (plugin) for checking output (result) of the check-backups{,-netapp} programs.

%prep
%setup 
%build

%install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec

install -m 0700 check_backups.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_backups

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc README  
%{prefix}/nagios/libexec/*
