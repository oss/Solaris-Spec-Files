%define name webtools_squirrelmail
%define version 0.1
%define release 1
%define prefix /usr/local

Summary: Script run by spam_buttons plugin of squirrelmail
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}
BuildRoot: %{_tmppath}/%{name}-root
Requires: webtools >= 0.4 pear-DB pear-HTML

%description
This is an addon package to webtools. It is run by the spam_buttons plugin 
of squirrelmail.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}/html
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}/webbin

install -c -m 0555 %{SOURCE0} $RPM_BUILD_ROOT%{prefix}/%{name}/webbin/spamfilter

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,www,555)
%{prefix}/%{name}/webbin/*
