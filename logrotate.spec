Summary: Shell script to rotate system log files to a log area
Name: logrotate
Version: 1.2
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: logrotate-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Logrotate is usually run from cron.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,other) /usr/local/sbin/*
