%define name nagios-plugins
%define version 1.3.1
%define release 15
%define prefix /usr/local 

Summary: Host/service/network monitoring program plugins for Nagios 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
Patch0: nagios-plugins.addons.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios coreutils openssl openldap-client


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
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping 
LDFLAGS="-L/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
export LD_RUN_PATH PATH_TO_FPING LDFLAGS CPPFLAGS
./configure --with-df-command="/usr/local/gnu/bin/df -Pkh" --with-openssl="/usr/local/ssl"
make all
cd contrib-brylon/
make

%install
make DESTDIR=$RPM_BUILD_ROOT AM_INSTALL_PROGRAM_FLAGS="" INSTALL_OPTS="" install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/etc
install -m 0644 command.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/command.cfg-example
install -m 0700 contrib/check_file_age.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_file_age
install -m 0600 contrib-brylon/plugins.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/plugins.cfg-example

install -m 0755 contrib-brylon/check_imap ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_pop ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_jabber ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_dns_resolver ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_tcp_down ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0700 contrib-brylon/check_ldap_reader.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_reader
install -m 0700 contrib-brylon/check_radius.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_radius
install -m 0700 contrib-brylon/check_file_size.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_file_size
install -m 0700 contrib-brylon/check_qstat.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_qstat
install -m 0700 contrib-brylon/check_ldap_reader2 ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_reader2

# This files seems to not be there anymore
rm -f ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%{prefix}/nagios/libexec
%config(noreplace)%{prefix}/nagios/etc/*
