%define cvsdate 20030610

Summary: maildir-check
Name: maildir-check
Version: 0.%{cvsdate}
Release: 1ru
Group: System Environment/Base
Copyright: Rutgers
Source: %{name}-%{cvsdate}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl

%description
maildir-check is a program which checks and fixes people(s) maildir
folders.  See the internal usage for details.

%prep
%setup -q -n maildir-check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mv maildir-check $RPM_BUILD_ROOT/usr/local/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0755, root, root) /usr/local/sbin/maildir-check



