%define cvsdate 20030501

Summary: Software to check release dependencies
Name: checkrelease
Version: 0.%{cvsdate}
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: repository-scripts-%{cvsdate}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: bash

%description
Software to check release dependencies

%prep
%setup -q -n repository-scripts

#%patch -p1

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/checkrelease \
    $RPM_BUILD_ROOT/usr/local/bin \
    $RPM_BUILD_ROOT/var/local/checkrelease \
    $RPM_BUILD_ROOT/rpm/webroot/rpm/status
cp checkrelease.sh $RPM_BUILD_ROOT/usr/local/bin/
chmod 700 $RPM_BUILD_ROOT/usr/local/bin/checkrelease.sh
cp *.complete $RPM_BUILD_ROOT/usr/local/etc/checkrelease/
chmod 600 $RPM_BUILD_ROOT/usr/local/etc/checkrelease/*.complete
chmod 700 $RPM_BUILD_ROOT/usr/local/etc/checkrelease
chmod 700 $RPM_BUILD_ROOT/var/local/checkrelease
chmod 755 $RPM_BUILD_ROOT/rpm/webroot/rpm/status

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/checkrelease.sh
/usr/local/etc/checkrelease
/rpm/webroot/rpm/status
/var/local/checkrelease

