%define name webtools_vmail
%define version 0.4
%define release 5
%define prefix /usr/local

Summary: Web application addon for allowing departments to setup users for virtual domains
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4

%description
Web application addon, allowing departments to setup users for virtual domains   

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/

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

%defattr(-, root, www)
%doc README
%{prefix}/%{name}-%{version}/html/*
