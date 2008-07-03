Summary:	PDF rendering library
Name:		poppler
Version:	0.8.4
Release:        1
Copyright:	GPL
Group:		System/Libraries
Source:		%{name}-%{version}.tar.gz
Patch:		poppler-0.8.4.patch
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
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
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/include -I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-utils --enable-zlib

gmake

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc README* NEWS COPYING AUTHORS ChangeLog
%doc /usr/local/share/gtk-doc
%defattr(-,bin,bin)
/usr/local/lib/*.so*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*
/usr/local/lib/*.a
/usr/local/lib/*.la

%changelog
* Thu Jul 03 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.8.4-1
- Updated to version 0.8.4
* Tue Oct 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.5.4-1
- New version, fixed conflicts with xpdf package
* Tue Aug 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.4.5-1
- Initial Rutgers release
