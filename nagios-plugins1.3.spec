%define name nagios-plugins
%define version 1.3.1
%define mysql_ver 3.23.58 
%define release 37
%define prefix /usr/local 

Summary: 	Host/service/network monitoring program plugins for Nagios 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Copyright: 	GPL
Group: 		Applications/System
Source0: 	%{name}-%{version}.tar.gz
Source1:	check_mailq
Source2:	check_ldap_clearbind
Source3:	ldapSynchCheck.py
Source4:        kerbtest.sh
Source5:        check_ldap_sync 
Source6:        check_ldap_readeverything
Source7:        check_ipmi_remote
Source8:        check_ipmi_chassis_remote
Source9:	check_ldap_reader	
Source10:	check_ldap_namingcontexts
Patch0: 	nagios-plugins.addons.patch
Patch1:         ldapSynchCheck.patch
Patch2:         reader.patch
URL:		http://www.nagios.org
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	coreutils openssl fping net-snmp radiusclient
Requires: 	nagios coreutils openssl fping net-snmp bind-dnstools

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
Summary: LDAP monitoring program plugins for Nagios 
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Requires: nagios openldap-client python-ldap

%description -n nagios-ldap-plugin
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the LDAP plugins for optional use with the
Nagios package.  

###############################################################################

%package -n nagios-mysql-plugin
Summary: MySQL monitoring program plugins for Nagios 
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Requires: nagios mysql

%description -n nagios-mysql-plugin
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the MySQL plugins for optional use with the
Nagios package.  

###############################################################################

%package -n nagios-ipmi-plugin
Summary: IPMI monitoring program plugins for Nagios 
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Requires: nagios

%description -n nagios-ipmi-plugin
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the IPMI plugins for optional use with the
Nagios package.  

###############################################################################

%package -n nagios-radius-plugin
Summary: Radius monitoring program plugins for Nagios
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Requires: nagios

%description -n nagios-radius-plugin
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the IPMI plugins for optional use with the
Nagios package.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build

# ---Craptastic configure setups---
# Make sure for the mysql plugin that you explicitly set the L and R path to
# the absolute path or it won't find anything in the subdirectories

LD_RUN_PATH=/usr/local/lib \
PATH_TO_FPING=/usr/local/sbin/fping \
PATH_TO_MAILQ=/usr/local/bin/mailq \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql-%{mysql_ver}/lib/mysql -R/usr/local/mysql-%{mysql_ver}/lib/mysql" \
CPPFLAGS="-I/usr/local/include -I/usr/local/mysql-%{mysql_ver}/include" PATH=/usr/sbin:$PATH \
LD="/usr/ccs/bin/ld" CFLAGS='-g -xs' CC='/opt/SUNWspro/bin/cc' CXX="CC"
export LD_RUN_PATH PATH_TO_FPING PATH_TO_MAILQ LDFLAGS CPPFLAGS PATH LD CFLAGS CC CXX

./configure \
	--with-df-command="/usr/local/gnu/bin/df -Pkh" \
	--with-openssl="/usr/local/ssl" \
	--with-mysql="/usr/local/mysql"

gmake all

cd contrib-brylon/

gmake

%install
make DESTDIR=$RPM_BUILD_ROOT AM_INSTALL_PROGRAM_FLAGS="" INSTALL_OPTS="" install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/etc
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0644 command.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/command.cfg-example
install -m 0700 contrib/check_file_age.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_file_age
install -m 0600 contrib-brylon/plugins.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/plugins.cfg-example

install -m 0755 contrib-brylon/check_imap ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_pop ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_jabber ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_dns_resolver ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec
install -m 0755 contrib-brylon/check_tcp_down ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec

install -m 0700 %{SOURCE2} %{buildroot}%{prefix}/nagios/libexec/check_ldap_clearbind
install -m 0700 %{SOURCE3} %{buildroot}%{prefix}/nagios/libexec/ldapSynchCheck.py

install -m 0755 %{SOURCE1} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_mailq

install -m 0755 %{SOURCE4} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/kerbtest.sh
install -m 0755 %{SOURCE5} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_sync
install -m 0755 %{SOURCE6} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_readeverything


install -m 0755 %{SOURCE7} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ipmi_remote

install -m 0755 %{SOURCE8} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ipmi_chassis_remote
install -m 0755 %{SOURCE9} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_reader
install -m 0755 %{SOURCE10} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap_namingcontexts

install -m 0755 contrib-davediff/check_clamav ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_clamav

# This files seems to not be there anymore
rm -f ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ldap


%post -n nagios-mysql-plugin
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
	                 /usr/local/info/mysql_plugin.info
fi
cat<<EOF

================================================

NOTE: MySQL3 lib is not linked to /usr/local/lib 
during its install.

Beforing using, please:

ln -s /usr/local/mysql/lib/mysql/libmysqlclient.so.10 libmysqlclient.so.10

================================================

EOF

%preun -n nagios-mysql-plugin
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	                 /usr/local/info/mysql_plugin.info
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios,755)
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
%{prefix}/nagios/libexec/check_clamav
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
%defattr(755,nagios,nagios,755)
%{prefix}/nagios/libexec/check_ldap_reader
%{prefix}/nagios/libexec/check_ldap_clearbind
%{prefix}/nagios/libexec/ldapSynchCheck.py
%{prefix}/nagios/libexec/kerbtest.sh
%{prefix}/nagios/libexec/check_ldap_sync
%{prefix}/nagios/libexec/check_ldap_readeverything
%{prefix}/nagios/libexec/check_ldap_namingcontexts

%files -n nagios-mysql-plugin
%defattr(-,nagios,nagios,755)
%{prefix}/nagios/libexec/check_mysql

%files -n nagios-ipmi-plugin
%defattr(-,nagios,nagios,755)
%{prefix}/nagios/libexec/check_ipmi_remote
%{prefix}/nagios/libexec/check_ipmi_chassis_remote

%files -n nagios-radius-plugin
%defattr(-,nagios,nagios,755)
%{prefix}/nagios/libexec/check_radius

#Doesn't exist yet in 1.3.1
#%{prefix}/nagios/libexec/check_mysql_query

%changelog
* Thu Aug 28 2008 David Diffenbaug <davediff@nbcs.rutgers.edu> 1.3.1-32
- added check_clamav plugin
* Thu Sep 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-31
- Added check_radius plugin
* Wed Jan 10 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-29
- Respun with new check_ipmi
* Wed Dec 20 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-28
- Fixed ldap patch
* Fri Dec 15 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-27
- Patched check_ldap_reader3
* Thu Dec 14 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-26
- Added check_ipmi package
* Fri Dec 08 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-25
- Bumped to build against latest version of SSL
* Thu Nov 30 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-24
- Bug
* Thu Nov 30 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-23
- Fixed libmysqlclient.so.10 dependency issue
* Mon Nov 27 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-22
- Broke out mysql plugin
* Tue Nov 14 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-21
- Added ldapsync.sh check_ldap_reader3 and patched ldapSync
* Wed Nov 08 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.3.1-20
- Added kerbtest.sh
* Tue Dec 06 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.1-19
- Fixed a bug in check_mailq
* Tue Dec 06 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.1-18
- More changes in utils.pm
* Fri Nov 18 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.1-17
- Made changes in utils.pm and check_mailq
* Mon Aug 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.3.1-15
- Broke out check_ldap_reader.pl and check_ldap_reader2 into the nagios-ldap-plugin package
- Removed the requires on openldap-client from nagios-plugins
- Removed check_file_size.pl, check_qstat.pl, and check_radius.pl, as they are no longer used
