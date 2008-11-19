%define majorv 1.24
%define minorv 0

Name:		atk
Version:	%{majorv}.%{minorv}
Release:	1
License:	LGPL
Group:		System Environment/Libraries
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/atk/%{majorv}/%{name}-%{version}.tar.gz
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
Summary:	Interfaces for accessibility support.
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	glib2 >= 2.16.5
BuildRequires:	glib2-devel >= 2.16.5

%description
The ATK library provides a set of interfaces for adding
accessibility support to applications and graphical user
interface toolkits. By aupporting the ATK interface, an
application or toolkit can be used with tools such as
screen readers, magnifiers, and alternative input devices.

%package devel
Summary: System for layout and rendering of internationalized text.
Requires: %{name} = %{version}-%{release}
BuildRequires: glib2-devel >= 2.14.0
Group: Development
%description devel
The atk-devel package includes the header files and
developer docs for the atk package.

%package doc
Summary: %{name} extra documentation
Requires: %{name} = %{version}-%{release}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --disable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure \
	--prefix=/usr/local \
	--disable-nls \
	--disable-rebuilds \
	--disable-gtk-doc

gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
cd %{buildroot}
rm .%{_libdir}/libatk-1.0.la 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,other)
%doc README NEWS COPYING AUTHORS MAINTAINERS ChangeLog
%{_libdir}/*so*
%{_datadir}/locale/*

%files devel
%defattr(-,root,other)
%{_includedir}/atk-1.0/*
%{_libdir}/pkgconfig/atk.pc

%files doc
%defattr(-,root,other)
%doc %{_datadir}/gtk-doc/*

%changelog
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
