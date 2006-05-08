Summary:	SDL - Simple Directmedia Layer
Name:		SDL
Version:	1.2.9
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Simple DirectMedia Layer is a cross-platform multimedia library 
designed to provide low level access to audio, keyboard, mouse, 
joystick, 3D hardware via OpenGL, and 2D video framebuffer. It is used 
by MPEG playback software, emulators, and many popular games, including 
the award winning Linux port of "Civilization: Call To Power."

Simple DirectMedia Layer supports Linux, Windows, BeOS, MacOS Classic, 
MacOS X, FreeBSD, OpenBSD, BSD/OS, Solaris, IRIX, and QNX. There is also 
code, but no official support, for Windows CE, AmigaOS, Dreamcast, 
Atari, NetBSD, AIX, OSF/Tru64, RISC OS, and SymbianOS.

SDL is written in C, but works with C++ natively, and has bindings to 
several other languages, including Ada, Eiffel, Java, Lua, ML, Pascal, 
Perl, PHP, Pike, Python, and Ruby. 

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
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC

./configure --prefix=/usr/local

make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/lib/*so
/usr/local/lib/*so*
/usr/local/man/man3/*

%files devel
%defattr(-,root,root)
/usr/local/share/*
/usr/local/include/*

%changelog
* Sun Feb 26 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.2.9-1
- Initial Rutgers release

