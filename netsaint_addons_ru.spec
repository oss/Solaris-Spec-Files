%define name 	netsaint_addons_ru
%define version 0.1
%define release 1 
%define prefix /usr/local

Summary:	Host/service/network monitoring program addons
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.netsaint.org
BuildRoot: 	%{_tmppath}/%{name}-root
#BuildRequires: 	libgd1-devel
Requires:	netsaint, netsaint-plugins, nsca

%description
NetSaint is a program that will monitor hosts and 
services on your network.

Addons, such as allowing clients/servants to download changed
cfg files from a master and "massage" those changed cfg files 
being downloaded.

%prep

%setup 

%build

%install

mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/bin

install -m 755 * $RPM_BUILD_ROOT%{prefix}/netsaint/bin

%post
echo 'Installed fix-cfg.pl and retrieve.sh in /usr/local/netsaint/bin'
echo 'A cron job should be created & run retrieve.sh and fix-cfg.pl as desired' 
echo 'Readme is at /skipper/minnow/netsaint/NEWSETUP '

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%{prefix}/netsaint/bin
