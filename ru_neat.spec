%define name ru_neat
%define version 4.9 
%define release 1 
%define prefix /usr/local 

Summary: NetSaint Easy Administration Tool (NEAT) is a web administration interface for NetSaint
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: ru_netsaint, netsaint-plugins 

%description

NetSaint is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. NetSaint runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to NetSaint.

NetSaint Easy Administration Tool (NEAT) is a web administration 
interface for NetSaint that is written in Perl. It allows you to 
add/edit/delete definitions in your host configuration file and 
restart NetSaint upon completion of the configuration changes. 


%prep
%setup 

%build

%install

mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/sbin
mkdir -p ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/ORIG

install -m 755 RU/neat.cgi.brylon ${RPM_BUILD_ROOT}%{prefix}/netsaint/sbin/neat.cgi
install -m 644 RU/neat4.options ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/neat4.options.rpm
install -m 644 RU/entity_defs ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/entity_defs.rpm
install -m 644 RU/deletion_rules ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/deletion_rules.rpm
install -m 644 ver_tags ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/ver_tags.rpm

install -m 755 neat.cgi ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/ORIG/neat.cgi
install -m 644 neat4.options ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/ORIG/neat4.options.rpm

install -m 644 0.7_entity_defs ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/ORIG/entity_defs.rpm
install -m 644 deletion_rules ${RPM_BUILD_ROOT}%{prefix}/netsaint/neat-4.9/ORIG/deletion_rules.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%doc README.txt  
%{prefix}/netsaint/neat-4.9
%attr(4755,netsaint,netsaint)%{prefix}/netsaint/sbin/neat.cgi
