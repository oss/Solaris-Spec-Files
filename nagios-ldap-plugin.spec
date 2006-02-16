%define name nagios-ldap-plugin
%define version 1.3.1
%define release 15
%define prefix /usr/local 

Summary: Host/service/network monitoring program plugins for Nagios 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: nagios-plugins-%{version}.tar.gz
Patch0: nagios-plugins.addons.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios openldap-client
Requires: nagios-plugins = %{version}-%{release}


%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.


%prep
%setup -n %{name}-%{version}
%patch0 -p1

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0700 contrib-check_ldap_reader.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_reader
install -m 0700 contrib-check_ldap_reader2 ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_reader2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%{prefix}/nagios/libexec

%changelog
* Mon Aug 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.3.1-15
- Broke out check_ldap_reader.pl and check_ldap_reader2.pl from the nagios-ldap-plugin package
