Name: ghostview
Version: 1.5
Copyright: GPL
Group: Applications/Publishing
Summary: GNU Postscript viewer for X11
Release: 2
Source: ghostview-1.5.tar.gz
Requires: gs
BuildRoot: /var/tmp/%{name}-root

%description
Ghostview is a postscript viewer for X11.  It requires gs.

%prep
%setup -q

%build
xmkmf -a
make CC=gcc LINTOPTS="" CCOPTIONS="-g" PICFLAGS=-fpic

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults
install -c ghostview $RPM_BUILD_ROOT/usr/local/bin/ghostview
install -c -m 0444 Ghostview.ad \
   $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/Ghostview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/ghostview
/usr/openwin/lib/X11/app-defaults/Ghostview
