Name: xpm
Version: 3.4k
Copyright: Freely distributable
Group: User Interface/X
Summary: The XPM library
Release: 4
Provides: libXpm.so.4.11 libXpm.so
Source: xpm-%{version}.tar.gz
Patch: xpm-%{version}.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: make
Conflicts: vpkg-SFWxpm

%description
xpm is is a library that lets you manipulate X pixmaps.  It is used by
several X programs.

%prep
%setup -q
%patch -p1
mv doc/xpm.PS.gz doc/xpm.ps.gz

%build
set +e; xmkmf -a
gmake CC=gcc LINTOPTS="" CCOPTIONS="-g" PICFLAGS=-fpic

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT \
	INCROOT=/usr/local/include \
	USRLIBDIR=/usr/local/lib \
	SHLIBDIR=/usr/local/lib \
	MANPATH=/usr/local/man BINDIR=/usr/local/bin \
	MKDIRHIER=/usr/openwin/bin/mkdirhier
if [ -r $RPM_BUILD_ROOT/usr/local/include/X11/X11/xpm.h ] ; then
    mv $RPM_BUILD_ROOT/usr/local/include/X11/X11/xpm.h \
       $RPM_BUILD_ROOT/usr/local/include/X11/xpm.h
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/xpm.ps.gz
/usr/local/lib/lib*.so*
/usr/local/include/X11/xpm.h
/usr/local/bin/sxpm
/usr/local/bin/cxpm
