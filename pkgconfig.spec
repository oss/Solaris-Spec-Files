Summary:	pkg-config
Name:		pkgconfig
Version:	0.22
Release:	1
Source:		pkg-config-%{version}.tar.gz
Copyright:	GPL
Group:		Libraries
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root

%description
pkgconfig

%prep
%setup -q -n pkg-config-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls --disable-rebuilds

%install
rm -rf $RPM_BUILD_ROOT

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/bin/pkg-config
/usr/local/share/man/man1/pkg-config.1
/usr/local/share/aclocal/pkg.m4

%changelog
* Thu Aug 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.22-1
- Bumped 0.22
* Wed Aug 16 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.21-1
- Switched to Sun CC
* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.20-1
- Updated to version 0.20
