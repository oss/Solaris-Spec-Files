Summary: phpSched
Name: phpSched
Version: 0.9b
Release: 1
Copyright: GPL
Group: Misc
Source: http://telia.dl.sourceforge.net/sourceforge/phpsched/phpSched-0.9b.tar.gz
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root
Requires: php

%description
(null)
%prep
%setup -q -n phpSched-0.9b

%build

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/apache/htdocs/phpSched-0.9b
cp -r * $RPM_BUILD_ROOT/usr/local/apache/htdocs/phpSched-0.9b/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/apache/htdocs/phpSched-0.9b



