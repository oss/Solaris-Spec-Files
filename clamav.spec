%global build_64bit 0

Summary:	An antivirus for Unix
Name:		clamav
Version:	0.97.8
Release:	1
License:	GPL
Group:		Applications/System
Source0:        http://downloads.sourceforge.net/clamav/%{name}-%{version}.tar.gz
URL:		http://clamav.sf.net/
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Requires:	gmp
BuildRequires:	gmp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Clam AntiVirus is an powerful anti-virus toolkit for Unix.
The package provides a flexible and scalable multi-threaded daemon,
a command line scanner, and a tool for automatic updating via Internet.
It supports AMaViS, Sendmail milter, compressed files and mbox format.
Clamav is multithreaded, written in C, and POSIX compliant.

%prep
%setup -q

%build
# Add/Remove -m64 to build 64bit/32bit
%if %{build_64bit}
CFLAGS="-I/usr/local/include/gmp32 -m64"
CPPFLAGS="-I/usr/local/include/gmp32 -m64"
%else
CFLAGS="-I/usr/local/include/gmp32"
CPPFLAGS="-I/usr/local/include/gmp32"
%endif

LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lz"

export LDFLAGS

./configure \
	CC=cc \
	--enable-id-check \
	--disable-clamav \
	--with-user=clamav \
	--with-group=clamav \
	--with-dbdir=%{_localstatedir}/lib/clamav \
	--sysconfdir=/etc \
	--disable-silent-rules

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/etc/clamd.conf $RPM_BUILD_ROOT/etc/clamd.conf.example
mv $RPM_BUILD_ROOT/etc/freshclam.conf $RPM_BUILD_ROOT/etc/freshclam.conf.example

rm $RPM_BUILD_ROOT/usr/local/lib/libclamav.la  # Rid the evil
rm $RPM_BUILD_ROOT/usr/local/lib/libclamunrar.la
rm $RPM_BUILD_ROOT/usr/local/lib/libclamunrar_iface.la

%clean
#rm -rf $RPM_BUILD_ROOT

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
#%attr(0755,root,bin) %dir %{_localstatedir}/lib/clamav/
%attr(0644,root,bin) %{_libdir}/pkgconfig/libclamav.pc
#%config(noreplace) %attr(0644,root,bin) %{_localstatedir}/lib/clamav/main.cvd
#%config(noreplace) %attr(0644,root,bin) %{_localstatedir}/lib/clamav/daily.cvd
/usr/local/share/man/*

%changelog
* Fri Jun 28 2013 Matt Robinson <mwr54@nbcs.rutgers.edu> - 0.97.8-1
- bumped to 0.97.8
- removed references to .cvd files

* Tue Apr 18 2012 Josh Matthews <jmatth@nbcs.rutgers.edu> - 0.97.4-2
- rebuilt to fix gpg key signing issues

* Tue Mar 20 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.4-1
- Bump to 0.97.4

* Fri Mar 09 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-8
- added and exported LDFLAGS to fix library linking issue.

* Fri Mar 09 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-6
- rebuilt to link against only one version of libz in /usr/local/lib

* Wed Mar 07 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-5
-added export statements for LD_LIBRARY_PATH so it links to the correct libraries.

* Tue Mar 06 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-4
-rebuilt after reinstalling build machine. May fix not found errors.

* Tue Feb 28 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-3
-moved CC=cc to the configure flags
-removed clean

* Tue Feb 21 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-2
- changed gmake to make 
- added export to use cc instead of gcc

* Fri Jan 12 2012 Josh Matthews <jam761@nbcs.rutgers.edu> - 0.97.3-1
- bump to 0.97.3
- changed %configure to ./configure under build

* Mon Aug 15 2011 Steven Lu <sjlu@nbcs.rutgers.edu> - 0.97.2-1
- bump to 0.97.2

* Mon Jun 27 2011 Russ Frank <rfranknj@nbcs.rutgers.edu> - 0.97.1-1
- bump to 0.97.1

* Mon Feb 28 2011 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 0.97-1
- updated to 0.97 

* Tue Nov 30 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.5-1
- Update to 0.96.5

* Fri Oct 01 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.3-2
- Set localstatedir back to /usr/local/var

* Wed Sep 29 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.3-1
- Update to 0.96.3

* Wed Aug 18 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.2-1
- Update to 0.96.2

* Thu Jun 03 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.1-5
- Rebuild with -m64 flag.

* Thu Jun 03 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.1-4
- Fix memalign bug

* Thu May 27 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.1-3
- Compile without optimization

* Thu May 20 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.96.1-2
- Rebuild with -m64 flag.
- Some cleanup in the specfile

* Wed May 19 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 0.96.1-1
- version bump to 0.96.1
* Tue Apr 27 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 0.96-1
- version bump to 0.96
* Thu Mar 25 2010 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - .96rc2-1
- version bump to .96rc2
* Mon Jan 11 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 0.95.3-1
- Updated to 0.95.3
* Wed Jun 17 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.95.2-1
- updated to 0.95.2
* Mon Apr 20 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.95.1-1
- updated to 0.95.1
* Mon Mar 23 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.95-1
- updated to 0.95
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
