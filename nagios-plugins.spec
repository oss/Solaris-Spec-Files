%define name nagios-plugins
%define version 1.4.2
%define release 1
%define prefix /usr/local 

Summary: Host/service/network monitoring program plugins for Nagios 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
#Patch0: nagios-plugins.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios coreutils gmp openssl openldap-client openldap-lib cyrus-sasl


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
#%patch0 -p1

%build
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping 
LDFLAGS="-L/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
export LD_RUN_PATH PATH_TO_FPING LDFLAGS CPPFLAGS
./configure --with-df-command="/usr/local/gnu/bin/df -Pkh" --with-openssl="/usr/local/ssl"
make all
#cd contrib-brylon/
#make

%install
make DESTDIR=$RPM_BUILD_ROOT AM_INSTALL_PROGRAM_FLAGS="" INSTALL_OPTS="" install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/etc
install -m 0644 command.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/command.cfg-example

#install -m 0700 contrib/check_file_age.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_file_age
#install -m 0700 plugins-scripts/check_mailq ${RPM_BUILD_ROOT}%{prefix}/nagios2/libexec/check_mailq

#install -m 0700 contrib-brylon/check_unwanted_ru.pl ${RPM_BUILD_ROOT}%{prefix}/nagios2/libexec/check_unwanted_ru
#install -m 0700 contrib-brylon/check_ldap_ru.pl ${RPM_BUILD_ROOT}%{prefix}/nagios2/libexec/check_ldap_ru
#install -m 0700 contrib-brylon/check_ldap2_ru.pl ${RPM_BUILD_ROOT}%{prefix}/nagios2/libexec/check_ldap2_ru

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%{prefix}/nagios/libexec
%config(noreplace)%{prefix}/nagios/etc/*
