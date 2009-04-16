%define prefix /usr/local

Name: nagios-plugins
Version: 1.4.13
Release: 4
Summary: Host/service/network monitoring program plugins for Nagios

Group: Applications/System
License: GPLv2+
URL: http://nagiosplug.sourceforge.net/
Source0: http://dl.sf.net/sourceforge/nagiosplug/%{name}-%{version}.tar.gz
Source1: nagios-plugins.README.Fedora
Patch0: nagios-plugins-1.4.3-subst.patch
Patch1: nagios-plugins-1.4.3-ntpd.patch
Patch2: nagios-plugins-check_log-path.patch
Patch3: nagios-plugins-1.4.13-trusted_path.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: openldap-devel
BuildRequires: mysql-devel
BuildRequires: net-snmp-devel
BuildRequires: net-snmp-utils
BuildRequires: samba-client
BuildRequires: gettext
BuildRequires: %{_bindir}/ssh
BuildRequires: bind-dnstools
BuildRequires: %{_bindir}/mailq
BuildRequires: %{_sbindir}/fping
BuildRequires: perl-module-Net-SNMP
BuildRequires: radiusclient

%global reqfilt sh -c "%{__perl_requires} | sed -e 's!perl(utils)!nagios-plugins-perl!'"
%define __perl_requires %{reqfilt}


%description

Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios. This package
contains those plugins.

%package all
Summary: Nagios Plugins - All plugins
Group: Applications/System
Requires: nagios-plugins-breeze, nagios-plugins-by_ssh, nagios-plugins-dhcp, nagios-plugins-dig, nagios-plugins-disk, nagios-plugins-disk_smb, nagios-plugins-dns, nagios-plugins-dummy, nagios-plugins-file_age, nagios-plugins-flexlm, nagios-plugins-fping, nagios-plugins-hpjd, nagios-plugins-http, nagios-plugins-icmp, nagios-plugins-ircd, nagios-plugins-ldap, nagios-plugins-load, nagios-plugins-log, nagios-plugins-mailq, nagios-plugins-mrtg, nagios-plugins-mrtgtraf, nagios-plugins-mysql, nagios-plugins-nagios, nagios-plugins-nt, nagios-plugins-ntp, nagios-plugins-nwstat, nagios-plugins-oracle, nagios-plugins-overcr, nagios-plugins-ping, nagios-plugins-procs, nagios-plugins-real, nagios-plugins-rpc, nagios-plugins-smtp, nagios-plugins-snmp, nagios-plugins-ssh, nagios-plugins-swap, nagios-plugins-tcp, nagios-plugins-time, nagios-plugins-udp, nagios-plugins-ups, nagios-plugins-users, nagios-plugins-wave, nagios-plugins-cluster
%ifnarch ppc ppc64 sparc sparc64
Requires: nagios-plugins-sensors
%endif

%description all
This package provides all Nagios plugins.

%package apt
Summary: Nagios Plugin - check_apt
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description apt
Provides check_apt support for Nagios.

%package breeze
Summary: Nagios Plugin - check_breeze
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description breeze
Provides check_breeze support for Nagios.

%package cluster
Summary: Nagios Plugin - check_cluster
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description cluster
Provides check_cluster support for Nagios.

%package by_ssh
Summary: Nagios Plugin - check_by_ssh
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/ssh

%description by_ssh
Provides check_by_ssh support for Nagios.

%package dhcp
Summary: Nagios Plugin - check_dhcp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description dhcp
Provides check_dhcp support for Nagios.

%package dig
Summary: Nagios Plugin - check_dig
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/dig

%description dig
Provides check_dig support for Nagios.

%package disk
Summary: Nagios Plugin - check_disk
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description disk
Provides check_disk support for Nagios.

%package disk_smb
Summary: Nagios Plugin - check_disk_smb
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description disk_smb
Provides check_disk_smb support for Nagios.

%package dns
Summary: Nagios Plugin - check_dns
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/nslookup

%description dns
Provides check_dns support for Nagios.

%package dummy
Summary: Nagios Plugin - check_dummy
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description dummy
Provides check_dummy support for Nagios.
This plugin does not actually check anything, simply provide it with a flag
0-4 and it will return the corresponding status code to Nagios.

%package file_age
Summary: Nagios Plugin - check_file_age
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description file_age
Provides check_file_age support for Nagios.

%package flexlm
Summary: Nagios Plugin - check_flexlm
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description flexlm
Provides check_flexlm support for Nagios.

%package fping
Summary: Nagios Plugin - check_fping
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_sbindir}/fping

