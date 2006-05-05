Summary:	contains one plugin with a set of elements using the FFmpeg library code
Name:		gst-ffmpeg
Version:	0.10.1
Release:        1
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
GStreamer FFmpeg plug-in contains one plugin with a set of elements 
using the FFmpeg library code. It contains most popular decoders as well 
as very fast colorspace conversion elements.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LD_LIBRARY_PATH="/usr/local/lib"
LD_RUN_PATH="/usr/local/lib"
CC="gcc"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

./configure --prefix=/usr/local --disable-nls

for i in `find . -name Makefile` ; do mv $i $i.wrong ; sed -e 's/-mt //g' $i.wrong > $i ; done

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/gstreamer-0.10/*.so
/usr/local/lib/gstreamer-0.10/*so*

%changelog
* Tue May 02 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.1-1
- Initial Rutgers release
