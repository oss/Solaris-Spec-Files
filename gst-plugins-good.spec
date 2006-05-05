Summary:	a set of good-quality GStreamer plug-ins under our preferred license, LGPL
Name:		gst-plugins-good
Version:	0.10.2
Release:        1
Copyright:	LGPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gstreamer, liboil
BuildRequires:	gstreamer-devel, liboil-devel

%description
GStreamer Good Plug-ins is a set of plug-ins that we consider to have 
good quality code, correct functionality, our preferred license (LGPL 
for the plug-in code, LGPL or LGPL-compatible for the supporting 
library).

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
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
/usr/local/lib/gstreamer-0.10/*.so
/usr/local/lib/gstreamer-0.10/*so
/usr/local/etc/*

%changelog
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.2-1
- Initial Rutgers release
