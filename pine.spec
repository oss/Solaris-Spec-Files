Name: pine
Version: 4.58
Release: 1
Summary: UWash Pine email reader
Copyright: UWash
Group: Applications/Email
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl

%description
Pine is an email program. This version of pine includes SSL support.

%prep
%setup -q -n pine4.58

%build
alias make=gmake
./build CC=gcc NOLDAP so5 PASSWDTYPE=pmb 

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pine $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pilot $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pico $RPM_BUILD_ROOT/usr/local/bin/

mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1/
install -m0644 doc/*.1 $RPM_BUILD_ROOT/usr/local/man/man1/

cd doc
mkdir -p $RPM_BUILD_ROOT/usr/local/doc/pine-4.44
install -m0644 brochure.txt mailcap.unx mime.types pine-ports tech-notes.txt $RPM_BUILD_ROOT/usr/local/doc/pine-4.44/
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
/usr/local/doc/*
%{_mandir}/man1/*
/usr/local/bin/pi*
