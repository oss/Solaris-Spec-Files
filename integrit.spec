%define name integrit
%define version 2.01
%define release .01
%define prefix /usr/local

Summary: An intrusion detection system.

Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/System
Copyright: GPL
Url: http://integrit.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/integrit/integrit-2.01.01.tar.gz
BuildRoot: /tmp/free/%{name}-root

%description
integrit is an alternative to file integrity verification programs like
tripwire and aide. It helps you determine whether an intruder has modified
a computer system.

%prep
%setup

%build
./configure --prefix=%{prefix}
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}
mkdir -p $RPM_BUILD_ROOT%{prefix}/sbin
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/man1

install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/integrit $RPM_BUILD_ROOT%{prefix}/sbin
install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/doc/i-ls.1 $RPM_BUILD_ROOT%{prefix}/man/man1
install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/doc/i-viewdb.1 $RPM_BUILD_ROOT%{prefix}/man/man1
install -c -m 755 $RPM_BUILD_DIR/%{name}-%{version}/doc/integrit.1 $RPM_BUILD_ROOT%{prefix}/man/man1

%files
%doc doc
%attr(755,root,root) %{prefix}/sbin/integrit

%clean
rm -r $RPM_BUILD_ROOT

