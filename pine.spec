Name: pine
Version: 4.62
Release: 3
Summary: UWash Pine email reader
Copyright: UWash
Group: Applications/Email
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
Source0: %{name}-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl >= 0.9.7e-3

%description
Pine is an email program. This version of pine includes SSL support.

%prep
%setup -q -n pine4.62

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/sfw/lib -R/usr/local/sfw/lib"
CC="gcc -03 -pipe -s -fforce-addr"
PATH="/usr/local/lib:/usr/sfw/bin:/usr/local/ssl/lib:$PATH"
export LDFLAGS CC PATH
alias make=gmake
./build CC=gcc NOLDAP so5 PASSWDTYPE=pmb SSLDIR=/usr/local/ssl SSLLIB=/usr/local/ssl/lib

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pine $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pilot $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pico $RPM_BUILD_ROOT/usr/local/bin/

mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1/
install -m0644 doc/*.1 $RPM_BUILD_ROOT/usr/local/man/man1/

cd doc
mkdir -p $RPM_BUILD_ROOT/usr/local/doc/pine-4.62
install -m0644 brochure.txt mailcap.unx mime.types pine-ports tech-notes.txt $RPM_BUILD_ROOT/usr/local/doc/pine-4.62/
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
/usr/local/doc/*
%{_mandir}/man1/*
/usr/local/bin/pi*

%changelog
* Fri Feb 04 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> -  4.62-2
- Fixed openssl problem
* Tue Feb 01 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> -  4.62-1
- Updated to 4.62
