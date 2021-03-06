%define major 1.24
%define minor 4

Name:		pango
Version:	%{major}.%{minor}
Release:	1
Group:		System Environment/Libraries
License:	LGPL
URL:		http://www.pango.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pango/%{major}/pango-%{version}.tar.bz2
Source1:	pango.modules
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	libtool-devel, pkgconfig
BuildRequires:	glib2-devel, freetype2-devel, fontconfig-devel
BuildRequires:  cairo-devel, xft2-devel, xrender-devel

Summary:        System for layout and rendering of internationalized text

%description
Pango is a system for layout and rendering of internationalized text.

%package devel
Group:		Development/Libraries

Requires: 	pango = %{version}-%{release}
Requires:	glib2-devel, freetype2-devel, fontconfig-devel
Requires:	cairo-devel, xft2-devel, xrender-devel
Requires:	pkgconfig

Summary:        Development files for pango
	
%description devel
The pango-devel package includes the header files and
developer docs for the pango package.

%package doc
Group:		Documentation

Requires:       pango = %{version}-%{release}

Summary:        Extra documentation for pango

%description doc
Additional documentation for pango

%prep
%setup -q
%{__sed} -i "/gtkdoc-rebase/d" docs/Makefile.in

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS TOOLS_NOOP

./configure				\
	--prefix=%{_prefix} 		\
	--mandir=%{_mandir}		\
	--disable-rebuilds		\
	--disable-man			\
	--disable-gtk-doc		\
	--disable-doc-cross-references

gmake -j3 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/pango
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
%{_mandir}/man1/*

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
* Wed Jul 15 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.24.4-1
- Updated to version 1.24.4
* Mon May 18 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.24.2-1
- Updated to version 1.24.2
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
