Summary: Migration scripts for LDAP
Name:      MigrationTools
Version:   44
Release:   2ru
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

%files
%defattr(-, root, bin)
/usr/local/%{name}

%doc README




