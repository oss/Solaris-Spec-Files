Summary:        The GNU Portable Threads library
Name:           pth
Version:        2.0.7
Release:        10
License:        LGPLv2+
Group:          System Environment/Libraries
URL:            http://www.gnu.org/software/pth/
Source:         ftp://ftp.gnu.org/gnu/pth/pth-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/pth/pth-%{version}.tar.gz.sig
Patch1:         pth-2.0.7-dont-remove-gcc-g.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms
which provides non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications.
All threads run in the same address space of the server application,
but each thread has it's own individual program-counter, run-time
stack, signal mask and errno variable.

%package devel
Summary:        Development headers and libraries for GNU Pth
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers and libraries for GNU Pth.


%prep
%setup -q
%patch1 -p1 -b .dont-remove-gcc-g



%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CFLAGS="-I/usr/local/include -O2 -g" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
export PATH CC CXX CFLAGS LD LDFLAGS
%configure --disable-static ac_cv_func_sigstack='no'


# this is necessary; without it make -j fails
gmake pth_p.h
gmake %{?_smp_mflags}



%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ANNOUNCE AUTHORS COPYING ChangeLog HISTORY NEWS PORTING README
%doc SUPPORT TESTS THANKS USERS
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc HACKING
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/*/*
%{_datadir}/aclocal/*


%changelog
* Wed Nov 04 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.0.7.10
- Solaris port

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 31 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.7-7
- Drop "|| :" from check section. It failed to build for mdomsch
  in Rawhide today.

* Fri Feb 08 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.7-6
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Sun Oct 21 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.7-5
- Patch pth-config.
  This shall fix the multiarch conflict in pth-devel (#342961).
  It must not return -I/usr/include and -L/usr/{lib,lib64} either,
  since these are default search paths already.
- Replace the config.status CFLAGS sed expr with a patch.

* Tue Aug 21 2007 Michael Schwendt <mschwendt@fedoraproject.org>
- rebuilt

* Thu Aug  2 2007 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.7-2
- Clarify licence (LGPLv2+).

* Sat Nov 25 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.7-1
- Update to 2.0.7 (very minor maintenance updates only).

* Mon Aug 28 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.6-3
- rebuilt

* Mon May 22 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.6-2
- Insert -g into CFLAGS after configure script removes it.
- Disable configure check for obsolete sigstack(), which segfaults.

* Thu Feb 16 2006 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.6-1
- Update to 2.0.6.

* Fri Oct  7 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5.
- Don't build static archive.

* Fri May 13 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-3
- rebuilt

* Thu Apr  7 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.4-2
- rebuilt

* Thu Feb 24 2005 Michael Schwendt <mschwendt@fedoraproject.org> - 0:2.0.4-1
- Update to 2.0.4.
- Remove ancient changelog entries which even pre-date Fedora.

* Tue Dec 14 2004 Michael Schwendt <mschwendt@fedoraproject.org> - 0:2.0.3-1
- Update to 2.0.3, minor and common spec adjustments + LGPL, %%check,
  use URLs for official GNU companion sites.

* Thu Oct 07 2004 Adrian Reber <adrian@lisas.de> - 0:2.0.2-0.fdr.2
- iconv-ing spec to utf8

* Wed Oct 06 2004 Adrian Reber <adrian@lisas.de> - 0:2.0.2-0.fdr.1
- Update to 2.0.2 and current Fedora guidelines.
- added workaround for make -j problem

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0.0-0.fdr.1
- Update to 2.0.0 and current Fedora guidelines.
- Exclude %%{_libdir}/*.la

* Fri Feb  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-1.fedora.1
- First Fedora release, based on Ryan Weaver's work.
- Move (most of) docs to main package.

