Summary:	libvorbis - Library to for the Ogg Vorbis audio format
Name:		libvorbis
Version:	1.1.2
Release:        1
Copyright:	BSD
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root
BuildRequires:	libogg
Requires:	libogg

%description
Vorbis is a general purpose audio and music encoding format
contemporary to MPEG-4's AAC and TwinVQ, the next generation beyond
MPEG audio layer 3. Unlike the MPEG sponsored formats (and other
proprietary formats such as RealAudio G2 and Windows' flavor of the
month), the Vorbis CODEC specification belongs to the public domain.
All the technical details are published and documented, and any
software entity may make full use of the format without license 
fee, royalty or patent concerns.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%dir /usr/local/share/doc/libvorbis-%{version}/
/usr/local/include/*
/usr/local/lib/*
/usr/local/share/aclocal/vorbis.m4
/usr/local/share/doc/libvorbis-%{version}/*

