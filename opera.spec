Summary: Opera
Name: opera
Version: 8.50
Release: 1
Copyright: Freely distributed
Group: Applications/Internet
Source: opera-8.50-static.tar.gz
URL: http://www.opera.com
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
Opera is a full feature web browser. It includes pop-up blocking, tabbed browsing, integrated searches, E-mail, RSS Newsfeeds and IRC chat.

%prep
%setup -q -n opera

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local
cd ..
cp -R opera $RPM_BUILD_ROOT/usr/local
cp opera/bin/opera $RPM_BUILD_ROOT/usr/local/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/opera
/usr/local/bin

%changelog
* Mon Oct 03 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 8.50-1
- First release: Version Opera 8.50
