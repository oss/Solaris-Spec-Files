%define name maildrop-tools
%define version 0.1
%define release 1
%define prefix /usr/local

Summary: Scripts, usually to be run via cron to clean up various maildrop things
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root
Requires: maildrop

%description
Scripts, usually to be run via cron to clean up various maildrop things.

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/sbin

install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/* $RPM_BUILD_ROOT%{prefix}/sbin/

%post
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "READ the README!!";

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%{prefix}/sbin/*
