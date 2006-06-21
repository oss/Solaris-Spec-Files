%define opera_dir opera-9.0

Summary: Opera
Name: opera
Version: 9.0
Release: 4
Copyright: Freely distributed
Group: Applications/Internet
Source: opera-%{version}-static.tar.bz2
Source1: opera-wrapper
URL: http://www.opera.com
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
Opera is a full feature web browser. It includes pop-up blocking, tabbed browsing, integrated searches, E-mail, RSS Newsfeeds and IRC chat.

%prep
%setup -q -n %{opera_dir}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cd ..
cp -R %{opera_dir} $RPM_BUILD_ROOT/usr/local/opera
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/local/opera/bin/opera
cd $RPM_BUILD_ROOT/usr/local/bin
ln -s ../opera/bin/opera opera

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/opera
/usr/local/bin

%changelog
* Tue Jun 20 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 9.0-1
Updated to 9.0
* Mon Oct 03 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 8.50-1
- First release: Version Opera 8.50
