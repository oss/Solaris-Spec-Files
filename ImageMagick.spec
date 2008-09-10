%define im_ver 6.4.3_6
%define realversion 6.4.3-6
%define shortversion 6.4.3

Summary: 	Image manipulation library
Name: 		ImageMagick
Version: 	%{im_ver}
Release: 	1
Group: 		Development/Libraries
License: 	Freely distributable
Source: 	ImageMagick-%{realversion}.tar.gz
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	libpng3 libjpeg libtiff gs bzip2
BuildRequires: 	libpng3-devel libjpeg-devel libtiff-devel gs bzip2

%description
ImageMagick is an image manipulation library.

%package devel
Summary:	ImageMagick header files and static libraries
Group:		Development/Libraries
Requires:	ImageMagick = %{version}-%{release}

%description devel
ImageMagick-devel contains the ImageMagick headers and static libraries.

%package doc
Summary:	ImageMagick documentation
Group:		Development/Libraries
Requires:	ImageMagick = %{version}-%{release}
 	
%description doc
This package consists of in-depth documentation for ImageMagick.

%prep
%setup -q -n %{name}-%{shortversion}

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LD="/usr/ccs/bin/ld" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure --prefix=/usr/local \
   --mandir=/usr/local/man --enable-static --without-perl 

gmake -j3

%install
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

# Remove libtool .la files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/ImageMagick-%{shortversion}/modules-Q16/coders/*.la
rm -f %{buildroot}%{_libdir}/ImageMagick-%{shortversion}/modules-Q16/filters/analyze.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%{_bindir}/*
%{_libdir}/*.so*
%dir %{_libdir}/ImageMagick-%{shortversion}
%{_libdir}/ImageMagick-%{shortversion}/config
%dir %{_libdir}/ImageMagick-%{shortversion}/modules-Q16
%dir %{_libdir}/ImageMagick-%{shortversion}/modules-Q16/coders
%{_libdir}/ImageMagick-%{shortversion}/modules-Q16/coders/*.so
%dir %{_libdir}/ImageMagick-%{shortversion}/modules-Q16/filters
%{_libdir}/ImageMagick-%{shortversion}/modules-Q16/filters/analyze.so
%dir %{_datadir}/ImageMagick-%{shortversion}
%doc %{_datadir}/ImageMagick-%{shortversion}/ChangeLog
%doc %{_datadir}/ImageMagick-%{shortversion}/LICENSE
%doc %{_datadir}/ImageMagick-%{shortversion}/NEWS.txt
%{_datadir}/ImageMagick-%{shortversion}/config
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/ImageMagick
%{_libdir}/*.a
%{_libdir}/ImageMagick-%{shortversion}/modules-Q16/coders/*.a
%{_libdir}/ImageMagick-%{shortversion}/modules-Q16/filters/analyze.a
%{_libdir}/pkgconfig/*

%files doc
%defattr(-,root,root)
%doc %{_datadir}/doc/ImageMagick-%{shortversion}

%changelog
* Wed Sep 10 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 6.4.3-1
- Fixed some things, added doc package, changed to use Sun cc, bumped
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 6.4.1-1
- bumped, added -fpic
* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 6.3.6-1
- Updated to 6.3.6
* Wed Jun 20 2007 Kevin Mulvey <kmulvey@nbcs.rutgers.edu> - 6.3.4-10
- Updated to 6.3.4
