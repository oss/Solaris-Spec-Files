%define name netsaint-plugins
%define version 1.2.9
%define netsaint_release 4
%define release 3 
%define prefix /usr/local 

Summary: Host/service/network monitoring program plugins for NetSaint
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}-%{netsaint_release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl >= 0.9.6e-4ru
Requires: netsaint >= 0.0.7-4  openssl >= 0.9.6e-4ru

%description

NetSaint is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. NetSaint runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to NetSaint.

This package contains the basic plugins necessary for use with the
NetSaint package.  This package should install cleanly on almost any
RPM-based system.


%prep
%setup -n netsaint-plugins-1.2.9-4 

%build
LD_RUN_PATH="/usr/local/lib"
export LD_RUN_PATH
./configure 

make

%install
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/libexec

make DESTDIR=${RPM_BUILD_ROOT} install

install -m 600 command.cfg ${RPM_BUILD_ROOT}%{prefix}/netsaint/etc

%clean
#rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,netsaint,netsaint)
%doc AUTHORS COPYING ChangeLog FAQ INSTALL NEWS README REQUIREMENTS 
%{prefix}/netsaint/libexec
%config(noreplace)%{prefix}/netsaint/etc/command.cfg
