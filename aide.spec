%define name aide
%define version 0.7
%define release 1
%define prefix /usr/local

Summary: Advanced Intrusion Detection Environment
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Console/Security
Source0: http://www.cs.tut.fi/~rammer/%{name}-%{version}.tar.gz
BuildRoot: /tmp/free/%{name}-root

%description
aide is an intrusion detection system for checking the integrity of files.

%prep
%setup

%build
./configure --prefix=%{prefix} --sysconfdir=/etc --with-config-file=/etc/aide.conf

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install-strip
mkdir -p -m 700 $RPM_BUILD_ROOT/var/lib/aide
mkdir -p $RPM_BUILD_ROOT/etc

install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/aide.conf.example $RPM_BUILD_ROOT/etc

%post 

echo aide.conf.example must be changed to aide.conf in the /etc directory

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README doc/aide*
%{prefix}/bin/aide
%{prefix}/man/man1/aide.1
%{prefix}/man/man5/aide.conf.5
/var/lib/aide
/etc/aide.conf.example
