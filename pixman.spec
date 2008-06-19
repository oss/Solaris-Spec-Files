Summary:	A pixel manipulation library
Name:		pixman
Version:	0.11.4
Release:	1
License:	MIT
Group:		Development/Libraries
Source:         %{name}-%{version}.tar.gz
Patch:          pixman-solaris9.patch
URL:		http://cairographics.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRequires:	autoconf automake libtool pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
The pixel manipulation library for X and cairo.

%package devel
Summary: Libraries, includes to develop applications with %{name}. 
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel 
The %{name}-devel package contains the header files and 
static libraries for building applications which use %{name}. 

%prep
%setup -q
%patch -p1
 
%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix="/usr/local"
gmake

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
/usr/local/lib/libpixman-1.so.*

%files devel
%defattr(-,root,root) 
%dir /usr/local/include/pixman-1
/usr/local/include/pixman-1/pixman.h
/usr/local/include/pixman-1/pixman-version.h 
/usr/local/lib/libpixman-1.so
/usr/local/lib/libpixman-1.a
/usr/local/lib/libpixman-1.la
/usr/local/lib/pkgconfig/pixman-1.pc

%changelog
* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.11.4-1
- Initial release, needed for new version of cairo.
