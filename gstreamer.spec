Summary:	GStreamer Audio Library
Name:		gstreamer
Version:	0.10.5
Release:        5
Copyright:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

gmake

%install
rm -rf $RPM_BUID_ROOT

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

gmake install DESTDIR=$RPM_BUILD_ROOT

chmod -R 755 $RPM_BUILD_ROOT/usr/local/lib/gstreamer*

rm -f %{buildroot}/usr/local/lib/*.la
rm -f %{buildroot}/usr/local/lib/gstreamer-0.10/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README RELEASE TODO
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*.so
/usr/local/lib/*so*
/usr/local/lib/gstreamer-0.10/*.so
/usr/local/share/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files static
%defattr(-,bin,bin)
/usr/local/lib/*.a
/usr/local/lib/gstreamer-0.10/*.a

%changelog
* Tue Aug 26 2008 David Diffenbaugh <davediff@nbs.rutgers.edu> -0.10.5-5
- built against liboil 0.3.15, added doc, switched to gmake, added static subpackage
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.5-1
- Initial Rutgers release
