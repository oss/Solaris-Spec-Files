Summary: Migration scripts for LDAP
Name:      MigrationTools
Version:   44
Release:   3ru
Source:    ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
Source1:   migrate-ex.tar.gz
URL:       http://www.padl.com/
Copyright: BSD
Group: Networking/Utilities
BuildRoot: %{_tmppath}/rpm-%{name}-root
Prefix: /usr/local
#Requires: openldap?
Requires: perl 

%description
The MigrationTools are a set of Perl scripts for migrating users, groups,
aliases, hosts, netgroups, networks, protocols, RPCs, and services from 
existing nameservices (flat files, NIS, and NetInfo) to LDAP. 

%prep
%setup 
%setup -T -D -b 1 
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/%{name}

%setup


%build

%install
mv ../migrate* ./ # blame ebede for making tar that explodes in cwd
cp -a migrate_* $RPM_BUILD_ROOT/usr/local/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo You may want to modify the config files migrate_common.ph and 
echo migrate_all_online.sh in /usr/local/MigrationTools.  Example files
echo exist in the same directory.

%files
%defattr(-, root, bin)
/usr/local/%{name}
%config(noreplace) /usr/local/%{name}/migrate_common.ph
%config(noreplace) /usr/local/%{name}/migrate_all_online.sh

%doc README




