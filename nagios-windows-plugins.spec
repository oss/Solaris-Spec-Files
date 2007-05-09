%define name nagios-windows-plugins
%define version 1.0
%define release 1
%define prefix /usr/local 

Summary:	Windows SNMP plugins for Nagios 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
License:	Unknown
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	net-snmp, perl

%description
Nagios monitoring plugins that use SNMP to monitor MS Windows
cpu, hd, memory, and processes

%prep
%setup -q -n %{name}-%{version}

#%build

%install
mkdir -p %{buildroot}%{prefix}/nagios/libexec
cp check_win* %{buildroot}%{prefix}/nagios/libexec/
chmod u+x %{buildroot}%{prefix}/nagios/libexec/ check_win*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,nagios,nagios)
%{prefix}/nagios/libexec/check*

%changelog
* Wed May 09 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.0-1
- Initial Build.

