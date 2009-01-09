Summary:	An antivirus for Unix
Name:		clamav
Version:	0.94.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:        %{name}-%{version}.tar.gz
URL:		http://clamav.sf.net/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager:  	David Diffenbaugh <davediff@nbcs.rutgers.edu>	
Requires:	gmp
BuildRequires:	autoconf automake gmp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Clam AntiVirus is an powerful anti-virus toolkit for Unix.
The package provides a flexible and scalable multi-threaded daemon,
a command line scanner, and a tool for automatic updating via Internet.
It supports AMaViS, Sendmail milter, compressed files and mbox format.
Clamav is multithreaded, written in C, and POSIX compliant.

%package static
Summary: ClamAV static libraries
Group: Development/Libraries
Requires: %{name} = %{version}

%description static
ClamAV's static libraries (the .a files), which you don't need unless
you are building executables with static libraries.  Why would someone do
that?  I do not know.

%prep
%setup -q -n %{name}-%{version}

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" \
CC="cc" CXX="CC" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/include/gmp32" \
PKG_CONFIG_PATH="/usr/local/lib/pkgconfig:/usr/local/ssl/lib/pkgconfig" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LDFLAGS PKG_CONFIG_PATH

./configure \
	--enable-id-check \
	--disable-clamav \
	--with-user=clamav \
	--with-group=clamav \
	--with-dbdir=%{_localstatedir}/lib/clamav \
	--sysconfdir=/etc

gmake -j3

%install
rm -rf $RPM_BUILD_ROOT

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" \
CC="cc" CXX="CC" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include -I/usr/local/include/gmp32" \
PKG_CONFIG_PATH="/usr/local/lib/pkgconfig:/usr/local/ssl/lib/pkgconfig" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LDFLAGS PKG_CONFIG_PATH

gmake install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/etc/clamd.conf $RPM_BUILD_ROOT/etc/clamd.conf.example
mv $RPM_BUILD_ROOT/etc/freshclam.conf $RPM_BUILD_ROOT/etc/freshclam.conf.example

rm $RPM_BUILD_ROOT/usr/local/lib/libclamav.la  # Rid the evil
rm $RPM_BUILD_ROOT/usr/local/lib/libclamunrar.la
rm $RPM_BUILD_ROOT/usr/local/lib/libclamunrar_iface.la

%clean
rm -rf $RPM_BUILD_ROOT

# Not done at Rutgers.
#%pre
#	/usr/sbin/groupadd -g 46 -r -f clamav
#	/usr/sbin/useradd -u 46 -r -d /tmp  -s /sbin/nologin -c "Clam AV Checker" -g clamav clamav 1>&2

%post

cat <<EOF

To complete installation, make sure you create some sort of clamav user and group.

*** ATTENTION *** As of version 0.90, the configuration file format 
has changed *** ATTENTION ***

EOF

%files
%defattr(-,root,bin)
%doc AUTHORS BUGS COPYING ChangeLog FAQ INSTALL NEWS README docs/html/
%attr(0755,root,bin) %{_bindir}/*
%attr(0755,root,bin) %{_sbindir}/clamd
%attr(0755,root,bin) %{_includedir}/clamav.h
%attr(0755,root,bin) %{_libdir}/libclamav.so*
%attr(0755,root,bin) %{_libdir}/libclamunrar.so*
%attr(0755,root,bin) %{_libdir}/libclamunrar_iface.so*
%attr(0755,root,bin) /etc/clamd.conf.example
%attr(0755,root,bin) /etc/freshclam.conf.example
%attr(0755,root,bin) %dir %{_localstatedir}/lib/clamav/
%attr(0644,root,bin) %{_libdir}/pkgconfig/libclamav.pc
%config(noreplace) %attr(0644,root,bin) %{_localstatedir}/lib/clamav/main.cvd
%config(noreplace) %attr(0644,root,bin) %{_localstatedir}/lib/clamav/daily.cvd
/usr/local/share/man/*

%files static
%defattr(-,root,bin)
%attr(0755,root,bin) %{_libdir}/libclamav.a
%attr(0755,root,bin) %{_libdir}/libclamunrar.a
%attr(0755,root,bin) %{_libdir}/libclamunrar_iface.a

%changelog
* Wed Nov 26 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.94.2-1
- updated to latest release
* Mon Sep 08 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.94-1
- updated to latest release
* Mon Jul 07 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.93.3-1
- bumped
* Wed Jun 11 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.93.1-1
- bumped to 0.93.1
* Tue Apr 15 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.93-1
- updated to 0.93, changed to Sun CC
* Wed Feb 13 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.92.1-1
- updated to 0.92.1
* Mon Dec 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.92-1
 - Bump to 0.92
* Tue Aug 21 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 0.91.2-1
 - updated to 0.91.2
* Tue Jul 17 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 0.91.1-1
 - updated to 0.91.1
* Wed Jul 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.91-1
 - Updated to 0.91
* Thu May 31 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.90.3-1
 - Updated to 0.90.3
* Thu Apr 12 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.90.2-1
 - Updated to 0.90.2
* Fri Mar 02 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.90.1-1
 - Updated to 0.90.1
* Fri Feb 23 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.90-1
 - Updated to 0.90
* Mon Nov  6 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Updated to 0.88.6
* Fri Oct 20 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.88.5-1
 - Updated to 0.88.5
* Wed Aug 16 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.88.4-1
 - Updated to 0.88.4
* Fri Jun 02 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 0.88.2-1
 - Updated to 0.88.2
* Fri Apr 14 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Updated to 0.88.1, switched to Sun CC
* Tue Nov 08 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Updated to 0.87.1
* Thu Jul 13 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Updated to 0.86.1
* Tue Jun 21 2005 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
 - Upgraded to 0.86
* Fri Feb 25 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Updated to 0.83
* Tue Feb 08 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Updated to 0.82
* Wed Feb 02 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Updated to 0.81
* Tue Oct 26 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Updated to 0.80 
* Mon Apr  5 2004 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Updated to 0.68-1
* Fri Jan 30 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Fixed clamav.conf bug.
* Mon Dec 22 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
 - Rutgerized package.
* Wed Dec 03 2003 Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
 - Initial Rutgers release
