Name:		gstreamer
Version:	0.10.23
Release:        1
License:	GPL
Group:		Applications/Libraries
Source:		http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.gz
URL:		http://gstreamer.freedesktop.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}root

BuildRequires:  liboil-devel >= 0.3.15, libxml2-devel
Requires:	liboil >= 0.3.15

Obsoletes:	gstreamer-static

Summary:        GStreamer Audio Library

%description
GStreamer is a library that allows the construction of graphs of 
media-handling components, ranging from simple Ogg/Vorbis playback to 
complex audio (mixing) and video (non-linear editing) processing.
Applications can take advantage of advances in codec and filter 
technology transparently. Developers can add new codecs and filters by 
writing a simple plugin with a clean, generic interface.
GStreamer is released under the LGPL.

%package devel 
Group:		Applications/Libraries
Requires:	gstreamer = %{version}-%{release}
Summary:	gstreamer development files

%description devel
This package contains files needed for building applications that 
use gstreamer.

%package doc
Group:          Applications/Libraries
Requires:       gstreamer = %{version}-%{release}
Summary:        gstreamer documentation

%description doc
This package contains the gtk-doc documentation for gstreamer.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix} 	\
	--mandir=%{_mandir} 	\
	--disable-static	\
	--disable-nls

gmake

%install
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" 
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LDFLAGS

gmake install DESTDIR=%{buildroot}

chmod -R 755 %{buildroot}/usr/local/lib/gstreamer*

find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog 
%doc NEWS README RELEASE
%{_bindir}/*
%{_libdir}/*so*
%{_libdir}/gstreamer-0.10
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*

%files doc
%defattr(-, root, root)
%docdir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/*

%changelog
* Tue May 26 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.10.23-1
- Updated to version 0.10.23
- No longer build static libraries
- Added doc package
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.10.20-1
- Made a few minor changes, bumped to 0.10.20
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbs.rutgers.edu> -0.10.5-5
- built against liboil 0.3.15, added doc, switched to gmake, added static subpackage
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.5-1
- Initial Rutgers release
