Summary:	nethack - game
Name:		nethack
Version:	3.4.3
Release:        1
Copyright:	GPL
Group:		Applications/Games
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
NetHack is a single player dungeon exploration game that runs on a wide 
variety of computer systems. But that's a very dry description. See the 
Guidebook for much more information, including the game commands.

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

make all

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/local/share/locale/locale.alias

chmod -R 755 $RPM_BUILD_ROOT/usr/local/lib/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/libexec/beep-media-player-2-bin
/usr/local/lib/*.so
/usr/local/lib/*so*
/usr/local/lib/bmp-2.0/plugins/container/*.so
/usr/local/lib/bmp-2.0/plugins/container/*so*
/usr/local/lib/bmp-2.0/plugins/flow/*.so
/usr/local/lib/bmp-2.0/plugins/flow/*so*
/usr/local/lib/bmp-2.0/plugins/transport/*.so
/usr/local/lib/bmp-2.0/plugins/transport/*so*
/usr/local/share/*
/usr/local/man/man1/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Tue May 23 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 3.4.3-1
- Initial Rutgers release
