%define majorv 1.26
%define minorv 0

Name:		atk
Version:	%{majorv}.%{minorv}
Release:	1
Group:		System Environment/Libraries
License:	GPL
URL:		http://library.gnome.org/devel/atk
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/atk/%{majorv}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	glib2-devel

Summary:        Interfaces for accessibility support

%description
The ATK library provides a set of interfaces for adding
accessibility support to applications and graphical user
interface toolkits. By aupporting the ATK interface, an
application or toolkit can be used with tools such as
screen readers, magnifiers, and alternative input devices.

%package devel
Group:		System Environment/Libraries
Requires: 	atk = %{version}-%{release}
Requires:	glib2-devel
Summary:	atk development files

%description devel
This package contains files needed for building applications that use atk.

%package doc
Group:          System Environment/Libraries
Summary:        atk development files
Requires:	atk-devel = %{version}-%{release}
Summary:        Extra documentation for atk

%description doc
This package contains the gtk-doc documentation for atk.

%prep
%setup -q -n %{name}-%{version}
%{__sed} -i '/gtkdoc-rebase/d' docs/Makefile.in

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

# --disable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure			\
	--prefix=%{_prefix} 	\
	--disable-nls 		\
	--disable-rebuilds 	\
	--disable-gtk-doc

gmake -j3

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

rm %{buildroot}%{_libdir}/*.la 

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS 
%doc MAINTAINERS NEWS ChangeLog
%{_libdir}/*.so.*
%{_datadir}/locale/*/LC_MESSAGES/*

%files devel
%defattr(-, root, root)
%{_includedir}/atk-*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/atk.pc

%files doc
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/*

%changelog
* Fri Jul 17 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.26.0-1
- Updated to version 1.26.0
- Moved .so symlink to devel package

* Wed Nov 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.24.0-1
- Fixed doc permissions and updated to version 1.24.0

* Tue Sep 02 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.23.5-1
- Added some docs and updated to latest version

* Tue Jan 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.20.0-1
- Updated to latest version

* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.19.6-1
- Bump to 1.19.6

* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.19.3
- Updated to 1.19.3

* Mon May 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.11.4
- Updated to latest version

* Tue Feb 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.9.0-5
- Fixed library linking problem

* Tue Feb 21 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.9.0-5
- Built on top of latest version of glib2

* Wed Jun 22 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-4
- switched back to gcc; see glib2.spec for reason

* Mon Jun 06 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-3
- changed gcc to cc

* Wed May 25 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-2
- Made a few tweaks to the spec file

* Tue May 24 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.9.0-1
- Upgraded to latest release
