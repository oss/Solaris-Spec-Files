Summary:	PDF rendering library
Name:		poppler
Version:	0.5.4
Release:        1
Copyright:	GPL
Group:		System/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	libjpeg
BuildRequires:	libjpeg-devel

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-utils --enable-zlib

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
* Tue Oct 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.5.4-1
- New version, fixed conflicts with xpdf package
* Tue Aug 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.4.5-1
- Initial Rutgers release