%description fping
Provides check_fping support for Nagios.

%package hpjd
Summary: Nagios Plugin - check_hpjd
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description hpjd
Provides check_hpjd support for Nagios.

%package http
Summary: Nagios Plugin - check_http
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description http
Provides check_http support for Nagios.

%package icmp
Summary: Nagios Plugin - check_icmp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description icmp
Provides check_icmp support for Nagios.

%package ifoperstatus
Summary: Nagios Plugin - check_ifoperstatus
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ifoperstatus
Provides check_ifoperstatus support for Nagios to monitor network interfaces.

%package ifstatus
Summary: Nagios Plugin - check_ifstatus
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ifstatus
Provides check_ifstatus support for Nagios to monitor network interfaces.

%package ircd
Summary: Nagios Plugin - check_ircd
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ircd
Provides check_ircd support for Nagios.

%package ldap
Summary: Nagios Plugin - check_ldap
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ldap
Provides check_ldap support for Nagios.

%package load
Summary: Nagios Plugin - check_load
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description load
Provides check_load support for Nagios.

%package log
Summary: Nagios Plugin - check_log
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description log
Provides check_log support for Nagios.

%package mailq
Summary: Nagios Plugin - check_mailq
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description mailq
Provides check_mailq support for Nagios.

%package mrtg
Summary: Nagios Plugin - check_mrtg
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description mrtg
Provides check_mrtg support for Nagios.

%package mrtgtraf
Summary: Nagios Plugin - check_mrtgtraf
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description mrtgtraf
Provides check_mrtgtraf support for Nagios.

%package mysql
Summary: Nagios Plugin - check_mysql
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description mysql
Provides check_mysql and check_mysql_query support for Nagios.

%package nagios
Summary: Nagios Plugin - check_nagios
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description nagios
Provides check_nagios support for Nagios.

%package nt
Summary: Nagios Plugin - check_nt
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description nt
Provides check_nt support for Nagios.

%package ntp
Summary: Nagios Plugin - check_ntp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ntp
Provides check_ntp support for Nagios.

%package nwstat
Summary: Nagios Plugin - check_nwstat
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description nwstat
Provides check_nwstat support for Nagios.

%package oracle
Summary: Nagios Plugin - check_oracle
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description oracle
Provides check_oracle support for Nagios.

%package overcr
Summary: Nagios Plugin - check_overcr
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description overcr
Provides check_overcr support for Nagios.

%package perl
Summary: Nagios plugins perl dep.
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description perl
Perl dep for nagios plugins.  This is *NOT* an actual plugin it simply provides
utils.pm

%package ping
Summary: Nagios Plugin - check_ping
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ping
Provides check_ping support for Nagios.

%package procs
Summary: Nagios Plugin - check_procs
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description procs
Provides check_procs support for Nagios.

%package radius
Summary: Nagios Plugin - check_radius
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description radius
Provides check_radius support for Nagios.

%package real
Summary: Nagios Plugin - check_real
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description real
Provides check_real (rtsp) support for Nagios.

%package rpc
Summary: Nagios Plugin - check_rpc
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description rpc
Provides check_rpc support for Nagios.

%ifnarch ppc ppc64 sparc sparc64
%package sensors
Summary: Nagios Plugin - check_sensors
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Requires: /bin/egrep
Requires: %{_bindir}/sensors

%description sensors
Provides check_sensors support for Nagios.
%endif

%package smtp
Summary: Nagios Plugin - check_smtp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description smtp
Provides check_smtp support for Nagios.

%package snmp
Summary: Nagios Plugin - check_snmp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Requires: %{_bindir}/snmpgetnext
Requires: %{_bindir}/snmpget

%description snmp
Provides check_snmp support for Nagios.

%package ssh
Summary: Nagios Plugin - check_ssh
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ssh
Provides check_ssh support for Nagios.

%package swap
Summary: Nagios Plugin - check_swap
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description swap
Provides check_swap support for Nagios.

%package tcp
Summary: Nagios Plugin - check_tcp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}
Provides: nagios-plugins-ftp, nagios-plugins-imap, nagios-plugins-jabber, nagios-plugins-nntp, nagios-plugins-nntps, nagios-plugins-pop, nagios-plugins-simap, nagios-plugins-spop, nagios-plugins-ssmtp, nagios-plugins-udp2

%description tcp
Provides check_tcp, check_ftp, check_imap, check_jabber, check_nntp, 
check_nntps, check_pop, check_simap, check_spop, check_ssmtp, check_udp2
and check_clamd support for Nagios.

