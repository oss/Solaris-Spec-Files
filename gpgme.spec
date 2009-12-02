
Name:    gpgme
Summary: GnuPG Made Easy - high level crypto API
Version: 1.1.8
Release: 4%{?dist}

License: LGPLv2+
Group:   Applications/System
URL:     http://www.gnupg.org/related_software/gpgme/
Source0: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1: gpgme-1.1.8-config_extras.patch

BuildRequires: gawk
BuildRequires: gnupg
BuildRequires: gnupg2
BuildRequires: libgpg-error-devel
BuildRequires: pth-devel

# --disable-gpg-test required since 'make check' currently includes some
# gpg(1)-specific tests
%define _with_gpg --with-gpg=%{_bindir}/gpg2 --disable-gpg-test
Requires: gnupg2

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:  Development headers and libraries for %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libgpg-error-devel
Requires(post): info
Requires(postun): info
%description devel
%{summary}


%prep
%setup -q

%patch1 -p1 -b .config_extras

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

# void function cannot return value:
sed -i -e 's|\(return _gpgme_conf_arg_release\)|//\1|' src/gpgconf.c

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CFLAGS="-I/usr/local/include -O2 -g" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CFLAGS LD LDFLAGS
%configure \
  --disable-static \
  %{?_with_gpg}

gmake %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

# unpackaged files
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/gpgme/


%check 
# skip for now
# expect 1(+?) errors with gnupg < 1.2.4
# gpgme-1.1.6 includes one known failure (FAIL: t-sign)
# make -C tests check 


%clean
rm -rf $RPM_BUILD_ROOT


%post devel
/usr/local/bin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun devel
if [ $1 -eq 0 ] ; then
  /usr/local/bin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* ChangeLog NEWS README* THANKS TODO VERSION
%{_libdir}/libgpgme.so.11*
%{_libdir}/libgpgme-pth.so.11*
%{_libdir}/libgpgme-pthread.so.11*

%files devel
%defattr(-,root,root,-)
%{_bindir}/gpgme-config
%{_includedir}/*
%{_libdir}/libgpgme*.so
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*


%changelog
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> 1.1.8-4
- I will not publish unsigned packages again

* Wed Nov 04 2009 Orcan Ogetbil <orcan@ncbs.rutgers.edu> 1.1.8-3
- Solaris port

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.8-1
- gpgme-1.1.8
- -devel: s/postun/preun/ info scriptlet

* Wed Mar 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.1.7-3
- track shlib sonames closer, to highlight future abi/soname changes
- _with_gpg macro, to potentially conditionalize gnupg vs gnupg2 defaults
  for various os/releases (ie, fedora vs rhel)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 18 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.7-1
- gpgme-1.1.7

* Sun Feb 17 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.6-3
- --with-gpg=%%_bindir/gpg2 (#432445)
- drop Requires: gnupg (#432445)

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 1.1.6-2 
- respin (gcc43)

* Fri Jan 04 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.6-1
- gpgme-1.1.6
- multiarch conflicts in gpgme (#341351)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-4
- BR: gawk

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-3
- respin (BuildID)

* Thu Aug 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-2
- License: LGPLv2+

* Mon Jul 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.5-1
- gpgme-1.1.5

* Mon Mar 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.4-1
- gpgme-1.1.4

* Sat Feb 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.1.3-1
- gpgme-1.1.3

* Tue Oct 03 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- respin

* Mon Sep 18 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-6
- fix gpgme-config --thread=pthread --cflags

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-5
- fc6 respin

* Mon Mar 6 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-4
- add back support for gpgme-config --thread=pthread

* Mon Mar 6 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-2
- drop extraneous libs from gpgme-config

* Fri Mar 3 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.1.2-1
- 1.1.2
- drop upstreamed gpgme-1.1.0-tests.patch

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Wed Nov 30 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 1.1.0-3
- (re)build against (newer) libksba/gnupg2

* Thu Oct 06 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 1.1.0-2
- 1.1.0

* Mon Aug  8 2005 Rex Dieter <rexdieter[AT]users.sf.net> - 1.0.3-1
- 1.0.3
- --disable-static

* Thu May 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-3
- rebuilt

* Fri Mar 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.2-2
- Fix FC4 build.

* Tue Feb  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:1.0.2-1
- LGPL used here, and made summary more explicit.
- Remove dirmngr dependency (gpgsm interfaces with it).
- Obsolete cryptplug as gpgme >= 0.4.5 provides what we used cryptplug for.

* Thu Jan 06 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:1.0.2-0.fdr.1
- 1.0.2

* Thu Oct 21 2004 Rex Dieter <rexdieter at sf.net> 0:1.0.0-0.fdr.1
- 1.0.0
- Requires: dirmngr

* Tue Oct 19 2004 Rex Dieter <rexdieter at sf.net> 0:0.4.7-0.fdr.1
- 0.4.7

* Sun May  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.3
- Require %%{_bindir}/gpgsm instead of newpg.
- Cosmetic spec file improvements.

* Thu Oct 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.2
- Update description.

* Tue Oct  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.3-0.fdr.1
- Update to 0.4.3.

* Fri Aug 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.2-0.fdr.1
- Update to 0.4.2.
- make check in the %%check section.

* Thu Jul 10 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.1-0.fdr.1
- Update to 0.4.1.
- Make -devel cooperate with --excludedocs.

* Sat Apr 19 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.2
- BuildRequire pth-devel, fix missing epoch in -devel Requires (#169).
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.4.0-0.fdr.1
- Update to current Fedora guidelines.
- Exclude %%{_libdir}/*.la.

* Tue Feb 12 2003 Warren Togami <warren@togami.com> 0.4.0-1.fedora.3
- info/dir temporary workaround

* Sat Feb  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-1.fedora.1
- First Fedora release.
