Summary:	Multiplatform Chat Program
Name:		xchat
Version:	2.6.2
Release:        1
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root

%description
XChat is an IRC (chat) program for Windows and UNIX (Linux/BSD) 
operating systems. I.R.C. is Internet Relay Chat, see http://irchelp.org 
for more information about IRC in general. XChat runs on most BSD and 
POSIX compliant operating systems, and has been reported to work on, at 
least:

    * GNU-Linux
    * FreeBSD
    * NetBSD
    * OpenBSD
    * Solaris
    * AIX
    * IRIX
    * DEC/Compaq Tru64 UNIX
    * HP-UX 10.20 and 11
    * MacOS X
    * Windows 98/ME/NT/2000/XP

XChat is a graphical IRC client. It runs under the X Window System and 
uses the GTK+ toolkit. Optionally it can be compiled to use Gnome. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --disable-python \
--enable-perl --disable-tcl --enable-openssl=/usr/local/ssl \
--disable-nls 
make

%install
rm -rf $RPM_BUID_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/share/*

%changelog
* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.1-1
- Updated to version 2.6.2
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.1-1
- Initial Rutgers release