%package time
Summary: Nagios Plugin - check_time
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description time
Provides check_time support for Nagios.

%package udp
Summary: Nagios Plugin - check_udp
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description udp
Provides check_udp support for Nagios.

%package ups
Summary: Nagios Plugin - check_ups
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description ups
Provides check_ups support for Nagios.

%package users
Summary: Nagios Plugin - check_users
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description users
Provides check_users support for Nagios.

%package wave
Summary: Nagios Plugin - check_wave
Group: Applications/System
Requires: nagios-plugins = %{version}-%{release}

%description wave
Provides check_wave support for Nagios.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0

%build

PATH=/opt/SUNWspro/bin:$PATH
LD_RUN_PATH=/usr/local/lib
PATH_TO_FPING=%{_sbindir}/fping
PATH_TO_NTPQ=/usr/sbin/ntpq 
PATH_TO_NTPDC=/usr/sbin/ntpdc 
PATH_TO_NTPDATE=/usr/sbin/ntpdate 
PATH_TO_RPCINFO=/usr/bin/rpcinfo
PATH_TO_PING=/usr/sbin/ping
PATH_TO_QMAIL_QSTAT=/usr/local/qmail/bin/qmail-qstat
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql5/lib/ -R/usr/local/mysql5/lib/ -L/usr/local/radiusclient/lib -R/usr/local/radiusclient/lib"
CPPFLAGS="-I/usr/local/include -I/usr/local/radiusclient/include"
LD="/usr/ccs/bin/ld"
CFLAGS="-g -xs -lm"
CC="cc"
CXX="CC"
export PATH LD_RUN_PATH PATH_TO_FPING PATH_TO_NTPQ PATH_TO_NTPDC PATH_TO_NTPDATE PATH_TO_RPCINFO PATH_TO_PING PATH_TO_QMAIL_QSTAT LDFLAGS CPPFLAGS LD CFLAGS CC CXX

./configure \
        --with-df-command="/usr/local/gnu/bin/df -Pkh" \
        --with-openssl="/usr/local/ssl" \
        --with-mysql="/usr/local/mysql5" \
        --with-nagios-user="nagios" \
        --with-nagios-group="nagios" \
        --disable-nls \
        --with-ps-command="`which ps` -eo 's uid pid ppid vsz rss pcpu etime comm args'" \
        --with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
        --with-ps-cols=10 \
        --enable-extra-opts \
        --with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos'

#hack to fix for solaris ping command
sed -e 's/PING_COMMAND ""/PING_COMMAND "\/usr\/sbin\/ping -s %s 64 %u"/' config.h > config.h.new
mv config.h.new config.h

make %{?_smp_mflags}
cd plugins
make check_ldap
make check_radius
make check_swap

cd ..


cp %{SOURCE1} ./README.Fedora

%install
sed -i 's,^MKINSTALLDIRS.*,MKINSTALLDIRS = ../mkinstalldirs,' po/Makefile
slide %{__rm} -rf %{buildroot}
slide %{__make} AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=%{buildroot} install
slide %{__make} AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=%{buildroot} install-root

#%{__install} -m 0755 plugins-root/check_icmp %{buildroot}/%{prefix}/nagios/libexec
#%{__install} -m 0755 plugins-root/check_dhcp %{buildroot}/%{prefix}/nagios/libexec
#%{__install} -m 0755 plugins/check_ldap %{buildroot}/%{prefix}/nagios/libexec
#%{__install} -m 0755 plugins/check_radius %{buildroot}/%{prefix}/nagios/libexec
slide %{__install} -m 0755 plugins/check_swap %{buildroot}/%{prefix}/nagios/libexec

slide %{__rm} -f %{buildroot}/%{prefix}/nagios/lib/charset.alias

%ifarch ppc ppc64 sparc sparc64
slide %{__rm} -f %{buildroot}/%{prefix}/nagios/libexec/check_sensors
%endif

slide %{__chmod} 644 %{buildroot}/%{prefix}/nagios/libexec/utils.pm

slide mkdir -m 0775 -p %{buildroot}/%{prefix}/doc/nagios-plugins-1.4.13

%find_lang %{name}

%clean
slide %{__rm} -rf %{buildroot}

%files all

%files apt
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_apt

%files breeze
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_breeze

%files cluster
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_cluster

%files by_ssh
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_by_ssh

%files dhcp
%defattr(4750,root,nagios,-)
%{prefix}/nagios/libexec/check_dhcp

%files dig
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_dig

%files disk
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_disk

%files disk_smb
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_disk_smb

