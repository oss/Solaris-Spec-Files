%define name 	nagios
%define version 2.0b5
%define release 3
%define prefix /usr/local

Summary:	Host/service/network monitoring program
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.gz
#Patch0:	nagiosnew.patch
URL:		http://www.nagios.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
#BuildRequires: 	gd-devel > 1.8

%description
Nagios is a program that will monitor hosts and 
services on your network.

It has the ability to email or page you when a problem
arises and when a problem is resolved.
Nagios is written in C and is designed to run under 
Linux (and some other *NIX variants) as a background process,
intermittently running checks on various services that 
you specify. The actual service checks are performed by
separate "plugin" programs which return the status of the 
checks to Nagios. Several CGI programs are included with 
Nagios in order to allow you to view the current 
service status, problem history, notification history, 
and log file via the web. 


%prep
%setup -q
%setup -n %{name}-%{version}
#%patch0 -p1

%build
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
export LD_RUN_PATH
./configure --prefix=%{prefix}/%{name} --with-command-group=nagiocmd \
            --with-cgiurl=/%{name}/cgi-bin --with-htmurl=/%{name} \
            --with-mail=/usr/bin/mailx --with-gd-lib=/usr/sfw/lib \
	    --with-gd-inc=/usr/sfw/include

make all 

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install
make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-init
make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-config
make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-commandmode

install -d -m 0755 ${RPM_BUILD_ROOT}%{prefix}/nagios/sbin/eventhandlers
install -d -m 0755 ${RPM_BUILD_ROOT}/etc/init.d

install -m 0750 contrib/eventhandlers/submit_check_result $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/submit_check_result-sample
install -m 0750 contrib/eventhandlers/disable_active_service_checks $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/disable_active_service_checks-sample
install -m 0750 contrib/eventhandlers/disable_notifications $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/disable_notifications-sample
install -m 0750 contrib/eventhandlers/enable_notifications $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/enable_notifications-sample
install -m 0750 contrib/eventhandlers/enable_active_service_checks $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/enable_active_service_checks-sample
install -m 0750 contrib/eventhandlers/distributed-monitoring/obsessive_svc_handler $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/obsessive_svc_handler-sample
install -m 0750 contrib/eventhandlers/distributed-monitoring/submit_check_result_via_nsca $RPM_BUILD_ROOT%{prefix}/nagios/sbin/eventhandlers/submit_check_result_via_nsca-sample
#install -m 0750 roy.init $RPM_BUILD_ROOT/etc/init.d/nagios

touch $RPM_BUILD_ROOT%{prefix}/nagios/var/nagios.log

%post
echo "All files and binaries installed in %{prefix}/nagios"
echo "ENJOY!!"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,nagios,nagios)
%dir %{prefix}/nagios
%dir %{prefix}/nagios/bin
%dir %{prefix}/nagios/sbin
%dir %{prefix}/nagios/sbin/eventhandlers
%dir %{prefix}/nagios/etc
%dir %{prefix}/nagios/share
%dir %{prefix}/nagios/var
%dir %attr(2770,nagios,nagiocmd)%{prefix}/nagios/var/rw
%dir %attr(0770,nagios,nagios)%{prefix}/nagios/var/archives

%defattr(-,nagios,nagios)
%doc Changelog LEGAL LICENSE README UPGRADING
%attr(0755,nagios,nagios)%{prefix}/nagios/bin/*
%config(noreplace)%attr(0644,nagios,nagios)%{prefix}/nagios/etc/*
%attr(0750,root,root)/etc/init.d/*
%attr(4755,nagios,nagios)%{prefix}/nagios/sbin/*.cgi
%attr(0750,nagios,nagios)%{prefix}/nagios/sbin/eventhandlers/*
%{prefix}/nagios/share/
%attr(0644,nagios,nagios)%{prefix}/nagios/var/nagios.log

%changelog
* Fri Nov 18 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0b5-3
- Updated to 2.0b5
* Thu Sep 22 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0b4-1
- New version
