%define name syslog-ng
%define version 1.4.12
%define release 0
%define prefix /usr/local

Summary: syslog-ng daemon.

Name: %{name}
Version: %{version}
Release: %{release}
Group: System Environment/Daemons
Copyright: GPL
Url: http://www.balabit.hu/products/syslog-ng/
Source0: http://www.balabit.hu/downloads/syslog-ng/1.4/syslog-ng-%{version}.tar.gz
BuildRoot: /tmp/free/%{name}-root
Requires: libol >= 0.2.23

%description
An enhanced syslog daemon.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" 
./configure --prefix=%{prefix}
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}
mkdir -p $RPM_BUILD_ROOT%{prefix}/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man5
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man8

install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/src/syslog-ng $RPM_BUILD_ROOT%{prefix}/sbin
install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/doc/syslog-ng.8 $RPM_BUILD_ROOT%{prefix}/man/man8 
install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/doc/syslog-ng.conf.5 $RPM_BUILD_ROOT%{prefix}/man/man5 

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog INSTALL NEWS
%doc doc
%attr(755,root,root) %{prefix}/sbin/syslog-ng
%{prefix}/man

%clean
rm -r $RPM_BUILD_ROOT
