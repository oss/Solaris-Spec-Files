%define name nagios-plugins
%define version 1.4.11
%define release 3
%define prefix /usr/local 

Summary:	Host/service/network monitoring program plugins for Nagios 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/System
URL:		http://www.nagios.org
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
Source0:	%{name}-%{version}.tar.gz
Source1:	nagios-ldap-plugin.tar.gz
Patch0:		reader.patch
Patch1:		nagios-plugins-1.4.11-ntp.patch		
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	coreutils openssl fping perl-module-Net-SNMP net-snmp gmp radiusclient
Requires:	nagios coreutils openssl fping perl-module-Net-SNMP net-snmp cyrus-sasl radiusclient

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

%package -n nagios-ldap-plugin
Summary:	LDAP monitoring program plugins for Nagios
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/System
Requires:	nagios openldap-client
BuildRequires:	openldap-devel

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

%package -n nagios-mysql5-plugin
Summary:	MySQL monitoring program plugins for Nagios
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/System
BuildRequires:	mysql5-common mysql5-devel
Requires:	nagios

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

%package -n nagios-oracle-plugin
Summary:	Host/service/network monitoring program plugins for Nagios
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Applications/System
Requires:	nagios

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

%prep
rm -rf nagios-ldap-plugin
gzip -dc %{_sourcedir}/nagios-ldap-plugin.tar.gz | tar -xf -

%setup -q

%patch1 -p0

cd ..

%patch0 -p0

%build
PATH=/opt/SUNWspro/bin:$PATH
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=/usr/local/sbin/fping
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql5/lib/ -R/usr/local/mysql5/lib/ -L/usr/local/radiusclient/lib -R/usr/local/radiusclient/lib"
CPPFLAGS="-I/usr/local/include -I/usr/local/radiusclient/include"
LD="/usr/ccs/bin/ld"
CFLAGS="-g -xs -lm"
CC="cc"
CXX="CC"
export PATH LD_RUN_PATH PATH_TO_FPING LDFLAGS CPPFLAGS LD CFLAGS CC CXX

./configure \
	--with-df-command="/usr/local/gnu/bin/df -Pkh" \
	--with-openssl="/usr/local/ssl" \
	--with-mysql="/usr/local/mysql5" \
	--with-nagios-user="nagios" \
	--with-nagios-group="nagios" \
	--disable-nls

gmake -j3 all

%install
slide rm -rf %{buildroot}

mkdir -p %{buildroot}%{prefix}/nagios/etc
mkdir -p %{buildroot}%{prefix}/nagios/libexec

slide gmake DESTDIR=%{buildroot} AM_INSTALL_PROGRAM_FLAGS="" install

slide gmake DESTDIR=%{buildroot} AM_INSTALL_PROGRAM_FLAGS="" install-root

install -m 0644 command.cfg %{buildroot}%{prefix}/nagios/etc/command.cfg-example

install -m 0755 contrib/check_ora_table_space.pl %{buildroot}%{prefix}/nagios/libexec/check_ora_table_space
install -m 0755 contrib/check_oracle_instance.pl %{buildroot}%{prefix}/nagios/libexec/check_oracle_instance
install -m 0755 contrib/check_oracle_tbs %{buildroot}%{prefix}/nagios/libexec/check_oracle_tbs

install -m 0755 ../nagios-ldap-plugin/* %{buildroot}%{prefix}/nagios/libexec/

# remove to make room for our own version
cd %{buildroot}
rm -rf usr/local/nagios/libexec/check_ldap

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

%clean

slide rm -rf %{buildroot}

%files
%defattr(-,nagios,nagios,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README REQUIREMENTS 
%{prefix}/nagios/libexec/check_apt
%{prefix}/nagios/libexec/check_breeze
%{prefix}/nagios/libexec/check_by_ssh
%{prefix}/nagios/libexec/check_clamd
%{prefix}/nagios/libexec/check_dhcp
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
%{prefix}/nagios/libexec/check_icmp
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
%{prefix}/nagios/libexec/check_radius
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
%{prefix}/nagios/libexec/check_cluster
%{prefix}/nagios/libexec/negate
%{prefix}/nagios/libexec/urlize
%{prefix}/nagios/libexec/utils.pm
%{prefix}/nagios/libexec/utils.sh
%{prefix}/nagios/libexec/check_ntp_peer
%{prefix}/nagios/libexec/check_ntp_time
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
* Fri Oct 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10-1
- Bump to 1.4.10
* Tue Aug 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.9-1
- Bump with oldssl
* Sat Apr 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.8-1
- Version Bump
- Misc. tidying
* Wed Feb 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.6-1
- Version Bump
* Thu Feb 08 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-11
- Fixed mysql5 dependancy
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
