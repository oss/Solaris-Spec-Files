%define name webtools_newperms
%define version 0.1
%define release 1
%define prefix /usr/local

Summary: Web application allowing users to tighten up permissions for files 
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4

%description
Web application allowing users to tighten up permissions for files 

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin

install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/fixperms $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/

%post
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}";
echo "ln -s /usr/bin/touch /usr/local/webtools/webbin/touch";
echo "ln -s /usr/bin/chmod /usr/local/webtools/webbin/chmod";
echo "mkdir -m 0700 /usr/local/apache/logs/webtools_logs";
echo "chown www:www /usr/local/apache/logs/webtools_logs";
echo "READ the README!!";

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%dir %{prefix}/%{name}-%{version}
%dir %{prefix}/%{name}-%{version}/html
%dir %{prefix}/%{name}-%{version}/webbin

%defattr(-, www, www)
%doc README
%{prefix}/%{name}-%{version}/html/*
%attr(- ,root, www)%{prefix}/%{name}-%{version}/webbin/*
