%define name 	netsaint
%define version 0.0.7
%define release 1 
%define prefix /usr/local

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
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
./configure


make all

%install

mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/etc
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/var/rw
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/var/archives
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/images/logos
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/developer/images
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/docs/othersw
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/images/logos
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/stylesheets 
mkdir -p $RPM_BUILD_ROOT%{prefix}/netsaint/share/media 

install -m 750 daemon-init $RPM_BUILD_ROOT/etc/init.d/netsaint 
install -m 644 nscgi.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc
install -m 644 resource.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc
install -m 644 netsaint.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc
install -m 644 hosts.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc
install -m 644 commands.cfg $RPM_BUILD_ROOT%{prefix}/netsaint/etc
install -m 755 base/netsaint $RPM_BUILD_ROOT%{prefix}/netsaint/bin
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
echo 'Readme is at /skipper/minnow/netsaint/NEWSETUP '
echo 'Still need to install netsaint-plugins*.rpm! '
echo 'Still need to install nsca*.rpm! '
echo 'ENJOY '

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
%doc Changelog INSTALL LICENSE README UPGRADING
%dir %{prefix}/netsaint
%{prefix}/netsaint/bin
%config(noreplace)%attr(-,netsaint,netsaint)%{prefix}/netsaint/etc
%dir %{prefix}/netsaint/sbin
%attr(4755,netsaint,netsaint)%{prefix}/netsaint/sbin/*
%{prefix}/netsaint/share
%dir %attr(775,netsaint,nscmd)%{prefix}/netsaint/var
%attr(2775,netsaint,nscmd)%{prefix}/netsaint/var/rw
%attr(2775,netsaint,nscmd)%{prefix}/netsaint/var/archives
%config(noreplace)%attr(-,root,root)/etc/init.d/*
