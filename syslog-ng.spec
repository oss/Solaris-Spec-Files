%define name syslog-ng
%define version 1.6.0rc3
%define release 4
%define prefix /usr/local

Summary: syslog-ng daemon.

Name: %{name}
Version: %{version}
Release: %{release}
Group: System Environment/Daemons
Copyright: GPL
Url: http://www.balabit.hu/products/syslog-ng/
Source0: http://www.balabit.hu/downloads/syslog-ng/1.6/src/syslog-ng-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: libol >= 0.3.10
BuildRequires: libol-devel >= 0.3.10

%description
An enhanced syslog daemon.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" 
./configure --prefix=%{prefix} --enable-sun-door
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
%{prefix}/man
%attr(755,root,root) %{prefix}/sbin/syslog-ng

%clean
rm -r $RPM_BUILD_ROOT
