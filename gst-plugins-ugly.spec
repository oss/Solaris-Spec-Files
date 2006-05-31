Summary:	a set of good-quality GStreamer plug-ins not under our preferred license, LGPL
Name:		gst-plugins-ugly
Version:	0.10.3
Release:        2
Copyright:	Questionable
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gstreamer, liboil, libmad, libid3tag
BuildRequires:	gstreamer-devel, liboil-devel, libmad-devel, libid3tag-devel

%description
Gstreamer Ugly Plug-ins is a set of plug-ins that have good quality and 
correct functionality, but distributing them might pose problems. The 
license on either the plug-ins or the supporting libraries might not be 
how we'd like.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-nls

mv gst/mpegstream/gstmpegdemux.c gst/mpegstream/gstmpegdemux.c.wrong

sed -e 's/__FUNCTION__/__func__/' gst/mpegstream/gstmpegdemux.c.wrong > gst/mpegstream/gstmpegdemux.c

#for i in `find . -name Makefile` ; do mv $i $i.wrong ; sed -e 's/-mt//g' $i.wrong > $i ; done

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/lib/gstreamer-0.10/*.so
/usr/local/lib/gstreamer-0.10/*so

%changelog
* Tue May 02 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.10.3-1
- Initial Rutgers release
