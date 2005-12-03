Summary:	2D Graphics Library
Name:		cairo
Version:	1.0.2
Release:	3
License:	GPL
Group:		Development/Libraries
Source0:        %{name}-%{version}.tar.gz
Patch0:		cairo-xlib-fix.patch
URL:		http://cairographics.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRequires:	autoconf automake
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
static libraries for building applications which use {%name}. 

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

## VERY IMPORTANT ##
# In order to make this package build, I had to copy over the ld and as
# binaries in /usr/local/gnu/bin to /usr/ccs/bin, overwriting the solaris
# ones, as flags to make it use the correct linker and assembler did not 
# work. Make sure you back up everything you overwrite, and don't forget 
# to put it all back after the package is built.
## VERY IMPORTANT ##
 
%build
LDFLAGS="-L/usr/sfw/lib:/usr/local/lib -R/usr/sfw/lib:/usr/local/lib -mimpure-text"
CC="gcc"
AS="/usr/local/gnu/bin/as"
CFLAGS="-O2"
PATH="/usr/local/gnu/bin:/usr/local/lib:/usr/sfw/bin:$PATH"
export LDFLAGS CC AS CFLAGS PATH

./configure \
	--prefix=/usr/local

make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/lib/libcairo*

%files devel
%defattr(0755,root,root) 
/usr/local/share/* 
/usr/local/include/* 
/usr/local/lib/pkgconfig/*

%changelog
* Fri Dec 02 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.2-2
- Split into regular and devel packages

* Thu Dec 01 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.2-1
 - Initial Rutgers release
