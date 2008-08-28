Summary:	GStreamer Audio Library
Name:		gstreamer
Version:	0.10.20
Release:        1
License:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	liboil >= 0.3.15, libxml2
BuildRequires:	liboil-devel >= 0.3.15, libxml2-devel

%description
GStreamer is a library that allows the construction of graphs of 
media-handling components, ranging from simple Ogg/Vorbis playback to 
complex audio (mixing) and video (non-linear editing) processing.
Applications can take advantage of advances in codec and filter 
technology transparently. Developers can add new codecs and filters by 
writing a simple plugin with a clean, generic interface.
GStreamer is released under the LGPL.

%package devel 
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files 
for building applications which use %{name}.

%package static
Summary: Static libraries
Group: Applications/Libraries
Requires: %{name} = %{version}

%description static
The %{name}-static package containts the static libraries
for building applications with %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=%{_prefix} --mandir=%{_mandir} --disable-nls

gmake

%install
rm -rf %{buildroot}

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake install DESTDIR=%{buildroot}

chmod -R 755 %{buildroot}/usr/local/lib/gstreamer*

rm -f %{buildroot}/usr/local/lib/*.la
rm -f %{buildroot}/usr/local/lib/gstreamer-0.10/*.la

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog NEWS README RELEASE
%defattr(-,bin,bin)
%{_bindir}/*
%{_libdir}/*so*
%dir %{_libdir}/gstreamer-0.10
%{_libdir}/gstreamer-0.10/*.so
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/gst-element-check-0.10.m4
%docdir %{_datadir}/gtk-doc/html/gstreamer-0.10
%docdir %{_datadir}/gtk-doc/html/gstreamer-libs-0.10
%docdir %{_datadir}/gtk-doc/html/gstreamer-plugins-0.10
%{_datadir}/gtk-doc/html/*

%files static
%defattr(-,bin,bin)
%{_libdir}/*.a
%{_libdir}/gstreamer-0.10/*.a

%changelog
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.10.20-1
- Made a few minor changes, bumped to 0.10.20
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbs.rutgers.edu> -0.10.5-5
- built against liboil 0.3.15, added doc, switched to gmake, added static subpackage
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.5-1
- Initial Rutgers release
