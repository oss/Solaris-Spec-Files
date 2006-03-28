Summary:	A simple, elegant, and usable Gtk theme 
Name:		gtk2-clearlooks
Version:	0.6.2
Release:        2
Copyright:	GPL
Group:		System Environment/Themes
Source:		clearlooks-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
Requires:	gtk2 >= 2.8.10
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Clearlooks is a GTK+ 2.x engine written in C that transforms your 
GNOME/XFCE desktop into a modern looking environment. It is fast and 
easy on the eyes.

%prep
%setup -q -n clearlooks-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/gtk-2.0/2.4.0/engines/libclearlooks.so
/usr/local/share/*

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.6.2-1
- Initial Rutgers release
