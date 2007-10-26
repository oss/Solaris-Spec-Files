%define name webtools_become
%define version 0.1
%define release 5
%define prefix /usr/local
%define become_tardir become
Summary: Web application allowing users to request become accounts
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Packager: Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu>
Source0: %{name}-%{version}.tar 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4 pear-DB pear-HTML
#Patch0: iid-check.patch

%description
This is an addon package to webtools. It allows users request a become
account on a particular cluster of their choosing (rci, eden, nbcs). The
following steps are needed to setup this package with webtools.

%prep
%setup -n %{become_tardir}


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin

install -c -m 0555 $RPM_BUILD_DIR/%{become_tardir}/yplookup $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0644 $RPM_BUILD_DIR/%{become_tardir}/*.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/

%post
cat << EOF
The README is located in /usr/local/doc/webtools_become/.
There are install instructions there.
READ IT!!!

EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%doc README
%{prefix}/%{name}-%{version}/html/*
%attr(- ,root, www)%{prefix}/%{name}-%{version}/webbin/*

%changelog
* Fri Sep 28 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 0.1-5
- Chnages directory name and file permissions
* Fri Sep 28 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 0.1-4
- Corrected patch to check to see if input looks like an IID
* Fri Jul 27 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 0.1-3
- Added patch to check to see if input looks like an IID
* Mon Jul 09 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.1-2
- Fixed user privileges bug
