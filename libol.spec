%define name libol
%define version 0.3.16
%define release 1
%define prefix /usr/local

Summary: Support library for syslog-ng

Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: System Environment/Libraries
Url: http://www.balabit.hu/products/syslog-ng/
Source0: http://www.balabit.hu/downloads/syslog-ng/libol/0.3/libol-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root

%description
Support library for syslog-ng.

%package devel
Summary: libol headers, libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
libol headers, libraries

%prep
%setup

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make -e DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/bin/libol-config
%{prefix}/lib/libol.so
%{prefix}/lib/libol.so.0
%{prefix}/lib/libol.so.0.0.0

%files devel
%defattr(-,root,root)
%{prefix}/bin/make_class
%{prefix}/include/libol
%{prefix}/lib/libol.a
#%{prefix}/lib/libol.la
