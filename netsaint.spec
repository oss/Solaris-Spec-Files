%define name netsaint
%define version 0.0.7
%define release 1
%define nsusr netsaint
%define nsgrp netsaint
%define cmdusr netsaint
%define cmdgrp nscmd

Summary: Host/service/network monitoring program
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Application/System
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: gd-devel > 1.8

%description
NetSaint is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. NetSaint is written in C and is
designed to run under Linux (and some other *NIX variants) as a
background process, intermittently running checks on various services
that you specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to NetSaint. The plugins are
available at http://sourceforge.net/projects/netsaintplug

This package provide core programs for netsaint. 

%package www
Group: Application/System
Summary: Provides the HTML and CGI files for the Netsaint web interface.

%description www
NetSaint is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. NetSaint is written in C and is
designed to run under Linux (and some other *NIX variants) as a
background process, intermittently running checks on various services
that you specify.

Several CGI programs are included with NetSaint in order to allow you
to view the current service status, problem history, notification
history, and log file via the web. This package provides the HTML and
CGI files for the Netsaint web interface. In addition, HTML
documentation is included in this package.

%prep
%setup -q

%build
./configure --prefix=/usr/local/netsaint \
--with-netsaint-user=netsaint --with-netsaint-grp=netsaint \
--with-gd-lib=/usr/local/lib --disable-statuswrl \
--with-command-user=netsaint --with-command-grp=nscmd
make all

%install
install -d -m 0775 ${RPM_BUILD_ROOT}/var/spool/netsaint
install -d -m 0755 ${RPM_BUILD_ROOT}/etc/init.d
make fullinstall DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS=""
make install-config DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS="" COMMAND_OPTS="" INIT_OPTS=""
mv $RPM_BUILD_ROOT/usr/local/%{name}/etc/netsaint.cfg $RPM_BUILD_ROOT/usr/local/%{name}/etc/netsaint.cfg.rpm
mv $RPM_BUILD_ROOT/usr/local/%{name}/etc/hosts.cfg $RPM_BUILD_ROOT/usr/local/%{name}/etc/hosts.cfg.rpm
mv $RPM_BUILD_ROOT/usr/local/%{name}/etc/commands.cfg $RPM_BUILD_ROOT/usr/local/%{name}/etc/commands.cfg.rpm
mv $RPM_BUILD_ROOT/usr/local/%{name}/etc/nscgi.cfg $RPM_BUILD_ROOT/usr/local/%{name}/etc/nscgi.cfg.rpm
mv $RPM_BUILD_ROOT/usr/local/%{name}/etc/resource.cfg $RPM_BUILD_ROOT/usr/local/%{name}/etc/resource.cfg.rpm
mv $RPM_BUILD_ROOT/etc/init.d/netsaint $RPM_BUILD_ROOT/etc/init.d/netsaint.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,netsaint,netsaint)
/usr/local/%{name}/bin/*
/usr/local/%{name}/etc/*

%defattr(-,%{nsusr},%{cmdgrp})
/usr/local/%{name}/var/*
/var/spool/*

%defattr(-,root,root)
/etc/init.d/*

%files www
%defattr(-,netsaint,netsaint)
/usr/local/%{name}/sbin/*
/usr/local/%{name}/share/*
