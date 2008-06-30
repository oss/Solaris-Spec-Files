Summary:	libvorbis - Library to for the Ogg Vorbis audio format
Name:		libvorbis
Version:	1.2.0
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
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local
gmake

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README CHANGES AUTHORS COPYING
%dir /usr/local/share/doc/libvorbis-%{version}/
/usr/local/include/*
/usr/local/lib/*
/usr/local/share/aclocal/vorbis.m4
/usr/local/share/doc/libvorbis-%{version}/*

%changelog
* Mon Jun 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.2.0-1
- Added changelog and updated to version 1.2.0
