%define name check-criteria 
%define version 1.0
%define release 3 
%define prefix /usr/local

Summary: Check file criteria
Name: %name
Version: %version
Release: %release
Group: Applications/Internet
License: RU
Source: %name 
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl

%description
Check file criteria

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/bin
install -c -m 0555 $RPM_SOURCE_DIR/check-criteria $RPM_BUILD_ROOT%{prefix}/bin/check-criteria
#mkdir -p %{buildroot}/usr/local/bin/
#install -m 0555 $RPM_SOURCE_DIR/check-criteria %{buildroot}/usr/local/bin/check-criteria

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other) 
%prefix/bin/check-criteria
