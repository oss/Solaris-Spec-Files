Summary: Imake templates and X config files
Name: X_setup
Version: 1
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: X_setup.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
This package contains config files for X Windows.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
%config /etc/dt/config/Xsession.d/0015.sun.env
%config /usr/openwin/lib/config/*
