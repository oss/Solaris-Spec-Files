Summary: X remote shell utility
Name: xrsh
Version: 1.0
Release: 2
Group: Applications/Intenet
Copyright: Rutgers
Source: xrsh-1.0.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Xrsh is a remote shell utility for X.

%prep
%setup -q
# Xrsh is a single shell script, but by using %setup, etc. the shell
# script is included in source RPMs.  I could fool with the macros, but
# this way is portable across versions of rpm.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install xrsh $RPM_BUILD_ROOT/usr/local/bin/xrsh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755,root,other) /usr/local/bin/xrsh
