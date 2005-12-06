%define name nagios-plugins
%define version 1.3.1
%define release 19
%define prefix /usr/local 

Summary: 	Host/service/network monitoring program plugins for Nagios 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Copyright: 	GPL
Group: 		Applications/System
Source0: 	%{name}-%{version}.tar.gz
Source1:	check_mailq
Patch0: 	nagios-plugins.addons.patch
URL:		http://www.nagios.org
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires: 	nagios coreutils openssl


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

###############################################################################

%package -n nagios-ldap-plugin
Summary: Host/service/network monitoring program plugins for Nagios 
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Requires: nagios openldap-client nagios-plugins = %{version}-%{release}

%description -n nagios-ldap-plugin
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.

###############################################################################

%prep
%setup -n %{name}-%{version}
%patch0 -p1

%build
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping
PATH_TO_MAILQ=/usr/local/bin/mailq
LDFLAGS="-L/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
export LD_RUN_PATH PATH_TO_FPING PATH_TO_MAILQ LDFLAGS CPPFLAGS
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
install -m 0700 contrib-brylon/check_ldap_reader2 ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_reader2

install -m 0755 %{SOURCE1} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_mailq

# This files seems to not be there anymore
rm -f ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%config(noreplace)%{prefix}/nagios/etc/*
%ifos solaris2.9
   %ifarch sparc64
      %{prefix}/nagios/libexec/check_fping
      %{prefix}/nagios/libexec/check_hpjd
      %{prefix}/nagios/libexec/check_snmp
   %endif
%endif
%{prefix}/nagios/libexec/check_breeze
%{prefix}/nagios/libexec/check_by_ssh
%{prefix}/nagios/libexec/check_dig
%{prefix}/nagios/libexec/check_disk
%{prefix}/nagios/libexec/check_disk_smb
%{prefix}/nagios/libexec/check_dns
%{prefix}/nagios/libexec/check_dns_resolver
%{prefix}/nagios/libexec/check_dummy
%{prefix}/nagios/libexec/check_file_age
%{prefix}/nagios/libexec/check_flexlm
%{prefix}/nagios/libexec/check_ftp
%{prefix}/nagios/libexec/check_http
%{prefix}/nagios/libexec/check_ifoperstatus
%{prefix}/nagios/libexec/check_ifstatus
%{prefix}/nagios/libexec/check_imap
%{prefix}/nagios/libexec/check_ircd
%{prefix}/nagios/libexec/check_jabber
%{prefix}/nagios/libexec/check_load
%{prefix}/nagios/libexec/check_log
%{prefix}/nagios/libexec/check_mailq
%{prefix}/nagios/libexec/check_mrtg
%{prefix}/nagios/libexec/check_mrtgtraf
%{prefix}/nagios/libexec/check_nagios
%{prefix}/nagios/libexec/check_nntp
%{prefix}/nagios/libexec/check_nt
%{prefix}/nagios/libexec/check_ntp
%{prefix}/nagios/libexec/check_nwstat
%{prefix}/nagios/libexec/check_oracle
%{prefix}/nagios/libexec/check_overcr
%{prefix}/nagios/libexec/check_ping
%{prefix}/nagios/libexec/check_pop
%{prefix}/nagios/libexec/check_procs
%{prefix}/nagios/libexec/check_real
%{prefix}/nagios/libexec/check_rpc
%{prefix}/nagios/libexec/check_sensors
%{prefix}/nagios/libexec/check_simap
%{prefix}/nagios/libexec/check_smtp
%{prefix}/nagios/libexec/check_spop
%{prefix}/nagios/libexec/check_ssh
%{prefix}/nagios/libexec/check_swap
%{prefix}/nagios/libexec/check_tcp
%{prefix}/nagios/libexec/check_tcp_down
%{prefix}/nagios/libexec/check_time
%{prefix}/nagios/libexec/check_udp
%{prefix}/nagios/libexec/check_ups
%{prefix}/nagios/libexec/check_users
%{prefix}/nagios/libexec/check_vsz
%{prefix}/nagios/libexec/check_wave
%{prefix}/nagios/libexec/negate
%{prefix}/nagios/libexec/urlize
%{prefix}/nagios/libexec/utils.pm
%{prefix}/nagios/libexec/utils.sh

%files -n nagios-ldap-plugin
%defattr(-,nagios,nagios)
%{prefix}/nagios/libexec/check_ldap_reader
%{prefix}/nagios/libexec/check_ldap_reader2

%changelog
* Tue Dec 06 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.31-19
- Fixed a bug in check_mailq
* Tue Dec 06 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.31-18
- More changes in utils.pm
* Fri Nov 18 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.31-17
- Made changes in utils.pm and check_mailq
* Mon Aug 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.3.1-15
- Broke out check_ldap_reader.pl and check_ldap_reader2 into the nagios-ldap-plugin package
- Removed the requires on openldap-client from nagios-plugins
- Removed check_file_size.pl, check_qstat.pl, and check_radius.pl, as they are no longer used
