Name: pine
Version: 4.44
Release: RU4.1
Summary: UWash Pine email reader
Copyright: UWash/RU Hack Patch
Group: Applications/Email
Source0: %{name}%{version}.tar.gz
Patch0: pine4.44-RU4.patch
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl

%description
Pine is an email program. This version of pine includes SSL support.
This version of pine does NOT include support for the "mbox" driver, nor 
for LDAP. This release of pine is compiled to use the PAM libraries, 
although since it only contains the client programs I'm not sure if that 
matters.

%prep
%setup -q -n pine4.44
%patch -p1

%build
./build NOLDAP so5 PASSWDTYPE=pmb 

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
/usr/local/doc/pine-4.44
%{_mandir}/man1/*
/usr/local/bin/pi*
