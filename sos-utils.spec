Summary: Commonly used Rutgers utilities
Name: sos-utils
Version: 1.0
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: sos-utils-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
The sos-utils are fix.hme, hme-status, and netcheck.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0700,root,other) /usr/local/sbin/*
