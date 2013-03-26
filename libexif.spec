Summary:	libexif
Name:		libexif
Version:	0.6.13
Release:        2
Copyright:	GPL
Group:		System/Libraries
Source:		%{name}-%{version}.tar.bz2
Patch:		libexif.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
LibEXIF:
* is a library written in pure C.
* reads and writes EXIF metainformation from and to image files.
* is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 
(LGPL).
* runs under POSIX systems (e.g. GNU/Linux, xBSD, MacOS X, etc.) and 
Win32. Win64 untested.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/*.so*
/usr/local/share/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Tue Feb 12 2013 Kaitlin Poskaitis <katiepru@nbcs.rutgers.edu> - 0.6.13-2
- Release bump for testing
* Tue Aug 29 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.6.13-1
- Initial Rutgers release
