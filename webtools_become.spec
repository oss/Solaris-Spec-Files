%define name webtools_become
%define version 0.1
%define release 2
%define prefix /usr/local
%define become_tardir become

Summary: Web application allowing users to request become accounts
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source0: %{name}-%{version}.tar 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4 pear-DB pear-HTML

%description
This is an addon package to webtools. It allows users request a become
account on a particular cluster of their choosing (rci, eden, nbcs). The
following steps are needed to setup this package with webtools.

%prep
%setup -n %{become_tardir}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}/html
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}/webbin

install -c -m 0555 $RPM_BUILD_DIR/%{become_tardir}/yplookup $RPM_BUILD_ROOT%{prefix}/%{name}/webbin/

install -c -m 0644 $RPM_BUILD_DIR/%{become_tardir}/*.php $RPM_BUILD_ROOT%{prefix}/%{name}/html/

%post
cat << EOF
The README is located in /usr/local/doc/webtools_become/.
There are install instructions there.
READ IT!!!

EOF

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, www, www)
%doc README
%{prefix}/%{name}/html/*
%attr(- ,root, www)%{prefix}/%{name}/webbin/*

%changelog
* Mon Jul 09 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.1-2
- Fixed user privileges bug
