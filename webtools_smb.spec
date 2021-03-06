%define name webtools_smb
%define version 0.1
%define release 2 
%define prefix /usr/local

Summary: Web application allowing users to setup access to a Samba account
Name: %name
Version: %version
Release: %release
License: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4

%description
Web application allowing users to setup access to a Samba account

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin

install -c -m 4555 $RPM_BUILD_DIR/%{name}-%{version}/src/samba-account $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/

%post
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}";
echo "READ the README!!";

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%dir %{prefix}/%{name}-%{version}
%dir %{prefix}/%{name}-%{version}/html
%dir %{prefix}/%{name}-%{version}/webbin

%defattr(-, root, www)
%doc README
%{prefix}/%{name}-%{version}/html/*
%attr(- ,root, www)%{prefix}/%{name}-%{version}/webbin/*

%changelog
* Wed Sep 2 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.1-2
- Fixed commit file.
