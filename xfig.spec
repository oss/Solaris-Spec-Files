Name: xfig
Version: 3.2.5
Release: 1
Summary: X11 drawing software
Copyright: Freely distributable
Group: Applications/Productivity
Source: xfig.%{version}.full.tar.gz
Patch: xfig-3.2.5.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: libpng3-devel libjpeg-devel xpm Xaw3d
Requires: libpng3 libjpeg xpm Xaw3d transfig

%description
Xfig is an X11 drawing program that can produce output in several
formats.

%prep
%setup -q -n xfig.%{version}
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS 

xmkmf
gmake Makefiles
gmake includes
gmake depend
gmake -j3 LIBDIR=/usr/local/lib

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
#mkdir -p $RPM_BUILD_ROOT/usr/local/lib/X11/xfig
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/xfig/Libraries
install -c   xfig $RPM_BUILD_ROOT/usr/local/bin/xfig
install -c -m 0444 Fig.ad $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults/Fig
install -c -m 0444 Fig-color.ad $RPM_BUILD_ROOT/usr/local/lib/X11/app-defaults/Fig-color
#chmod a+x,u+w $RPM_BUILD_ROOT/usr/local/lib/X11/xfig
install -c CompKeyDB $RPM_BUILD_ROOT/usr/local/lib/xfig
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
%doc CHANGES README FIGAPPS LATEX.AND.XFIG Libraries/*fig Doc/*
/usr/local/bin/xfig
/usr/local/man/man1/xfig.1
/usr/local/lib/X11/app-defaults/*
/usr/local/lib/xfig/*

%changelog
* Thu Nov 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.2.5-1
- Bump to 3.2.5
* Mon Oct 28 2002 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Changed Imakefile to have xfig look for CompKeyDB and doc files in
   the correct place.
 - Added Changelog
