Summary:	An eseential set of GStreamer plugins
Name:		gst-plugins-base
Version:	0.10.6
Release:        3
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gstreamer, liboil
BuildRequires:	gstreamer-devel, liboil-devel

%description
GStreamer Base Plug-ins is a well-groomed and well-maintained collection 
of GStreamer plug-ins and elements, spanning the range of possible types 
of elements one would want to write for GStreamer. It also contains 
helper libraries and base classes useful for writing elements. A wide 
range of video and audio decoders, encoders, and filters are included.

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
/usr/local/lib/gstreamer-0.10/*.so
/usr/local/lib/gstreamer-0.10/*so*
/usr/local/lib/*.so
/usr/local/lib/*so*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Fri Apr 28 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.6-1
- Initial Rutgers release
