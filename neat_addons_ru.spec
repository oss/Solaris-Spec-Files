%define name 	neat_addons_ru
%define version 0.1
%define release 4
%define prefix /usr/local

Summary:	Neat program addons
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.nagios.org
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	nagios, nagios-plugins, nsca, neat

%description
Neat is an administration tool for Nagios

The addons package is for allowing other dept's the ability to view only their
configuration data and make changes as they seem fit. 

%prep

%setup 

%build

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/sbin-neat
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/dept
mkdir -p $RPM_BUILD_ROOT%{prefix}/nagios/share-neat

install -m 4755 neat.cgi $RPM_BUILD_ROOT%{prefix}/nagios/sbin-neat/neat.cgi.new
install -m 0755 neat-wget-global-cfg.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 neat-wget-local-cfg.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0755 AS.sh $RPM_BUILD_ROOT%{prefix}/nagios/bin
install -m 0644 index.php $RPM_BUILD_ROOT%{prefix}/nagios/share-neat
install -m 0644 cfg.php $RPM_BUILD_ROOT%{prefix}/nagios/share-neat

%post
mv %{prefix}/nagios/sbin-neat/neat.cgi %{prefix}/nagios/sbin-neat/neat.cgi.orig
mv %{prefix}/nagios/sbin-neat/neat.cgi.new %{prefix}/nagios/sbin-neat/neat.cgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%dir %{prefix}/nagios/dept
%dir %{prefix}/nagios/share-neat

%defattr(-,nagios,nagios)
%{prefix}/nagios/dept
%{prefix}/nagios/bin/*
%{prefix}/nagios/sbin-neat/*
%{prefix}/nagios/share-neat/index.php
%config(noreplace)%{prefix}/nagios/share-neat/cfg.php
