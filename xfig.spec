Name: xfig
Version: 3.2.3d
Release: 3
Summary: X11 drawing software
Copyright: Freely distributable
Group: Applications/Productivity
Source: xfig.%{version}.full.tar.gz
Patch: xfig.%{version}.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc libpng libjpeg xpm Xaw3d
Requires: libpng libjpeg xpm Xaw3d transfig

%description
Xfig is an X11 drawing program that can produce output in several
formats.

%prep
%setup -q -n xfig.%{version}
%patch -p1

%build
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries
/usr/ucb/install -c   xfig $RPM_BUILD_ROOT/usr/local/bin/xfig
/usr/ucb/install -c -m 0444 Fig.ad \
    $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/Fig
/usr/ucb/install -c -m 0444 Fig-color.ad \
    $RPM_BUILD_ROOT/usr/openwin/lib/X11/app-defaults/Fig-color
chmod a+x,u+w $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig
/usr/ucb/install -c CompKeyDB $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig
(cd Examples/Libraries && tar cf - .) | \
(cd $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries && tar xf -)
find $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries \! -type d | \
xargs chmod 644
install -c -m 0644 Doc/xfig.man $RPM_BUILD_ROOT/usr/local/man/man1/xfig.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%doc Examples/*fig Doc/*
/usr/local/bin/xfig
/usr/local/man/man1/xfig.1
/usr/openwin/lib/X11/app-defaults/Fig
/usr/openwin/lib/X11/app-defaults/Fig-color
/usr/openwin/lib/X11/xfig
