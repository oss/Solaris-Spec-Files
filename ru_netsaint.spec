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
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/etc/ORIG
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/var/rw
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/var/archives
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open 
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/images/logos
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/developer/images
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/othersw
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/images/logos
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/stylesheets 
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/media 

install -m 444 RU/netsaint.SETUP $RPM_BUILD_ROOT%{prefix}/netsaint/NETSAINT.SETUP
install -m 644 RU/hosts.cfg.distributed $RPM_BUILD_ROOT%{prefix}/netsaint/etc/hosts.cfg.distributed.rpm
install -m 644 RU/hosts.cfg.masters $RPM_BUILD_ROOT%{prefix}/netsaint/etc/hosts.cfg.masters.rpm
install -m 644 RU/hosts.cfg.servants $RPM_BUILD_ROOT%{prefix}/netsaint/etc/hosts.cfg.servants.rpm
install -m 644 RU/hosts.cfg.clients $RPM_BUILD_ROOT%{prefix}/netsaint/etc/hosts.cfg.clients.rpm
install -m 644 RU/hosts.cfg.distributed $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open/hosts.cfg.distributed.rpm
install -m 644 RU/hosts.cfg.masters $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open/hosts.cfg.masters.rpm
install -m 644 RU/hosts.cfg.servants $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open/hosts.cfg.servants.rpm
install -m 644 RU/hosts.cfg.clients $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open/hosts.cfg.clients.rpm
install -m 644 RU/index.html $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open/index.html
install -m 644 RU/htaccess_wget $RPM_BUILD_ROOT%{prefix}/netsaint/etc_open/.htaccess
install -m 644 RU/htaccess_cgi $RPM_BUILD_ROOT%{prefix}/netsaint/sbin/.htaccess
install -m 644 RU/commands.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/commands.cfg.rpm
install -m 644 RU/netsaint.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/netsaint.cfg.rpm
install -m 644 RU/netsaint.cfg.tmp $RPM_BUILD_ROOT%{prefix}/netsaint/etc/netsaint.cfg.tmp.rpm
install -m 644 RU/remote-url.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/remote-url.cfg.rpm
install -m 755 RU/test.sh $RPM_BUILD_ROOT%{prefix}/netsaint/bin/test.sh
install -m 755 RU/kcron $RPM_BUILD_ROOT%{prefix}/netsaint/bin/kcron


install -m 750 daemon-init $RPM_BUILD_ROOT/etc/init.d/netsaint.rpm 
install -m 755 base/netsaint $RPM_BUILD_ROOT%{prefix}/netsaint/bin
install -m 644 netsaint.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/ORIG/netsaint.cfg.rpm
install -m 644 hosts.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/ORIG/hosts.cfg.rpm
install -m 644 commands.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/ORIG/commands.cfg.rpm
install -m 644 nscgi.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/nscgi.cfg.rpm
install -m 644 resource.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/resource.cfg.rpm
#install -m 644 test.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc/test.cfg.rpm
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

%post
echo 'All files and binaries installed in /usr/local/netsaint '
echo 'Readme is at /usr/local/netsaint/NETSAINT.SETUP '
echo 'Still need to install netsaint-plugins rpm! '
echo 'Still need to install ru_nsca rpm! '
echo 'ENJOY '

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%doc Changelog INSTALL LICENSE README UPGRADING

#%config(noreplace) %{prefix}/netsaint/etc/*.cfg
%{prefix}/netsaint/NETSAINT.SETUP
%{prefix}/netsaint/bin
%attr(-,netsaint,nscmd)%{prefix}/netsaint/etc

%dir %{prefix}/netsaint/sbin
%attr(-,root,other)%{prefix}/netsaint/sbin/.htaccess
%attr(4755,netsaint,netsaint)%{prefix}/netsaint/sbin/*

%{prefix}/netsaint/share

%dir %attr(775,netsaint,nscmd)%{prefix}/netsaint/var
%attr(2775,netsaint,nscmd)%{prefix}/netsaint/var/rw
%attr(2775,netsaint,nscmd)%{prefix}/netsaint/var/archives

%dir %attr(-,netsaint,netsaint)%{prefix}/netsaint/etc_open
%attr(-,root,other)%{prefix}/netsaint/etc_open/.htaccess
%{prefix}/netsaint/etc_open/*

%attr(-,root,root)/etc/init.d/*
