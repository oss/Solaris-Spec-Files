%define name 	ru_netsaint
%define version 0.0.7
%define release 1 
%define prefix /usr/local

%define nsusr 	netsaint
%define nsgrp 	netsaint
%define cmdusr 	nscmd
%define cmdgrp 	nscmd

Summary:	Host/service/network monitoring program
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.netsaint.org
BuildRoot: 	%{_tmppath}/%{name}-root
#BuildRequires: 	libgd1-devel

%description
NetSaint is a program that will monitor hosts and 
services on your network.

It has the ability to email or page you when a problem
arises and when a problem is resolved.
NetSaint is written in C and is designed to run under 
Linux (and some other *NIX variants) as a background process,
intermittently running checks on various services that 
you specify. The actual service checks are performed by
separate "plugin" programs which return the status of the 
checks to NetSaint. Several CGI programs are included with 
NetSaint in order to allow you to view the current 
service status, problem history, notification history, 
and log file via the web. 

%prep

%setup 

%build
./configure \
	--with-cgiurl=/cgi-bin/netsaint \
	--with-htmurl=/netsaint \
	--prefix=%{prefix}/netsaint \
	--bindir=%{prefix}/netsaint/bin \
	--sbindir=%{prefix}/netsaint/sbin \
	--libexecdir=%{prefix}/netsaint/libexec \
	--datadir=%{prefix}/netsaint/share \
	--sysconfdir=%{prefix}/netsaint/etc \
	--localstatedir=%{prefix}/netsaint/var \
	--with-command-user=%{cmdusr} \
	--with-command-grp=%{cmdgrp} \
	--with-lockfile=%{prefix}/netsaint/var/netsaint.lock \
	--with-ping-command=/usr/sbin/ping \
	--with-netsaint-user=%{nsusr} \
	--with-netsaint-grp=%{nsgrp} \
	--with-init-dir=/etc/init.d \
	--with-gd-inc=/usr/local/include \
	--with-gd-lib=/usr/local/lib

make all

%install

mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/etc
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/var
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open 
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/images/logos
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/developer/images
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/othersw
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/images/logos
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/stylesheets 
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/media 

install -m 444 netsaint.SETUP $RPM_BUILD_ROOT%{prefix}/netsaint/NETSAINT.SETUP
install -m 750 daemon-init $RPM_BUILD_ROOT/etc/init.d/netsaint.rpm 
install -m 755 base/netsaint $RPM_BUILD_ROOT%{prefix}/netsaint/bin
install -m 644 netsaint.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/netsaint.cfg.rpm
install -m 644 nscgi.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/nscgi.cfg.rpm
install -m 644 hosts.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/hosts.cfg.rpm
install -m 644 resource.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/resource.cfg.rpm
install -m 644 test.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/test.cfg.rpm
install -m 644 commands.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/commands.cfg.rpm
install -m 755 cgi/*.cgi $RPM_BUILD_ROOT%{prefix}/netsaint/sbin
install -m 755 contrib/*.cgi $RPM_BUILD_ROOT%{prefix}/netsaint/sbin
install -m 644 html/*.html $RPM_BUILD_ROOT%{prefix}/netsaint/share
install -m 644 html/docs/*.html	$RPM_BUILD_ROOT%{prefix}/netsaint/share/docs
install -m 644 html/docs/*.txt $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs
install -m 644 html/docs/developer/*.html $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/developer
install -m 644 html/docs/developer/images/* $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/developer/images
install -m 644 html/docs/images/* $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/images
install -m 644 html/docs/othersw/* $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/othersw
install -m 644 html/images/*.gif $RPM_BUILD_ROOT%{prefix}/netsaint/share/images
install -m 644 html/images/*.png $RPM_BUILD_ROOT%{prefix}/netsaint/share/images
install -m 644 html/images/logos/* $RPM_BUILD_ROOT%{prefix}/netsaint/share/images/logos
install -m 644 html/media/* $RPM_BUILD_ROOT%{prefix}/netsaint/share/media
install -m 644 html/stylesheets/* $RPM_BUILD_ROOT%{prefix}/netsaint/share/stylesheets
install -m 644  html/images/*.jpg $RPM_BUILD_ROOT%{prefix}/netsaint/share/images

touch rw archives

install -m 755 rw				$RPM_BUILD_ROOT%{prefix}/netsaint/var
install -m 755 archives				$RPM_BUILD_ROOT%{prefix}/netsaint/var

%post
echo 'All files and binaries installed in /usr/local/netsaint '
echo 'Readme is at /usr/local/netsaint/NETSAINT.SETUP '
echo 'Still need to install netsaint-plugins rpm! '
echo 'ENJOY '

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%doc Changelog INSTALL LICENSE README UPGRADING

#%config(noreplace) %{prefix}/netsaint/etc/*.cfg
%{prefix}/netsaint/NETSAINT.SETUP
%{prefix}/netsaint/bin
%{prefix}/netsaint/etc
%attr(-,www,other)%{prefix}/netsaint/sbin
%{prefix}/netsaint/share
%{prefix}/netsaint/var
%{prefix}/netsaint/etc_open
%attr(-,root,root)/etc/init.d/*
