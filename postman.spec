%define name ru_postman
%define version 1.12
%define release 3 
%define prefix /usr/local

Summary: Postman is a C++ Web Mail client.
Name: %name
Version: %version
Release: %release
Copyright: University of Valencia
Group: Mail/Client
Source0: ru_postman1.12.tar.gz
BuildRoot: /var/local/tmp/%{name}-root


%description
Postman is a web client for imap, designed and programmed in the Service of Computer science of the University of Valencia.


%prep
%setup -n ru_postman1.12 

%build
make CCLIENTDIR=/stooges/u1/brylon/rpm_postman/imap-2001a_SSL/c-client
#make CCLIENTDIR=/export/home/brylon/c-client

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{prefix}/apache/cgi-bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/postman
mkdir -p $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman
mkdir -p $RPM_BUILD_ROOT%{prefix}/etc

make SRC=$RPM_BUILD_DIR/%{name}%{version} PREFIX=$RPM_BUILD_ROOT%{prefix} POSTMANDIR=$RPM_BUILD_ROOT%{prefix}/postman CGIUSER=brylon CGIGROUP=studsys WEBGROUP=studsys SERVERGROUP=studsys SERVERUSER=brylon POSTMANUSER=brylon install

mv $RPM_BUILD_ROOT%{prefix}/sbin/interdaemon.ini $RPM_BUILD_ROOT%{prefix}/sbin/interdaemon.ini.rpm
mv $RPM_BUILD_ROOT%{prefix}/sbin/interdaemon2.ini $RPM_BUILD_ROOT%{prefix}/sbin/interdaemon2.ini.rpm

mv $RPM_BUILD_ROOT%{prefix}/etc/interdaemon.cfg $RPM_BUILD_ROOT%{prefix}/etc/interdaemon.cfg.rpm
mv $RPM_BUILD_ROOT%{prefix}/etc/interdaemon2.cfg $RPM_BUILD_ROOT%{prefix}/etc/interdaemon2.cfg.rpm
mv $RPM_BUILD_ROOT%{prefix}/etc/postman.mailcap $RPM_BUILD_ROOT%{prefix}/etc/postman.mailcap.rpm

mv $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.spa $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.spa.rpm 

mv $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.val $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.val.rpm 

mv $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.eng $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.eng.rpm 
mv $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.eus $RPM_BUILD_ROOT%{prefix}/etc/postman.motd.eus.rpm 
mv $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_eng.html $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_eng.html.rpm

mv $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_val.html $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_val.html.rpm
mv $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_eus.html $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_eus.html.rpm

mv $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_spa.html $RPM_BUILD_ROOT%{prefix}/apache/htdocs/postman/postman_spa.html.rpm


%post 
echo 'Must have user account webmail and group www on webserver'
echo 'To start interdaemon type: /usr/local/sbin/interdaemon.ini start'
echo 'To change relevant .rpm extensions to the correct filenames YOU MUST change all the files containing "postman*.rpm" as well as all files containing "interdaemon*.rpm" in the following directories:'
echo '/usr/local/sbin, /usr/local/etc, /usr/local/apache/htdocs/postman'


%clean
rm -rf $RPM_BUILD_ROOT
 

%files
%defattr(-, root, www)

%{prefix}/apache/cgi-bin/postman

%attr(750,webmail,www)%{prefix}/postman/server
%attr(750,webmail,www)%{prefix}/postman/sessions
%attr(750,webmail,www)%{prefix}/postman/netnews
%attr(700,webmail,www)%{prefix}/postman/locks
%attr(710,webmail,www)%{prefix}/postman/users
%attr(770,webmail,www)%{prefix}/postman/tmp

%attr(755,root,root)%{prefix}/sbin/interdaemon.ini.rpm
%attr(755,root,root)%{prefix}/sbin/interdaemon2.ini.rpm
%attr(755,root,www)%{prefix}/sbin/interdaemon

%attr(644,root,www)%{prefix}/etc/interdaemon.cfg.rpm
%attr(644,root,www)%{prefix}/etc/interdaemon2.cfg.rpm
%attr(644,root,www)%{prefix}/etc/postman.mailcap.rpm
%attr(644,root,www)%{prefix}/etc/postman.disabledx
%attr(644,root,www)%{prefix}/etc/postman.motd.spa.rpm
%attr(644,root,www)%{prefix}/etc/postman.motd.val.rpm
%attr(644,root,www)%{prefix}/etc/postman.motd.eng.rpm
%attr(644,root,www)%{prefix}/etc/postman.motd.eus.rpm

%{prefix}/apache/htdocs/postman/help/*
%{prefix}/apache/htdocs/postman/icons/*
%{prefix}/apache/htdocs/postman/disabled.html
%{prefix}/apache/htdocs/postman/postman_eng.html.rpm
%{prefix}/apache/htdocs/postman/postman_val.html.rpm
%{prefix}/apache/htdocs/postman/postman_spa.html.rpm
%{prefix}/apache/htdocs/postman/postman_eus.html.rpm



