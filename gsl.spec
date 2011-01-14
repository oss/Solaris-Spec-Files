Summary:       The GNU Scientific Library for numerical analysis
Name:          gsl
Version:       1.14
Release:       2%{?dist}
URL:           http://www.gnu.org/software/gsl/
Source:        ftp://ftp.gnu.org/gnu/gsl/%{name}-%{version}.tar.gz
Patch1:        gsl-1.14-link.patch
# info part of this package is under GFDL license
# eigen/nonsymmv.c and eigen/schur.c
# contains rutiens which are part of LAPACK - under BSD style license
License:       GPLv3 and GFDL and BSD
Group:         System Environment/Libraries
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: pkgconfig

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package devel
Summary:       Libraries and the header files for GSL development
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig, automake

%description devel
The gsl-devel package contains the header files necessary for 
developing programs using the GSL (GNU Scientific Library).

%prep
%setup -q
%patch1 -p1 -b .libs
iconv -f windows-1252 -t utf-8 THANKS  > THANKS.aux
touch -r THANKS THANKS.aux
mv THANKS.aux THANKS


%build
%configure 
gmake %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT install='install -p'

# remove unpackaged files from the buildroot
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# remove static libraries
rm -r $RPM_BUILD_ROOT%{_libdir}/*.a


%post devel
if [ -f %{_infodir}/gsl-ref.info.gz ]; then
    /sbin/install-info %{_infodir}/gsl-ref.info %{_infodir}/dir || :
fi

%preun devel
if [ "$1" = 0 ]; then
    if [ -f %{_infodir}/gsl-ref.info.gz ]; then
	/sbin/install-info --delete %{_infodir}/gsl-ref.info %{_infodir}/dir || :
    fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO
%{_libdir}/*so.*
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/gsl-config*
%{_datadir}/aclocal/*
%{_includedir}/*
%{_infodir}/*info*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gsl.pc
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/*.3*


%changelog
* Tue Aug 31 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.14-2
- Solaris port. Based on Fedora specfile.

* Wed May  5 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.14-1
- update to 1.14
- Resolves: #560219
             Library not linked correctly

* Wed Mar  3 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 1.13-2
- remove the static subpackage

* Tue Sep 15 2009 Ivana Varekova <varekova@redhat.com> - 1.13-1
- update to 1.13

* Mon Aug 17 2009 Ivana Varekova <varekova@redhat.com> - 1.12-6
- fix preun and post scripts (#517568)

* Mon Aug 10 2009 Ivana Varekova <varekova@redhat.com> - 1.12-5
- fix installation with --excludedocs option (#515971)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 07 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 1.12-3
- Remove rpaths (fix BZ#487823).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Ivana Varekova <varekova@redhat.com> - 1.12-1
- update to 1.12

* Tue Sep 16 2008 Ivana Varekova <varekova@redhat.com> - 1.11-4
- Resolves: #462369 - remove %%{_datadir}/aclocal
- add automake dependency

* Mon Jul 28 2008 Ivana Varekova <varekova@redhat.com> - 1.11-3
- add -fgnu89-inline flag to solve gcc4.3 problem 
  remove gcc43 patch

* Wed Jun 18 2008 Ivana Varekova <varekova@redhat.com> - 1.11-2
- Resolves: #451006
  programs build with gcc 4.3 based on gsl require -fgnu89-inline 

* Mon Jun 16 2008 Ivana Varekova <varekova@redhat.com> - 1.11-1
- update to 1.11

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10-10
- Autorebuild for GCC 4.3

* Thu Nov  1 2007 Ivana Varekova <varekova@redhat.com> - 1.10-9
- source file change
- spec cleanup

* Thu Nov  1 2007 Ivana Varekova <varekova@redhat.com> - 1.10-8
- fix man-pages directories

* Tue Oct 30 2007 Ivana Varekova <varekova@redhat.com> - 1.10-7
- add man pages

* Fri Oct 26 2007 Ivana Varekova <varekova@redhat.com> - 1.10-6
- minor spec changes

* Thu Oct 25 2007 Ivana Varekova <varekova@redhat.com> - 1.10-5
- minor spec changes

* Wed Oct 24 2007 Ivana Varekova <varekova@redhat.com> - 1.10-4
- add pkgconfig dependency
- separate static libraries to -static subpackage
- fix gsl-config script - thanks Patrice Dumas

* Tue Sep 23 2007 Ivana Varekova <varekova@redhat.com> - 1.10-3
- remove *.la files
- add pkgconfig configure file
- change source
- spec file cleanup

* Wed Sep 19 2007 Ivana Varekova <varekova@redhat.com> - 1.10-2
- update license tag

* Wed Sep 19 2007 Ivana Varekova <varekova@redhat.com> - 1.10-1
- update to 1.10
- change license tag

* Tue May 22 2007 Ivana Varekova <varekova@redhat.com> - 1.9-1
- update  to 1.9

* Wed Mar 14 2007 Ivana Varekova <varekova@redhat.com> - 1.8-3
- incorporate the package review feedback

* Mon Jan 22 2007 Ivana Varekova <varekova@redhat.com> - 1.8-2
- Resolves: 223700
  fix non-failsafe install-info problem
- spec file cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.8-1.1
- rebuild

* Fri May  5 2006 Ivana Varekova <varekova@redhat.com> - 1.8-1
- update to 1.8

* Fri Mar  3 2006 Ivana Varekova <varekova@redhat.com> - 1.7-2
- fix multilib problem

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.7-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.7-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Ivana Varekova <varekova@redhat.com> 1.7-1
- update to 1.7

* Mon Mar  7 2005 Ivana Varekova <varekova@redhat.com> 1.6-2
- rebuilt

* Thu Jan  6 2005 Ivana Varekova <varekova@redhat.com> 1.6-1
- update to 1.6 

* Wed Dec 15 2004 Ivana Varekova <varekova@redhat.com>
- fix bug #142696 gsl-config outputs invalid flags on multilib 64-bit 
architectures

* Fri Jul 02 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.5

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Aug 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.4

* Wed Jun 25 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.3

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 1.1.1-4
- remove unpackaged files from the buildroot

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Mar 21 2002 Trond Eivind Glomsrød <teg@redhat.com>
- 1.1.1 bugfix release
- Stop the gsl-config script from printing -I/usr/include 
  and -L/usr/lib (#59500)


* Wed Feb 27 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.1-1
- 1.1
- Update URL and location

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Dec 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.0-1
- 1.0
- Split into gsl and gsl-devel
- update description (#56926)

* Thu Jul 19 2001 Preston Brown <pbrown@redhat.com>
- upgrade to 0.9

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Jan 18 2001 Preston Brown <pbrown@redhat.com>
- prereq install-info (#24250)

* Mon Dec 11 2000 Preston Brown <pbrown@redhat.com>
- 0.7, remove excludearch for ia64

* Sun Jul 30 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- fix %%post to be a real shell and add ldconfig to %%post

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Preston Brown <pbrown@redhat.com>
- don't include the info dir file...

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- add %%defattr

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- 0.6, FHS paths
- exclude ia64, it is having issues

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- update to 0.3f
- add patches to fix glibc-2.1 compilation, doc oddity

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- new summary/description, work around automake oddity

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- libtoolize for arm

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- spec file fixups

* Sat May 9 1998 Michael Fulbright <msf@redhat.com>
- started with package for gmp from Toshio Kuratomi <toshiok@cats.ucsc.edu>
- cleaned up file list
- fixed up install-info support
