Summary:	Beep Media Player 
Name:		bmp
Version:	0.9.7.1
Release:        2
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	libvorbis libogg gtk2 id3lib

%description
BMP is an audio player that tries to maintain a stable audio playback 
core with a powerful, yet easy-to-use remote API using DBus, while also 
providing a skinned, yet easy and understandable user interface with the 
core GUI.

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
/usr/local/lib/*
#/usr/local/lib/*so*
#/usr/local/lib/bmp/Input/*so
#/usr/local/lib/bmp/Output/*so
#/usr/local/lib/bmp/Visualization/*so
/usr/local/share/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Wed Mar 01 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.7.1-1
- Initial Rutgers release
