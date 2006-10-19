%define name webtools_whitelist
%define version 0.1
%define release 1
%define prefix /usr/local
%define tardir whitelist

Summary: Web application allowing users to whitelist IPs for SMTP
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4 pear-DB pear-HTML pear-Mail

%description
This is an addon package to webtools.  This tool is designed to allow
Responsible Persons (RPs) of record to request the authorization of
specific network-attached devices, such as printers and switches, on the
Rutgers IP space to be able to send email messages without first
authenticating to the NBCS SMTP server (smtp.rutgers.edu) with a specific
NetID and password.

%prep
%setup -n %{tardir}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}/html
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}/webbin

install -c -m 0555 $RPM_BUILD_DIR/%{tardir}/rplookup $RPM_BUILD_ROOT%{prefix}/%{name}/webbin/

install -c -m 0644 $RPM_BUILD_DIR/%{tardir}/*.php $RPM_BUILD_ROOT%{prefix}/%{name}/html/

%post
cat << EOF
The README is located in /usr/local/doc/webtools_whitelist/.
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

