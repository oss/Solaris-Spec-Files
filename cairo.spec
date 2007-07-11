Summary:	2D Graphics Library
Name:		cairo
Version:	1.4.10
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:        %{name}-%{version}.tar.gz
#Patch0:		cairo-xlib-fix.patch
#Patch1:		cairo-02-8bit-fix.diff
URL:		http://cairographics.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
Requires:	librsvg, poppler
BuildRequires:	autoconf automake librsvg-devel, poppler-devel
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
%setup -q -n %{name}-%{version}
#%patch0 -p1

## VERY IMPORTANT ##
# In order to make this package build, I had to copy over the ld and as
# binaries in /usr/local/gnu/bin to /usr/ccs/bin, overwriting the solaris
# ones, as flags to make it use the correct linker and assembler did not 
# work. Make sure you back up everything you overwrite, and don't forget 
# to put it all back after the package is built.
## VERY IMPORTANT ##
 
%build
#LDFLAGS="-L/usr/sfw/lib:/usr/local/lib -R/usr/sfw/lib:/usr/local/lib -mimpure-text"
#CC="gcc"
#AS="/usr/local/gnu/bin/as"
#CFLAGS="-O2"
#PATH="/usr/local/gnu/bin:/usr/local/lib:/usr/sfw/bin:$PATH"
#export LDFLAGS CC AS CFLAGS PATH

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
	--enable-svg=yes

make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/lib/libcairo*so*

%files devel
%defattr(0755,root,root) 
/usr/local/share/* 
/usr/local/include/* 
/usr/local/lib/pkgconfig/*

%changelog
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
