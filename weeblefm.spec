Summary: weeblefm
Name: weeblefm
Version: 0.0.1
Release: 1
Copyright: GPL
Group: Misc
Source: weeblefm.tar.bz2
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root
Requires: php

%description
(null)
%prep
%setup -q -n weeblefm

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/apache/htdocs/weeblefm
cp -r * $RPM_BUILD_ROOT/usr/local/apache/htdocs/weeblefm/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/apache/htdocs/weeblefm



