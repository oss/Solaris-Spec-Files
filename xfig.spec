Name: xfig
Version: 3.2.4
Release: 2ru 
Summary: X11 drawing software
Copyright: Freely distributable
Group: Applications/Productivity
Source: xfig.%{version}.full.tar.gz
Patch: xfig.%{version}.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpng libjpeg xpm Xaw3d
#addt'l buildreq: vpkg-SPROcc 
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
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/X11/xfig/Libraries
/usr/ucb/install -c   xfig $RPM_BUILD_ROOT/usr/local/bin/xfig
/usr/ucb/install -c -m 0444 Fig.ad \
    $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults/Fig
/usr/ucb/install -c -m 0444 Fig-color.ad \
    $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults/Fig-color
chmod a+x,u+w $RPM_BUILD_ROOT/usr/local/lib/X11/xfig
/usr/ucb/install -c CompKeyDB $RPM_BUILD_ROOT/usr/local/lib/X11/xfig
cp -r Libraries $RPM_BUILD_ROOT/usr/local/lib/X11/xfig/
#(cd Libraries/Examples && tar cf - .) | \
#(cd $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries && tar xf -)
#chmod 644 `find $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries \! -type d`
install -c -m 0644 Doc/xfig.man $RPM_BUILD_ROOT/usr/local/man/man1/xfig.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
%doc Libraries/*fig Doc/*
/usr/local/bin/xfig
/usr/local/man/man1/xfig.1
/usr/local/lib/X11/app-defaults/Fig
/usr/local/lib/X11/app-defaults/Fig-color
/usr/local/lib/X11/xfig

%changelog
* Mon Oct 28 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed Imakefile to have xfig look for CompKeyDB and doc files in
   the correct place.
 - Added Changelog

