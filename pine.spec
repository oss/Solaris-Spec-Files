Name: pine
Version: 4.44
Release: RU3.2
Summary: WU Pine email reader
Copyright: UW/RU-hack
Group: Applications/Email
Source0: %{name}%{version}-RU3.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl

%description
Pine is an email program. This version of pine includes SSL support.
This version of pine does NOT include support for the "mbox" driver.

%prep
%setup -q -n pine4.44-RU3

%build
cd imap
sed s/'EXTRADRIVERS=mbox'/'EXTRADRIVERS='/g Makefile > Makefile.ru
mv Makefile.ru Makefile
cd ..
./build NOLDAP gs5

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pine $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pilot $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pico $RPM_BUILD_ROOT/usr/local/bin/

mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1/
install -m0644 doc/*.1 $RPM_BUILD_ROOT/usr/local/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc *.1
%{_mandir}/man1/*
/usr/local/bin/pi*
