Name: xfig
Version: 3.2.4
Release: 3ru 
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
%ifos solaris2.9
LD_LIBRARY_PATH=/usr/sfw/lib
LD_RUN_PATH=/usr/sfw/lib
export LD_LIBRARY_PATH LD_RUN_PATH
make LIBDIR=/usr/local/lib SYSINCDIR=/usr/sfw/include
%else
make LIBDIR=/usr/local/lib SYSINCDIR=/usr/local/include
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
#mkdir -p $RPM_BUILD_ROOT/usr/local/lib/X11/xfig
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/xfig/Libraries
/usr/ucb/install -c   xfig $RPM_BUILD_ROOT/usr/local/bin/xfig
/usr/ucb/install -c -m 0444 Fig.ad \
    $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults/Fig
/usr/ucb/install -c -m 0444 Fig-color.ad \
    $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults/Fig-color
#chmod a+x,u+w $RPM_BUILD_ROOT/usr/local/lib/X11/xfig
/usr/ucb/install -c CompKeyDB $RPM_BUILD_ROOT/usr/local/lib/xfig
cp -r Libraries $RPM_BUILD_ROOT/usr/local/lib/xfig/
#(cd Libraries/Examples && tar cf - .) | \
#(cd $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries && tar xf -)
#chmod 644 `find $RPM_BUILD_ROOT/usr/openwin/lib/X11/xfig/Libraries \! -type d`
install -c -m 0644 Doc/xfig.man $RPM_BUILD_ROOT/usr/local/man/man1/xfig.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You must make these symlinks:
ln -s /usr/local/lib/X11/app-defaults/Fig \
        /usr/openwin/lib/X11/app-defaults/Fig
ln -s /usr/local/lib/X11/app-defaults/Fig-color \
        /usr/openwin/lib/X11/app-defaults/Fig-color
EOF

%postun
cat <<EOF
You may remove these symlinks:
/usr/openwin/lib/X11/app-defaults/Fig
/usr/openwin/lib/X11/app-defaults/Fig-color
EOF


%files
%defattr(-, bin, bin)
%doc Libraries/*fig Doc/*
/usr/local/bin/xfig
/usr/local/man/man1/xfig.1
#/usr/openwin/lib/X11/app-defaults/Fig
#/usr/openwin/lib/X11/app-defaults/Fig-color
#/usr/openwin/lib/X11/xfig
/usr/local/lib/X11/app-defaults/*
/usr/local/lib/xfig/*
#/usr/local/lib/X11/xfig/CompKeyDB

%changelog
* Mon Oct 28 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed Imakefile to have xfig look for CompKeyDB and doc files in
   the correct place.
 - Added Changelog

