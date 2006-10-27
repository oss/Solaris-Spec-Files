%define name nagios-plugins
%define version 1.4.4
%define release 2
%define prefix /usr/local 

Summary:       Host/service/network monitoring program plugins for Nagios 
Name:	       %{name}
Version:       %{version}
Release:       %{release}
Copyright:     GPL
Group:	       Applications/System
URL:           http://www.nagios.org
Distribution:  RU-Solaris
Vendor:        NBCS-OSS
Packager:      David Lee Halik <dhalik@nbcs.rutgers.edu>
Source0:       %{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-root
BuildRequires: coreutils openssl fping net-snmp gmp mysql
Requires:      nagios coreutils openssl fping net-snmp openldap-client openldap-lib cyrus-sasl

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
%setup -q -n %{name}-%{version}

%build
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
export LD_RUN_PATH PATH_TO_FPING LDFLAGS CPPFLAGS LD

CFLAGS='-g -xs -lm' CC='/opt/SUNWspro/bin/cc' ./configure --with-df-command="/usr/local/gnu/bin/df -Pkh" --with-openssl="/usr/local/ssl" --with-mysql="/usr/local/mysql5"

make all

%install
make DESTDIR=$RPM_BUILD_ROOT AM_INSTALL_PROGRAM_FLAGS="" INSTALL_OPTS="" install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/etc
install -m 0644 command.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/command.cfg-example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%{prefix}/nagios/libexec
%{prefix}/nagios/share
%config(noreplace)%{prefix}/nagios/etc/*

%changelog
* Fri Oct 27 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-1
- Rebuilt with MySQL
