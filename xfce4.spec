Summary:	Xfce - lightweight desktop environment
Name:		xfce4
Version:	4.3.90.2
Release:        1
Copyright:	GPL
Group:		Applications/Xfce
Source1:	Xsession.xfce4
Source2:	Xsession.xfce43
Source3:	Xresources.xfce4
Source4:	Xfce4logo.pm
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	libxml2, libdbh, librsvg, startup-notification, gtk2, pkgconfig, Terminal, Thunar, dbus, gtk-xfce-engine, libexo, libxfce4mcs, libxfce4util, libxfcegui4, mousepad, orage, vte, xfce-mcs-manager, xfce-mcs-plugins, xfce-utils, xfce4-appfinder, xfce4-dev-tools, xfce4-icon-theme, xfce4-mixer, xfce4-panel, xfce4-session, xfdesktop, xfprint, xfwm4, xfwm4-themes, xarchiver, hicolor-icon-theme, xmms, verve-plugin, xfce4-quicklauncher-plugin, xfce4-weather-plugin, xfce4-xmms-plugin

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

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/dt/config/C/Xresources.d
mkdir -p $RPM_BUILD_ROOT/etc/dt/appconfig/icons/C

cd $RPM_BUILD_ROOT
/usr/local/gnu/bin/install -c -m 0555 %{SOURCE1} $RPM_BUILD_ROOT/etc/dt/config/Xsession.xfce4
/usr/local/gnu/bin/install -c -m 0555 %{SOURCE2} $RPM_BUILD_ROOT/etc/dt/config/Xsession.xfce43
/usr/local/gnu/bin/install -c -m 0444 %{SOURCE3} $RPM_BUILD_ROOT/etc/dt/config/C/Xresources.d/Xresources.xfce4
/usr/local/gnu/bin/install -c -m 0444 %{SOURCE4} $RPM_BUILD_ROOT/etc/dt/appconfig/icons/C/Xfce4logo.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/etc/dt/config/*
/etc/dt/appconfig/icons/C/*

%changelog
* Wed Aug 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.3.90.2-1
- Updated to latest version, changed any gcc depends to Sun CC
* Tue May 30 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 4.3.90.1-1
- Initial Rutgers release
