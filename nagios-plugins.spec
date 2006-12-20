%define name nagios-plugins
%define version 1.4.5
%define release 10
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
Source1:       nagios-ldap-plugin.tar.gz
Source2:       ldapSynchCheck.py
Patch0:        reader.patch
Patch1:        ldapSynchCheck.patch
BuildRoot:     %{_tmppath}/%{name}-root
BuildRequires: coreutils openssl fping net-snmp gmp
Requires:      nagios coreutils openssl fping net-snmp cyrus-sasl

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
Requires: nagios openldap-client

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


%package -n nagios-mysql5-plugin
Summary: MySQL monitoring program plugins for Nagios
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
BuildRequires: mysql5 mysql5-devel
Requires: nagios mysql5

%description -n nagios-mysql5-plugin
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

%package -n nagios-oracle-plugin
Summary: Host/service/network monitoring program plugins for Nagios
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Requires: nagios

%description -n nagios-oracle-plugin
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

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
export LD_RUN_PATH PATH_TO_FPING LDFLAGS CPPFLAGS LD

CFLAGS='-g -xs -lm' CC='/opt/SUNWspro/bin/cc' ./configure --with-df-command="/usr/local/gnu/bin/df -Pkh" --with-openssl="/usr/local/ssl" --with-mysql="/usr/local/mysql5"

make all

cd ..
tar xvf %{SOURCE1}

%install
make DESTDIR=$RPM_BUILD_ROOT AM_INSTALL_PROGRAM_FLAGS="" INSTALL_OPTS="" install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/etc
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec

install -m 0644 command.cfg ${RPM_BUILD_ROOT}%{prefix}/nagios/etc/command.cfg-example

install -m 0755 contrib/check_ora_table_space.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_ora_table_space
install -m 0755 contrib/check_oracle_instance.pl ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_oracle_instance
install -m 0755 contrib/check_oracle_tbs ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/check_oracle_tbs

install -m 0755 %{SOURCE2} ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/ldapSynchCheck.py

cd ..

install -m 0755 nagios-ldap-plugin/* ${RPM_BUILD_ROOT}%{prefix}/nagios/libexec/



%post -n nagios-oracle-plugin
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
	         /usr/local/info/oracle_plugin.info
fi
cat<<EOF

Note: While this package does not require Oracle to install, check_ora_table_space,
check_oracle_instance, and check_oracle_tbs are intended to be used locally. They
very likely will need to be modified to include Oracle environment values. These
are contrib plugins.

check_oracle is the official plugin for remote nagios checking. Enjoy!

EOF

%preun -n nagios-oracle-plugin
if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --delete --info-dir=/usr/local/info \
	         /usr/local/info/oracle_plugin.info
fi

#Not used anymore
rm -rf %{prefix}/nagios/libexec/check_ldap			 

%clean

rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%{prefix}/nagios/libexec/check_apt
%{prefix}/nagios/libexec/check_breeze
%{prefix}/nagios/libexec/check_by_ssh
%{prefix}/nagios/libexec/check_clamd
%{prefix}/nagios/libexec/check_dig
%{prefix}/nagios/libexec/check_disk
%{prefix}/nagios/libexec/check_disk_smb
%{prefix}/nagios/libexec/check_dns
%{prefix}/nagios/libexec/check_dummy
%{prefix}/nagios/libexec/check_file_age
%{prefix}/nagios/libexec/check_flexlm
%{prefix}/nagios/libexec/check_fping
%{prefix}/nagios/libexec/check_ftp
%{prefix}/nagios/libexec/check_hpjd
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
%{prefix}/nagios/libexec/check_nntps
%{prefix}/nagios/libexec/check_nt
%{prefix}/nagios/libexec/check_ntp
%{prefix}/nagios/libexec/check_nwstat
%{prefix}/nagios/libexec/check_overcr
%{prefix}/nagios/libexec/check_ping
%{prefix}/nagios/libexec/check_pop
%{prefix}/nagios/libexec/check_procs
%{prefix}/nagios/libexec/check_real
%{prefix}/nagios/libexec/check_rpc
%{prefix}/nagios/libexec/check_sensors
%{prefix}/nagios/libexec/check_simap
%{prefix}/nagios/libexec/check_smtp
%{prefix}/nagios/libexec/check_snmp
%{prefix}/nagios/libexec/check_spop
%{prefix}/nagios/libexec/check_ssh
%{prefix}/nagios/libexec/check_ssmtp
%{prefix}/nagios/libexec/check_swap
%{prefix}/nagios/libexec/check_tcp
%{prefix}/nagios/libexec/check_time
%{prefix}/nagios/libexec/check_udp
%{prefix}/nagios/libexec/check_ups
%{prefix}/nagios/libexec/check_users
%{prefix}/nagios/libexec/check_wave
%{prefix}/nagios/libexec/negate
%{prefix}/nagios/libexec/urlize
%{prefix}/nagios/libexec/utils.pm
%{prefix}/nagios/libexec/utils.sh
%{prefix}/nagios/share
%config(noreplace)%{prefix}/nagios/etc/*

%files -n nagios-ldap-plugin
%defattr(-,nagios,nagios,755)
%{prefix}/nagios/libexec/check_ldap_reader
%{prefix}/nagios/libexec/check_ldap_reader2
%{prefix}/nagios/libexec/check_ldap_clearbind
%{prefix}/nagios/libexec/ldapSynchCheck.py
%{prefix}/nagios/libexec/kerbtest.sh
%{prefix}/nagios/libexec/ldapsync.sh
%{prefix}/nagios/libexec/check_ldap_reader3

%files -n nagios-mysql5-plugin
%defattr(-,nagios,nagios,755)
%{prefix}/nagios/libexec/check_mysql
%{prefix}/nagios/libexec/check_mysql_query

%files -n nagios-oracle-plugin
%defattr(-,nagios,nagios,755)
%{prefix}/nagios/libexec/check_oracle
%{prefix}/nagios/libexec/check_ora_table_space
%{prefix}/nagios/libexec/check_oracle_instance
%{prefix}/nagios/libexec/check_oracle_tbs

%changelog
* Wed Dec 20 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-9
- Fixed ldap patch
* Fri Dec 15 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-7
- Patched check_ldap_reader3
* Fri Dec 08 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-6
- Bumped for new SSL version
* Thu Nov 30 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-5
- Fixed nag message bug
* Mon Nov 27 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-4
- Broke out MySQL to MySQL5-plugin
* Tue Nov 21 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-3
- Broke out Oracle plugins and spun LDAP tar
* Wed Nov 08 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-2
- Added kerbtest.sh to check-ldap-plugin
* Thu Nov 02 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-1
- Version Bump
* Tue Oct 31 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-4
- Bump
* Tue Oct 31 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-3
- Broke out MySQL into it's own package
* Tue Oct 31 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-2
- Broke out LDAP into it's own package
* Fri Oct 27 2006 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-1
- Rebuilt with MySQL
