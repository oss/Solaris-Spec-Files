%define name webtools_addons
%define version 0.1
%define release 2
%define prefix /usr/local

Summary: Scripts, usually to be run via cron to clean up various "leftovers" of certain webtools
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root

%description
Scripts, usually to be run via cron to clean up various "leftovers" of certain webtools.

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/sbin

install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/sbin/

%post
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}";
echo "The scripts provided require webtools to be installed somewhere";
echo "READ the README!!";

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%dir %{prefix}/%{name}-%{version}
%dir %{prefix}/%{name}-%{version}/sbin

%defattr(-, root, www)
%doc README
%{prefix}/%{name}-%{version}/sbin/*
