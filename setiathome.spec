Summary: Find ET
Name: setiathome
Version: 3.03
Release: 2ru
Copyright: Closed
Group: Applications/Editors
Source: ftp://ftp.cdrom.com/pub/setiathome/setiathome-3.03.sparcv9-sun-solaris2.7.tar
Source1: ftp://ftp.cdrom.com/pub/setiathome/setiathome-3.03.sparc-sun-solaris2.6.tar
Source2: setiathome-init.d
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Find ET

%prep
%setup -c -n setiathome -T

%setup -q -D -n setiathome -T -a 0
%setup -q -D -n setiathome -T -a 1

#%setup -q

#%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/setiathome/ $RPM_BUILD_ROOT/etc/init.d/

%ifarch sparc
cp setiathome-3.03.sparc-sun-solaris2.6/setiathome $RPM_BUILD_ROOT/usr/local/setiathome/
%else
cp setiathome-3.03.sparcv9-sun-solaris2.7/setiathome $RPM_BUILD_ROOT/usr/local/setiathome/
%endif

cp %{SOURCE2} $RPM_BUILD_ROOT/etc/init.d/setiathome

chmod 755 $RPM_BUILD_ROOT/usr/local/setiathome/setiathome
/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/setiathome/setiathome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc setiathome-3.03.sparc-sun-solaris2.6/README
%defattr(755,root,root)
/usr/local/setiathome/setiathome
/etc/init.d/setiathome