%files dns
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_dns

%files dummy
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_dummy

%files file_age
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_file_age

%files flexlm
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_flexlm

%files fping
%defattr(-,nagios,nagios,-)
%attr(4750,root,nagios)%{prefix}/nagios/libexec/check_fping

%files hpjd
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_hpjd

%files http
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_http

%files icmp
%defattr(-,nagios,nagios,-)
%attr(4750,root,nagios)%{prefix}/nagios/libexec/check_icmp

%files ifoperstatus
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ifoperstatus

%files ifstatus
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ifstatus

%files ircd
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ircd

%files ldap
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ldap
%{prefix}/nagios/libexec/check_ldaps

%files load
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_load

%files log
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_log

%files mailq
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_mailq

%files mrtg
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_mrtg

%files mrtgtraf
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_mrtgtraf

%files mysql
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_mysql
%{prefix}/nagios/libexec/check_mysql_query

%files nagios
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_nagios

%files nt
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_nt

%files ntp
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ntp
%{prefix}/nagios/libexec/check_ntp_peer
%{prefix}/nagios/libexec/check_ntp_time

%files nwstat
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_nwstat

%files oracle
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_oracle

%files overcr
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_overcr

%files perl
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/utils.pm

%files ping
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ping

%files procs
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_procs

%files radius
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_radius

%files real
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_real

%files rpc
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_rpc

%ifnarch ppc ppc64 sparc sparc64
%files sensors
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_sensors
%endif

%files smtp
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_smtp

%files snmp
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_snmp

%files ssh
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ssh

%files swap
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_swap

%files tcp
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_tcp
%{prefix}/nagios/libexec/check_clamd
%{prefix}/nagios/libexec/check_ftp
%{prefix}/nagios/libexec/check_imap
%{prefix}/nagios/libexec/check_jabber
%{prefix}/nagios/libexec/check_nntp
%{prefix}/nagios/libexec/check_nntps
%{prefix}/nagios/libexec/check_pop
%{prefix}/nagios/libexec/check_simap
%{prefix}/nagios/libexec/check_spop
%{prefix}/nagios/libexec/check_ssmtp

%files time
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_time

%files udp
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_udp

%files ups
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_ups

%files users
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_users

%files wave
%defattr(-,nagios,nagios,-)
%{prefix}/nagios/libexec/check_wave

%files  -f %{name}.lang
%defattr(-,nagios,nagios,-)
%doc ChangeLog CODING COPYING FAQ INSTALL LEGAL README REQUIREMENTS SUPPORT THANKS README.Fedora
%dir %{prefix}/nagios
%dir %{prefix}/nagios/libexec
%{prefix}/nagios/libexec/negate
%{prefix}/nagios/libexec/urlize
%{prefix}/nagios/libexec/utils.sh

%changelog
* Thu Apr 16 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4.13-4
- fixed some issues with the trusted_path patch

* Tue Apr 14 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4.13-3
- fixed trusted_path issue by patching bad regex in subst.in awk script
- added $PATH_TO_QMAIL_QSTAT to environment 

* Thu Apr 2 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4.13-2
- removed %{_bindir}/mailq from nagios-plugins-mailq Requires
- removed /usr/local/nagios/etc - not necessary
- rm -f charset.alias

* Tue Mar 31 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4.13-1
- rewrote linux spec file for Solaris

* Mon Feb 09 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4.13-12
- built against mysql-5.1.30

* Tue Jan 13 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> 1.4.13-12
- Removed check_game plugin 

* Mon Oct 20 2008 Robert M. Albrecht <romal@gmx.de> 1.4.13-11
- Enabled --with-extra-opts again

* Mon Oct 20 2008 Robert M. Albrecht <romal@gmx.de> 1.4.13-10
- removed provides perl plugins Bugzilla 457404

* Thu Oct 16 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-9
- This is a "CVS is horrible" rebuild

* Thu Oct  9 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-8
- Rebuilt with a proper patch

* Wed Oct  8 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-7
- Added changed recent permission changes to allow nagios group to execute

* Wed Oct  8 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-6
- Fixed up some permission issues

* Mon Oct  6 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-5
- Fixing patch, missing semicolon

* Sun Sep 28 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.13-4
- Upstream released new version #464419
- Added patch fix for check_linux_raid #253898
- Upstream releases fix for #451015 - check_ntp_peers
- Upstream released fix for #459309 - check_ntp
- Added Provides Nagios::Plugins for #457404
- Fixed configure line for #458985 check_procs

