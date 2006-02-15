%define name     nsca
%define version  2.5
%define release  2
%define prefix   /usr/local 
%define nscapath %{prefix}/%{name}

Summary: Daemon and client program for sending passive check results across the network 
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/System
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: nagios, nagios-plugins

%description

Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This addon allows you to send passive service check results from
remote hosts to a central monitoring host that runs Nagios. The client
can be used as a standalone program or can be integrated with remote
Nagios servers that run an ocsp command to setup a distributed
monitoring environment.


%prep
%setup 

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export LDFLAGS
./configure --prefix=%{nscapath}
make all

%install
PATH="/usr/local/gnu/bin:/usr/local/bin:$PATH"
export PATH

mkdir -p %{buildroot}%{nscapath}/etc
mkdir -p %{buildroot}%{nscapath}/bin
mkdir -p %{buildroot}/etc/init.d

install -m 0644 sample-config/nsca.cfg %{buildroot}%{nscapath}/etc/nsca.cfg-example
install -m 0644 sample-config/send_nsca.cfg %{buildroot}%{nscapath}/etc/send_nsca.cfg-example
install -m 0644 sample-config/nsca.xinetd %{buildroot}%{nscapath}/etc/nsca.xinetd-example
install -m 0755 src/nsca %{buildroot}%{nscapath}/bin
install -m 0755 src/send_nsca %{buildroot}%{nscapath}/bin
install -m 0755 init-script %{buildroot}/etc/init.d/nsca

%clean
rm -rf %{buildroot}

%files
%defattr(-,nagios,nagios)
%doc Changelog SECURITY README LEGAL
%config(noreplace)%{nscapath}/etc/*
%{nscapath}/bin/*
%config(noreplace)%attr(-,root,root)/etc/init.d/*

%changelog
* Wed Feb 15 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 2.5-2
- Changed the install directory from /usr/local/nagios to /usr/local/nsca
