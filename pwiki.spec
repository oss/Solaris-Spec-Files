Summary: pwiki
Name: pwiki
Version: 1.2.2
Release: 1
Copyright: GPL
Group: Misc
Source: http://wiki.2gn.com/wiki-files/wiki/pwiki-dist-1.2.2.tgz
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root
Requires: php

%description
(null)
%prep
%setup -q -n pwiki

%build

%install

tar xvf pwiki.tar
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/apache/htdocs/
cp -r pwiki $RPM_BUILD_ROOT/usr/local/apache/htdocs/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/apache/htdocs/pwiki



