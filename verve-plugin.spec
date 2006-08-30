Summary:	Xfce - lightweight desktop environment
Name:		verve-plugin
Version:	0.3.4
Release:        1
Copyright:	GPL
Group:		Applications/Xfce
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	libxml2, libdbh, librsvg, startup-notification, gtk2, pkgconfig, xfce4-dev-tools, libxfce4util, libxfcegui4, libxfce4mcs, xfce4-panel, pcre
BuildRequires:	libxml2-devel, libdbh-devel, librsvg-devel, startup-notification, gtk2-devel, libxfce4util-devel, libxfcegui4-devel, libxfce4mcs-devel, xfce4-panel-devel

%description
Xfce is a lightweight desktop environment for unix-like operating 
systems. It aims to be fast and lightweight, while still being visually 
appealing and easy to use.

Xfce 4.2 embodies the traditional UNIX philosophy of modularity and 
re-usability. It consists of a number of components that together 
provide the full functionality of the desktop environment. They are 
packaged separately and you can pick and choose from the available 
packages to create the best personal working environment.

Another priority of Xfce 4 is adhereance to standards, specifically 
those defined at freedesktop.org.

Xfce 4 can be installed on several UNIX platforms. It is known to 
compile on Linux, NetBSD, FreeBSD, Solaris, Cygwin and MacOS X, on x86, 
PPC, Sparc, Alpha...

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/openwin/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/pcre/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/pcre/lib -R/usr/local/pcre/lib -lintl" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local

mv scripts/Makefile scripts/Makefile.wrong
sed -e 's/$(INSTALL) verve-focus $(bindir)/$(INSTALL) verve-focus \/var\/tmp\/%{name}-%{version}-root$(bindir)\/verve-focus/' scripts/Makefile.wrong > scripts/Makefile

make

%install
rm -rf $RPM_BUID_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local/bin

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/libexec/xfce4/panel-plugins/*
/usr/local/share/*

%changelog
* Tue May 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.3.0-1
- Initial Rutgers release
