%define name 	nagios
%define version 2.0
%define release 2
%define prefix  /usr/local
%define nagpath %{prefix}/%{name}-%{version}

Summary:	Host/service/network monitoring program
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.nagios.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root

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

%build
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
export LD_RUN_PATH
./configure --prefix=%{nagpath} --with-command-group=nagiocmd \
            --with-cgiurl=/%{name}/cgi-bin --with-htmurl=/%{name} \
            --with-mail=/usr/bin/mailx --with-gd-lib=/usr/sfw/lib \
	    --with-gd-inc=/usr/sfw/include
make all 

%install
make DESTDIR=%{buildroot} INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install
make DESTDIR=%{buildroot} INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-init
make DESTDIR=%{buildroot} INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-config
make DESTDIR=%{buildroot} INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-commandmode

/usr/local/gnu/bin/install -d -m 0755 %{buildroot}%{nagpath}/sbin/eventhandlers
/usr/local/gnu/bin/install -d -m 0755 %{buildroot}/etc/init.d

# must use GNU install
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/submit_check_result \
    %{buildroot}%{nagpath}/sbin/eventhandlers/submit_check_result-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/disable_active_service_checks \
    %{buildroot}%{nagpath}/sbin/eventhandlers/disable_active_service_checks-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/disable_notifications \
    %{buildroot}%{nagpath}/sbin/eventhandlers/disable_notifications-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/enable_notifications \
    %{buildroot}%{nagpath}/sbin/eventhandlers/enable_notifications-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/enable_active_service_checks \
    %{buildroot}%{nagpath}/sbin/eventhandlers/enable_active_service_checks-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/distributed-monitoring/obsessive_svc_handler \
    %{buildroot}%{nagpath}/sbin/eventhandlers/obsessive_svc_handler-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/distributed-monitoring/submit_check_result_via_nsca \
    %{buildroot}%{nagpath}/sbin/eventhandlers/submit_check_result_via_nsca-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/redundancy-scenario1/handle-master-host-event \
    %{buildroot}%{nagpath}/sbin/eventhandlers/handle-master-host-event-sample
/usr/local/gnu/bin/install -m 0750 contrib/eventhandlers/redundancy-scenario1/handle-master-proc-event \
    %{buildroot}%{nagpath}/sbin/eventhandlers/handle-master-proc-event-sample

touch %{buildroot}%{nagpath}/var/nagios.log

%post
echo "All files and binaries installed in %{nagpath}"
echo "ENJOY!!"

%clean
rm -rf %{buildroot}

%files
%defattr(0755,nagios,nagios)
%dir %{nagpath}
%dir %{nagpath}/bin
%dir %{nagpath}/sbin
%dir %{nagpath}/sbin/eventhandlers
%dir %{nagpath}/etc
%dir %{nagpath}/share
%dir %{nagpath}/var
%dir %attr(2770,nagios,nagiocmd)%{nagpath}/var/rw
%dir %attr(0770,nagios,nagios)%{nagpath}/var/archives

%defattr(-,nagios,nagios)
%doc Changelog LEGAL LICENSE README UPGRADING
%attr(0755,nagios,nagios)%{nagpath}/bin/*
%config(noreplace)%attr(0644,nagios,nagios)%{nagpath}/etc/*
%attr(0750,root,root)/etc/init.d/*
%attr(4755,nagios,nagios)%{nagpath}/sbin/*.cgi
%attr(0750,nagios,nagios)%{nagpath}/sbin/eventhandlers/*
%{nagpath}/share/
%attr(0644,nagios,nagios)%{nagpath}/var/nagios.log

%changelog
* Tue Feb 14 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 2.0-2
- Changed the nagios directory from /usr/local/nagios to /usr/local/nagios-2.0
* Thu Feb 09 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 2.0-1
- Updated to the 2.0 release (out of beta)
* Fri Nov 18 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0b5-3
- Updated to 2.0b5
* Thu Sep 22 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0b4-1
- New version
