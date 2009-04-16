Summary:	Host/service/network monitoring program addons
Name:		nagios_plugins_ru
Version:	0.8.6
Release:	6
License:	Rutgers
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.nagios.org
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
BuildRoot: 	%{_tmppath}/%{name}-root
Packager: 	David Diffenbaugh <davediff@nbcs.rutgers.edu>
Requires:	nagios-plugins nagios-plugins-disk nagios-plugins-file_age nagios-plugins-load nagios-plugins-users nagios-plugins-mailq nagios-plugins-procs nagios-plugins-perl
%description
Nagios is a program that will monitor hosts and 
services on your network.

These plugins are home-grown at Rutgers. 
They require entries in sudoers, for instance. Be careful.


%package -n nagios_plugins_ldap_ru
Summary: Rutgers LDAP Plugins for Nagios
Group: Networking/Other
Requires: nagios-plugins nagios-plugins-perl python-ldap

%description -n nagios_plugins_ldap_ru
Provides LDAP plugins for Nagios which are home-grown at Rutgers.
They require entries in sudoers, for instance. Be careful.

%prep
%setup 

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers/etc
install -m 0755 check_ldap_clearbind $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 check_ldap_reader $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 check_ldap_sync $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 check_clamav $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 check_file_contents $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 check_imap_auth $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers/
install -m 0755 check_ldap_namingcontexts $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers/
install -m 0755 check_ldap_readeverything $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 kerbtest.sh $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 ldapSynchCheck.py $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers
install -m 0755 check_by_http $RPM_BUILD_ROOT/usr/local/nagios/libexec/rutgers

#WARNING: check_by_http is compiled separately in the nagios-plugins rpm but is 
#packaged separately here. In the future, this will be built here when 
#check_by_http has been rewritten so that it does not need to be built against 
#nagios-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc
%defattr(-,nagios,nagios)
/usr/local/nagios/libexec/rutgers/check_by_http
/usr/local/nagios/libexec/rutgers/check_clamav
/usr/local/nagios/libexec/rutgers/check_file_contents
/usr/local/nagios/libexec/rutgers/check_imap_auth
/usr/local/nagios/libexec/rutgers/kerbtest.sh
%dir /usr/local/nagios/libexec/rutgers/
%dir /usr/local/nagios/libexec/rutgers/etc

%files -n nagios_plugins_ldap_ru
%defattr(-,nagios,nagios)
/usr/local/nagios/libexec/rutgers/check_ldap_clearbind
/usr/local/nagios/libexec/rutgers/check_ldap_namingcontexts
/usr/local/nagios/libexec/rutgers/check_ldap_reader
/usr/local/nagios/libexec/rutgers/check_ldap_readeverything
/usr/local/nagios/libexec/rutgers/check_ldap_sync
/usr/local/nagios/libexec/rutgers/ldapSynchCheck.py

%changelog
* Thu Apr 16 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-6
- removed nagios-plugins-smtp from Requires
* Tue Apr 14 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-5
- broke out the ldap plugins into their own nagios_plugins_ldap_ru subpackage
* Mon Apr 13 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-4
- added updated verson of ldapSynchCheck.py
- added updated version of check_ldap_sync
- added etc directory to match linux package
* Fri Apr 3 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-3
- changed path to /usr/local/nagios/libexec/nagios
* Thu Apr 2 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-2
- update to check_file_contents script
* Tue Mar 31 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-1
- rewrote CentOS spec file for Solaris
* Wed Mar 25 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-14
- fixed output file problems in check_ipmi
* Wed Mar 25 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-13
- updated check_file_contents
- added alarm to check_ipmi to fix timeout issues
- added check_by_http (netdb)
* Wed Mar 18 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-12
- changed lib path back to absolute path
- added ifarch to spec to use correct lib path in scripts
- update to check_ipmi to handle no output from ipmitool
* Wed Mar 18 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-11
- changed lib path to relative path for perl scripts 
- fixes to check_ipmi
* Wed Mar 11 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.8.6-10
- Removed requires for nagios-plugins-mysql and nagios-plugins-radius
* Wed Feb 25 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-9
- updated to check_clamav-2.0.7 
- updates to check_file_contents
* Mon Feb 16 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.8.6-7
- Added config directory, new required new check_ipmi, tftp, xenvm, 
- removed check_ipmi_chassis ipmi_noshutdown ipmi_shutdown.
* Tue Jan 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.8.6-6
- Added, check_ipmi symlink. 
* Wed Jan 14 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.8.6-3
- Added, removed and updated scripts.
* Tue Nov 18 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.6-2
- updates to check_backups script, bumped release number
* Wed Oct 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.8.6-1
- Added check_backups script, bumped version to 0.8.6
* Mon Sep 15 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.5-3
- update to check_clamav script (added PATH variable)
* Thu Aug 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.5-2
- added ifarch so that path is correct in i386
* Wed Aug 20 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.5-1
- changed to UNKNOWN when check_clamav times out
* Tue Jul 1 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.4-1
- fixed argument handling in check_clamav script, bumped to 0.8.4
* Tue Jun 24 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.3-1
- made changes to check_clamav script, bumped version to 0.8.3
* Fri Jun 06 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.8.2-1
- added check_clamav script, bumped version number to 0.8.2 
