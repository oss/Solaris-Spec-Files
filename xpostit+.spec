Name: XPostitPlus
Version: 2.3
Release: 2
Summary: X11 meets 3M
Copyright: GPL
Group: Applications/Productivity
Source: XPostitPlus-2.3.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
XPostitPlus is a small application that lets you put electronic
"PostIt" notes on your screen.

%prep
%setup -q

%build
xmkmf -a
make CC=gcc CCOPTIONS="-O2" PICFLAGS="-fpic"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp xpostit+ $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults
cp XPostitPlus.ad $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/XPostitPlus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
/usr/local/bin/xpostit+
/usr/openwin/lib/X11/app-defaults/XPostitPlus


