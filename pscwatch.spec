%define name pscwatch
%define version 1.0b3 
%define release 1 
%define prefix /usr/local 

Summary: Ensures that passive service checks are being submitted at regular intervals. 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: ru_netsaint, netsaint-plugins, ru_nsca 

%description

NetSaint is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. NetSaint runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to NetSaint.

This addon's sole purpose in life is to ensure that passive service 
checks are being submitted to NetSaint on a regular basis. This addon 
is designed to be used on a central monitoring server when setting up 
a distributed monitoring environment. 

%prep
%setup 

%build

./configure
make

%install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/bin
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc

install -m 755 src/pscwatch  ${RPM_BUILD_ROOT}%{prefix}/netsaint/bin/pscwatch
install -m 644 pscwatch.cfg ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc/pscwatch.cfg.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%doc Changelog  
%{prefix}/netsaint/bin/*
%{prefix}/netsaint/etc/*
