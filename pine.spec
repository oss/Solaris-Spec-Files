Name: pine
Version: 4.44
Release: 2ru
Summary: WU Pine email reader
Copyright: UW/RU-hack
Group: Applications/Email
Source0: %{name}-%{version}-ru.tar.bz2
BuildRoot: /var/tmp/%{name}-%{version}


%description
Pine is an email program.

%prep
%setup -q -n pine-4.44-ru

%build

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

