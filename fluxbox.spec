Summary: Nano: GNU version of pico
Name: fluxbox
Version: 0.1.14
Release: 1ru
Copyright: GPL
Group: X11/Window Managers
Source: http://prdownloads.sourceforge.net/fluxbox/fluxbox-0.1.14.tar.bz2
URL: http://fluxbox.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Fluxbox is yet another windowmanager for X.
It's based on the Blackbox 0.61.1 code. Fluxbox looks like blackbox and handles styles, colors, window placement and similar thing exactly like blackbox (100% theme/style compability).

So what's the difference between fluxbox and blackbox then?
The answer is: LOTS!

%prep
%setup -q

%build
CC="gcc" ./configure --prefix=/usr/local --disable-dependency-tracking


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
#/usr/ccs/bin/strip $RPM_BUILD_ROOT/usr/local/bin/nano

%clean
rm -rf $RPM_BUILD_ROOT

%files
/




