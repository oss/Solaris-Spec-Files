%define glib2_version 2.18.0
%define freetype2_version 2.3.8
%define fontconfig_version 2.6.0-3
%define cairo_version 1.8.6

Name:		pango
Version:	1.22.4
Release:	2
License:	LGPL
Group:		System Environment/Libraries
Source0:	%{name}-%{version}.tar.gz
Source1:	pango.modules
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
Summary:	System for layout and rendering of internationalized text.
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
# Assuming system has necessary X libraries pre-installed
Requires:	glib2 >= %{glib2_version}
Requires:	freetype2 >= %{freetype2_version}
Requires:       fontconfig >= %{fontconfig_version}
Requires:       cairo >= %{cairo_version}
Requires:	xft2
Requires:	xrender
BuildRequires:	libtool, pkgconfig
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	freetype2-devel >= %{freetype2_version}
BuildRequires:	fontconfig-devel >= %{fontconfig_version}
BuildRequires:  cairo-devel >= %{cairo_version}
BuildRequires:	xft2-devel
BuildRequires:	xrender-devel

%description
Pango is a system for layout and rendering of internationalized text.

%package devel
Summary:	System for layout and rendering of internationalized text.
Group:		Development/Libraries
Requires: 	pango = %{version}-%{release}
Requires:	glib2-devel >= %{glib2_version}
Requires: 	freetype2-devel >= %{freetype2_version}
Requires:	fontconfig-devel >= %{fontconfig_version}
Requires:       cairo-devel >= %{cairo_version}
Requires:	xft2-devel
Requires:	xrender-devel
Requires:	pkgconfig
	
%description devel
The pango-devel package includes the header files and
developer docs for the pango package.

%package doc
Summary:	Pango extra documentation
Requires:	pango = %{version}-%{release}
Group:		Documentation

%description doc
Pango extra documentation

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --disable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure			\
	--prefix=%{_prefix} 	\
	--mandir=%{_mandir}	\
	--disable-rebuilds	\
	--disable-gtk-doc

gmake -j3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/etc/pango
gmake install DESTDIR=%{buildroot}

# Remove files that should not be packaged
rm %{buildroot}%{_libdir}/pango/1.6.0/modules/*.la
rm %{buildroot}%{_libdir}/*.la

%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pango/pango.modules

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog HACKING 
%doc INSTALL MAINTAINERS NEWS README THANKS
%defattr(-,root,root)
%{_bindir}/pango-querymodules
%{_sysconfdir}/pango
%{_libdir}/libpango*.so.*
%{_libdir}/pango
%{_mandir}/man1/*.1

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libpango*.so
%{_libdir}/pkgconfig/*
%{_bindir}/pango-view

%files doc
%defattr(-,root,root)
%{_datadir}/gtk-doc/html/pango

%changelog
* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.22.4-2
- Fixes
* Wed Dec 17 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.22.4-1
- Updated to version 1.22.4
* Mon Jul 28 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.20.5-1
- bumped
* Fri Mar 21 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.20.0-1
- Bump to 1.20.0	
* Thu Oct 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.18.3-1
- Bump to 1.18.3
* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.18.0-1
- Bump to 1.18.0
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.17.3-1
- Bump to 1.17.3
* Wed May 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.16.4-1
- Updated to version 1.16.4

* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.10.4
- Updated to version 1.10.4

* Wed Jun 29 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-6
- Changed /usr/local/lib to /usr/local/bin in the PATH

* Fri Jun 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-5
- Added a line to the %files section to include some unpackaged files

* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-4
- switched back to gcc; see glib2.spec for the reason

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-3
- changed gcc to cc

* Wed May 20 2005 Jonathan Kaczynski - <jmkacz@nbcs.rutgers.edu> - 1.9.0-1
- Upgraded to latest release
