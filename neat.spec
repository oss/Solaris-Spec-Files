%define name neat
%define version 4.9 
%define release 14
%define prefix /usr/local 

Summary: Nagios Easy Administration Tool (NEAT) is a web administration interface for Nagios
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
Patch0: neat.patch
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios, nagios-plugins

%description

Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

Nagios Easy Administration Tool (NEAT) is a web administration 
interface for Nagios that is written in Perl. It allows you to 
add/edit/delete definitions in your host configuration file and 
restart Nagios upon completion of the configuration changes. 


%prep
%setup 

%patch0 -p1

%build

%install

mkdir -m 0755 -p ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}
mkdir -m 0755 -p ${RPM_BUILD_ROOT}%{prefix}/nagios/sbin-neat
mkdir -m 0755 -p ${RPM_BUILD_ROOT}%{prefix}/nagios/etc_open

install -m 4755 neat.cgi ${RPM_BUILD_ROOT}%{prefix}/nagios/sbin-neat
install -m 0644 ver_tags ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}
install -m 0644 neat4.options ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}/neat4.options-example
install -m 0644 neat4.options-ru ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}/neat4.options-ru-example
install -m 0644 entity_defs-ru ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}/entity_defs-ru-example
install -m 0644 0.7_entity_defs ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}
install -m 0644 deletion_rules ${RPM_BUILD_ROOT}%{prefix}/nagios/%{name}-%{version}

/usr/bin/touch $RPM_BUILD_ROOT%{prefix}/nagios/sbin-neat/cmd.cgi

%post
/usr/local/gnu/bin/rm /usr/local/nagios/sbin-neat/cmd.cgi
/usr/local/gnu/bin/ln -s /usr/local/nagios/sbin/cmd.cgi /usr/local/nagios/sbin-neat/cmd.cgi
/usr/local/gnu/bin/chown -h nagios:nagios /usr/local/nagios/sbin-neat/cmd.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,nagios,nagios)
%dir %{prefix}/nagios/%{name}-%{version}
%dir %{prefix}/nagios/sbin-neat
%dir %{prefix}/nagios/etc_open

%defattr(-,nagios,nagios)
%doc README.txt  
%config(noreplace)%{prefix}/nagios/%{name}-%{version}/*
%{prefix}/nagios/sbin-neat/neat.cgi
%{prefix}/nagios/sbin-neat/cmd.cgi
