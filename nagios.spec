%define name 	nagios
%define aversion 1.0
%define release 9ru 
%define prefix /usr/local

Summary:	Host/service/network monitoring program
Name:		%{name}
Version:	%{aversion}
Release:	%{release}
License:	GPL
Group:		Networking/Other
Source0:	%{name}-%{aversion}.tar.gz
Patch0:		nagios.patch
URL:		http://www.nagios.org
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:       libpng3 libjpeg62
BuildRequires: 	gd-devel > 1.8

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
%setup -n nagios-1.0
%patch0 -p1

%build
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
export LD_RUN_PATH
./configure --prefix=%{prefix}/%{name} \
--with-default-objects --with-gd-lib=/usr/local/lib \
--with-gd-inc=/usr/local/include
make all 

%install
#LOGDIR=DESTDIR/var
#CFGDIR=DESTDIR/etc
#BINDIR=DESTDIR/bin
#CGIDIR=DESTDIR/sbin
#HTMLDIR=DESTDIR/share
#INIT_DIR=/etc/init.d
#CGICFGDIR=CGIDIR

make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install
make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-config
make DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS="" install-commandmode

install -d -m 0755 ${RPM_BUILD_ROOT}%{prefix}/%{name}/sbin/eventhandlers
install -d -m 0755 ${RPM_BUILD_ROOT}/etc/init.d

install -m 0750 contrib/eventhandlers/submit_check_result $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/submit_check_result-sample
install -m 0750 contrib/eventhandlers/disable_active_service_checks $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/disable_active_service_checks-sample
install -m 0750 contrib/eventhandlers/disable_notifications $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/disable_notifications-sample
install -m 0750 contrib/eventhandlers/enable_notifications $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/enable_notifications-sample
install -m 0750 contrib/eventhandlers/enable_active_service_checks $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/enable_active_service_checks-sample
install -m 0750 contrib/eventhandlers/distributed-monitoring/obsessive_svc_handler $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/obsessive_svc_handler-sample
install -m 0750 contrib/eventhandlers/distributed-monitoring/submit_check_result_via_nsca $RPM_BUILD_ROOT%{prefix}/%{name}/sbin/eventhandlers/submit_check_result_via_nsca-sample
install -m 0750 roy.init $RPM_BUILD_ROOT/etc/init.d/nagios

touch $RPM_BUILD_ROOT%{prefix}/nagios/var/nagios.log

%post
echo "All files and binaries installed in /usr/local/nagios"
echo "ENJOY!!"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,nagios,nagios)
%dir %{prefix}/%{name}
%dir %{prefix}/%{name}/bin
%dir %{prefix}/%{name}/sbin
%dir %{prefix}/%{name}/sbin/eventhandlers
%dir %{prefix}/%{name}/etc
%dir %{prefix}/%{name}/share
%dir %{prefix}/%{name}/var
%dir %attr(2770,nagios,nagiocmd)%{prefix}/%{name}/var/rw
%dir %attr(0770,nagios,nagios)%{prefix}/%{name}/var/archives

%defattr(-,nagios,nagios)
%doc Changelog LEGAL LICENSE README UPGRADING
%attr(0755,nagios,nagios)%{prefix}/%{name}/bin/*
%config(noreplace)%attr(0644,nagios,nagios)%{prefix}/%{name}/etc/*
%attr(0750,root,root)/etc/init.d/*
%attr(4755,nagios,nagios)%{prefix}/%{name}/sbin/*.cgi
%attr(0750,nagios,nagios)%{prefix}/%{name}/sbin/eventhandlers/*
%{prefix}/%{name}/share/
%attr(0644,nagios,nagios)%{prefix}/%{name}/var/nagios.log
