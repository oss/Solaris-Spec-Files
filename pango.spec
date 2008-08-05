Name:		pango
Version:	1.20.5
Release:	1
License:	LGPL
Group:		System Environment/Libraries
Source0:	%{name}-%{version}.tar.bz2
Source1:	pango.modules
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
Summary:	System for layout and rendering of internationalized text.
BuildRoot:	%{_tmppath}/%{name}-root
# -assuming system has necessary X libraries pre-installed
Requires:	cairo >= 1.4.10
Requires:	glib2 >= 2.14.0
Requires:	fontconfig >= 2.4.2
Requires:	freetype2 >= 2.3.5
Requires:	xft2 >= 2.1.7
Requires:	libpng3 >= 1.2.8-3
BuildRequires:	cairo-devel >= 1.4.10
BuildRequires:	libtool >= 1.5.24
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	pkgconfig >= 0.22
BuildRequires:	freetype2-devel >= 2.3.5
BuildRequires:	xft2-devel >= 2.1.7
BuildRequires:	libpng3-devel >= 1.2.8-3
BuildRequires:	fontconfig-devel >= 2.4.2

%description
Pango is a system for layout and rendering of internationalized text.

%package devel
Summary: System for layout and rendering of internationalized text.
Requires: %{name} = %{version}
Requires: glib2-devel >= 2.14.0
Requires: freetype2-devel >= 2.3.5
Group: Development/Libraries
%description devel
The pango-devel package includes the header files and
developer docs for the pango package.

%package doc
Summary: %{name} extra documentation
Requires: %{name} = %{version}
Group: Documentation
%description doc
%{name} extra documentation

%prep
%setup -q -n %{name}-%{version}

%build

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-g -xs -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

# --diable-gtk-doc just copies over existing documentation files, instead of creating new ones
./configure \
	--prefix=/usr/local \
	--disable-nls \
	--disable-rebuilds \
	--disable-gtk-doc
gmake -j3

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/pango
gmake install DESTDIR=$RPM_BUILD_ROOT
# Remove files that should not be packaged
rm $RPM_BUILD_ROOT/usr/local/lib/pango/1.6.0/modules/*.la
rm $RPM_BUILD_ROOT/usr/local/lib/*.la
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/local/etc/pango/pango.modules
chmod 644 $RPM_BUILD_ROOT/usr/local/etc/pango/pango.modules

%clean
rm -rf $RPM_BUILD_ROOT

%post
# This is so things built on the old pango don't freak out
# rm -rf /usr/local/lib/pango/1.4.0
# ln -s /usr/local/lib/pango/1.5.0 /usr/local/lib/pango/1.4.0

%files
%doc AUTHORS COPYING ChangeLog HACKING INSTALL MAINTAINERS NEWS README THANKS
%defattr(755,root,other)
/usr/local/bin/pango-view
/usr/local/etc/pango/pangox.aliases
/usr/local/etc/pango/pango.modules
/usr/local/bin/pango-querymodules
/usr/local/lib/libpango*.so*
/usr/local/lib/pango/1.6.0/modules/*
/usr/local/share/man/man1/pango-querymodules.1

%files devel
%defattr(-,root,other)
/usr/local/include/pango-1.0/pango/*
/usr/local/lib/pkgconfig/*

%files doc
%defattr(-,root,other)
/usr/local/share/gtk-doc/html/pango/*

%changelog
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
