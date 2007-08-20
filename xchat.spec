%include perl-header.spec

Summary:	Multiplatform Chat Program
Name:		xchat
Version:	2.8.4
Release:        3
Copyright:	GPL
Group:		System Environment/Libraries
Source:		%{name}-%{version}.tar.bz2
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk2, tcl, python >= 2.4, openssl >= 0.9.8
BuildRequires:	gtk2-devel, tcl-headers, python >= 2.4, openssl >= 0.9.8

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
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lposix4" \
PERLPATH="/usr/perl5" \
export PATH CC CXX CPPFLAGS LD LDFLAGS PERLPATH

./configure --prefix=/usr/local --enable-python \
--enable-tcl=/usr/local/lib --enable-openssl=/usr/local/ssl \
--enable-perl --enable-shm --disable-dbus --enable-ipv6

for i in `find . -name Makefile`; do mv $i $i.wrong; sed -e 's/-lutil//g' $i.wrong > $i; rm $i.wrong; done

mv src/common/msproxy.h src/common/msproxy.h.wrong

sed -e 's/data\[0\]/data\[1\]/g' src/common/msproxy.h.wrong > src/common/msproxy.h

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
/usr/local/lib/xchat/plugins/*.so*

%changelog
* Mon Aug 20 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.8.4-3
- Updated to 2.8.4-3
* Thu Jun 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.6.8-2
- Updated to 2.8.2
* Thu Dec 07 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.8-2
- Updated for OpenSSL 0.9.8
* Wed Nov 15 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.8-1
- Updated to 2.6.8
* Tue Jun 13 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.4-1
- Updated to 2.6.4, enabled IPv6
* Wed May 31 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.2-2
- Enable python, tcl and perl plugin support
* Tue Apr 04 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.1-1
- Updated to version 2.6.2
* Mon Feb 27 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.6.1-1
- Initial Rutgers release
