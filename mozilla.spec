Name: mozilla
Version: 1.2a
Copyright: MPL
Group: Applications/Web
Summary: Mozilla
Release: 1
Packager: Rutgers University
Source: mozilla-sparc-sun-solaris2.8-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Mozilla is an open source web/email/irc/etc. package.

%prep
%setup -n mozilla

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/mozilla
#cpdir . $RPM_BUILD_ROOT/usr/local/mozilla
/usr/local/gnu/bin/cp -R * $RPM_BUILD_ROOT/usr/local/mozilla

#mkdir -p $RPM_BUILD_ROOT/usr/local
#cd ..
#mv mozilla $RPM_BUILD_ROOT/usr/local

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/mozilla
