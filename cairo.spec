Summary:	2D Graphics Library
Name:		cairo
Version:	1.6.4
Release:	1
License:	GPL
Group:		Development/Libraries
Source:        %{name}-%{version}.tar.gz
URL:		http://cairographics.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
Requires:	poppler pixman
BuildRequires:	autoconf automake poppler-devel pixman-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Cairo is a 2D graphics library with support for multiple output devices. 
Currently supported output targets include the X Window System, win32, and 
image buffers. Experimental backends include OpenGL (through glitz), 
Quartz, XCB, PostScript and PDF file output.

%package devel
Summary: Libraries, includes to develop applications with %{name}. 
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel 
The %{name}-devel package contains the header files and 
static libraries for building applications which use %{name}. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix=/usr/local \
	--enable-xlib=yes \
	--enable-xlib-xrender=yes \
	--enable-png=yes \
	--enable-freetype=yes \
	--enable-pdf=yes \
	--enable-svg=no
#####################################################
# NOTE: You can not have svg enabled without creating
# a serious dependency loop for gtk. By doing this
# librsvg and cairo both depend on each other and apt
# becomes quickly confused (insane)
#####################################################
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/lib/libcairo*so*

%files devel
%defattr(0755,root,root) 
/usr/local/share/* 
/usr/local/include/* 
/usr/local/lib/pkgconfig/*
/usr/local/lib/libcairo.a
/usr/local/lib/libcairo.la

%changelog
* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.4-1
- Added pixman requirement and pixman-devel build requirement
- Updated to version 1.6.4
* Wed Aug 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10-2
- Removing librsvg dependency and support
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.10-1
- Bump to 1.4.10
* Mon Jan 29 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.6-1
- Updated to latest version and added 8 bit fix

* Tue Aug 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.2-2
- Updated to latest version and enabled poppler support

* Fri Dec 02 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.2-2
- Split into regular and devel packages

* Thu Dec 01 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.2-1
 - Initial Rutgers release
