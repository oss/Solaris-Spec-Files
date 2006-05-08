Summary:	library for reading and writing files containing sampled sound
Name:		libsndfile
Version:	1.0.14
Release:        2
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.gz
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
Libsndfile is a C library for reading and writing files containing 
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format) 
through one standard library interface. It is released in source code 
format under the Gnu Lesser General Public License.

The library was written to compile and run on a Linux system but should 
compile and run on just about any Unix (including MacOSX). It can also 
be compiled and run on Win32 systems using the Microsoft compiler and 
MacOS (OS9 and earlier) using the Metrowerks compiler. There are 
directions for compiling libsndfile on these platforms in the Win32 and 
MacOS directories of the source code distribution.

It was designed to handle both little-endian (such as WAV) and 
big-endian (such as AIFF) data, and to compile and run correctly on 
little-endian (such as Intel and DEC/Compaq Alpha) processor systems as 
well as big-endian processor systems such as Motorola 68k, Power PC, 
MIPS and Sparc. Hopefully the design of the library will also make it 
easy to extend for reading and writing new sound file formats.

It has been compiled and tested (at one time or another) on the 
following systems:

    * i586-pc-linux-gnu (Linux on PC hardware)
    * powerpc-unknown-linux-gnu (Linux on Apple Mac hardware)
    * powerpc-apple-darwin7.0 (Mac OS X 10.3)
    * sparc-sun-solaris2.8 (using gcc)
    * mips-sgi-irix5.3 (using gcc)
    * QNX 6.0
    * i386-unknown-openbsd2.9
    * Win32 (Microsoft Visual C++) 

At the moment, each new release is being tested on i386 Linux, PowerPC 
Linux, MacOSX on PowerPC and Win32. 

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
CC="gcc" CXX="g++"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CXX

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
/usr/local/man/man1/*
/usr/local/share/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.14-1
- Initial Rutgers release
