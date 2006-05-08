Summary:	GStreamer Audio Library
Name:		gstreamer
Version:	0.10.5
Release:        3
Copyright:	GPL
Group:		Libraries/System
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	liboil, libxml2
BuildRequires:	liboil-devel, libxml2-devel

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

./configure --prefix=/usr/local --disable-nls

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
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

%changelog
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.5-1
- Initial Rutgers release
