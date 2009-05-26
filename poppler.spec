Name:		poppler
Version:	0.10.7
Release:        1
License:	GPL
Group:		Applications/Libraries
Source:		http://poppler.freedesktop.org/poppler-%{version}.tar.gz
URL:		http://poppler.freedesktop.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	libjpeg
BuildRequires:	libjpeg-devel zlib-devel

Summary:        PDF rendering library

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package devel 
Group:		Applications/Libraries
Requires: 	poppler = %{version}-%{release}
Summary:	Development files for poppler

%description devel
This package contains the files needed to build applications
that use poppler.

%package doc
Group:          Applications/Libraries
Requires:       poppler = %{version}-%{release}
Summary:    	Additional poppler documentation

%description doc
This package contains the gtk-doc documentation for poppler.

%prep
%setup -q
%{__sed} -i '/gtkdoc-rebase/d' glib/reference/Makefile.in

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/include -D__EXTENSIONS__" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix} 	\
	--mandir=%{_mandir}	\
	--disable-utils 	\
	--disable-static	\
	--enable-zlib		

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README* NEWS COPYING AUTHORS ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%defattr(-, root, root)
%doc %{_datadir}/gtk-doc/*

%changelog
* Tue May 26 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.10.7-1
- Updated to version 0.10.7
- No longer build static libraries
- Added doc package
* Thu Jul 03 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.8.4-1
- Updated to version 0.8.4
* Tue Oct 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.5.4-1
- New version, fixed conflicts with xpdf package
* Tue Aug 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.4.5-1
- Initial Rutgers release
