Summary:	A pixel manipulation library
Name:		pixman
Version:	0.13.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source:         %{name}-%{version}.tar.gz
URL:		http://cairographics.org
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRequires:	autoconf automake libtool pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The pixel manipulation library for X and cairo.

%package devel
Summary:	Pixman development files  
Group:		Applications/Libraries
Requires:	pixman = %{version}-%{release}

%description devel 
This package contains the header files, etc. needed for 
building applications which use pixman. 

%prep
%setup -q
 
%build
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=%{_prefix} --disable-static
gmake

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libpixman-1.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO ChangeLog
%{_libdir}/libpixman-1.so.*

%files devel
%defattr(-,root,root) 
%{_includedir}/pixman-1
%{_libdir}/libpixman-1.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
* Mon Feb 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.13.2-1
- Updated to version 0.13.2
- No longer build static libraries
- Removed patch (no longer needed)
* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.11.4-1
- Initial release, needed for new version of cairo.
