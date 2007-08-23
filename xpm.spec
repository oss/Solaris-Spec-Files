Name:		xpm
Version:	3.4k
Copyright:	Freely distributable
Group:		User Interface/X
Summary:	The XPM library
Release:	5
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       David Lee Halik <dhalik@nbcs.rutgers.edu>
Source:		xpm-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	make
Conflicts:	vpkg-SFWxpm

%description
xpm is is a library that lets you manipulate X pixmaps.  It is used by
several X programs.

%prep
%setup -q
mv doc/xpm.PS.gz doc/xpm.ps.gz

%build
rm -rf %{buildroot}
set +e; xmkmf -a

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake LINTOPTS="" CCOPTIONS="-g" PICFLAGS="-Kpic"

%install
rm -rf %{buildroot}
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

%changelog
* Thu Aug 23 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.4.k-1
- This was apprently already built and disappeared into infinity, rebuilding