* Tue Jul 10 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-3
- Removed --with-extra-opts, does not build in Koji

* Mon Jun 30 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-2
- Enabled --with-extra-opts

* Sun Jun 29 2008 Robert M. Albrecht <romal@gmx.de> 1.4.12-1
- Upstream released version 1.4.12
- Removed patches ping_timeout.patch and pgsql-fix.patch

* Wed Apr 30 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-4
- added patch for check_pgsql

* Wed Apr 09 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-2
- Fix for 250588

* Thu Feb 28 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.11-1
- Upstream released version 1.4.11
- Added check_ntp peer and time

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.10-6
- Autorebuild for GCC 4.3

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> 1.4-10-5
- Rebuild for gcc43

* Thu Jan 10 2008 Mike McGrath <mmcgrath@redhat.com> 1.4.10-4
- Fixed check_log plugin #395601

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.10-2
- Rebuild for deps

* Thu Dec 06 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.10-1
- Upstream released new version
- Removed some patches

* Fri Oct 26 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-9
- Fix for Bug 348731 and CVE-2007-5623

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-7
- Rebuild for BuildID
- License change

* Fri Aug 10 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-6
- Fix for check_linux_raid - #234416
- Fix for check_ide_disk - #251635

* Tue Aug 07 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-2
- Fix for check_smtp - #251049

* Fri Apr 13 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.8-1
- Upstream released new version

* Fri Feb 23 2007 Mike McGrath <mmcgrath@redhat.com> 1.4.6-1
- Upstream released new version

* Sun Dec 17 2006 Mike McGrath <imlinux@gmail.com> 1.4.5-1
- Upstream released new version

* Fri Oct 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.4-2
- Enabled check_smart_ide
- Added patch for linux_raid
- Fixed permissions on check_icmp

* Tue Oct 24 2006 Mike McGrath <imlinux@gmail.com> 1.4.4-1
- Upstream new version
- Disabled check_ide_smart (does not compile cleanly/too lazy to fix right now)
- Added check_apt

* Sun Aug 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-18
- Removed utils.pm from the base nagios-plugins package into its own package

* Tue Aug 15 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-17
- Added requires qstat for check_game

* Thu Aug 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-16
- Providing path to qstat

* Thu Aug 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-15
- Fixed permissions on check_dhcp
- Added check_game
- Added check_radius
- Added patch for ntp

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-14
- Patched upstream issue: 196356

* Sun Jul 23 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-13
- nagios-plugins-all now includes nagios-plugins-mysql

* Thu Jun 22 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-12
- removed sensors support for sparc and sparc64

* Thu Jun 22 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-11
- Created a README.Fedora explaining how to install other plugins

* Sun Jun 11 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-9
- Removed check_sensors in install section

* Sat Jun 10 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-8
- Inserted conditional blocks for ppc exception.

* Wed Jun 07 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-7
- Removed sensors from all plugins and added excludearch: ppc

* Tue Jun 06 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-6
- For ntp plugins requires s/ntpc/ntpdc/

* Sun Jun 03 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-5
- Fixed a few syntax errors and removed an empty export

* Sat May 19 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-4
- Now using configure macro instead of ./configure
- Added BuildRequest: perl(Net::SNMP)
- For reference, this was bugzilla.redhat.com ticket# 176374

* Sat May 19 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-3
- Added check_ide_smart
- Added some dependencies
- Added support for check_if* (perl-Net-SNMP now in extras)
- nagios-plugins now owns dir %{_libdir}/nagios

* Sat May 13 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-2
- Added a number of requires that don't get auto-detected

* Sun May 07 2006 Mike McGrath <imlinux@gmail.com> 1.4.3-1
- Upstream remeased 1.4.3

* Tue Apr 18 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-9
- Fixed a typo where nagios-plugins-all required nagios-plugins-httpd

* Mon Mar 27 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-8
- Updated to CVS head for better MySQL support

* Sun Mar 5 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-7
- Added a nagios-plugins-all package

* Wed Feb 1 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-6
- Added provides for check_tcp

* Mon Jan 30 2006 Mike McGrath <imlinux@gmail.com> 1.4.2-5
- Created individual packages for all check_* scripts

* Tue Dec 20 2005 Mike McGrath <imlinux@gmail.com> 1.4.2-4
- Fedora friendly spec file

* Mon May 23 2005 Sean Finney <seanius@seanius.net> - cvs head
- just include the nagios plugins directory, which will automatically include
  all generated plugins (which keeps the build from failing on systems that
  don't have all build-dependencies for every plugin)

* Tue Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

* Tue Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

