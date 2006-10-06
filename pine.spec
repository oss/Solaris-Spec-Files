Name: 		pine
Version: 	4.64
Release: 	4
Summary: 	UWash Pine email reader
Copyright: 	UWash
Group: 		Applications/Email
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Source0: 	%{name}-%{version}.tar.bz2
BuildRoot: 	/var/tmp/%{name}-%{version}
Requires:	openldap
BuildRequires: 	openssl >= 0.9.7e-3, openldap-devel

%description
Pine is an email program. This version of pine includes SSL support.

%prep
%setup -q -n pine%{version}

%build
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/sfw/lib -R/usr/local/sfw/lib"
#PATH="/usr/local/lib:/usr/sfw/bin:/usr/local/ssl/lib:$PATH"
#export LDFLAGS 
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -llber" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./build soc PASSWDTYPE=pmb SSLTYPE=unix SSLDIR=/usr/local/ssl SSLLIB=/usr/local/ssl/lib

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pine $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pilot $RPM_BUILD_ROOT/usr/local/bin/
install -m0755 bin/pico $RPM_BUILD_ROOT/usr/local/bin/

mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1/
install -m0644 doc/*.1 $RPM_BUILD_ROOT/usr/local/man/man1/

cd doc
mkdir -p $RPM_BUILD_ROOT/usr/local/doc/pine-%{version}
install -m0644 brochure.txt mailcap.unx mime.types pine-ports tech-notes.txt $RPM_BUILD_ROOT/usr/local/doc/pine-%{version}/
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
/usr/local/doc/*
%{_mandir}/man1/*
/usr/local/bin/pi*

%changelog
* Tue Jun 13 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.64-2
- Enabled OpenLDAP
* Tue Oct 18 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.64-1
- Version 4.64 
* Fri May 27 2005 John M. Santel <jmsl@nbcs.rutgers.edu> - 4.63-1
- updated to 4.63 
- changed compiler to Sun's cc and used defaults for soc build target to improve stablity 
* Fri Feb 04 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> -  4.62-2
- Fixed openssl problem
* Tue Feb 01 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> -  4.62-1
- Updated to 4.62
