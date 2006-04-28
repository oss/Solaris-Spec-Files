Summary:	GQview - an image browser 
Name:		GQview
Version:	2.1.1
Release:        3
Copyright:	GPL
Group:		Applications/Multimedia
Source:		gqview-%{version}.tar.gz
Patch:		gqview.settings.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk2 >= 2.8.16 libpng3

%description
GQview is an image viewer for Unix operating systems (developed on 
Linux). It's key features include single click file viewing, external 
editor support, thumbnail preview, and zoom features. Some image 
management features are also included.

%prep
%setup -q -n gqview-%{version}
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lsocket" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*
/usr/local/share/*
/usr/local/man/man1/*

%changelog
* Thu Mar 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.1.1-1
- Initial Rutgers release
