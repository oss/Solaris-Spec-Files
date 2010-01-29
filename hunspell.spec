Name:      hunspell
Summary:   A spell checker and morphological analyzer library
Version:   1.2.8
Release:   18%{?dist}
Source0:   http://downloads.sourceforge.net/%{name}/hunspell-%{version}.tar.gz
Source1:   http://people.debian.org/~agmartin/misc/ispellaff2myspell
Source2:   http://people.redhat.com/caolanm/hunspell/wordlist2hunspell
Group:     System Environment/Libraries
URL:       http://hunspell.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License:   LGPLv2+ or GPLv2+ or MPLv1.1
BuildRequires: libtool
BuildRequires: ncurses-devel
BuildRequires: readline5-devel
Patch1:    hunspell-1.2.7-2314461.ispell-alike.patch
Patch2:    hunspell-1.2.8-2784983.defaultlanguage.patch
Patch3:    hunspell-1.2.8-2812045.warnings.fortify.patch
Patch4:    hunspell-1.2.8-2826164.fixtests.patch
Patch5:    hunspell-1.2.8-2910695.nohome.patch
Patch6:    hunspell-1.2.8-2934195.suggestmgr.patch

# OSS patches
Patch10:   hunspell-1.2.8-solaris-compile.patch

%description
Hunspell is a spell checker and morphological analyzer library and program 
designed for languages with rich morphology and complex word compounding or 
character encoding. Hunspell interfaces: Ispell-like terminal interface using 
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

%package devel
Requires: hunspell = %{version}-%{release}, pkgconfig
Summary: Files for developing with hunspell
Group: Development/Libraries

%description devel
Includes and definitions for developing with hunspell

%prep
%setup -q
%patch1 -p1 -b .ispell-alike.patch
%patch2 -p1 -b .defaultlanguage.patch
%patch3 -p1 -b .warnings.fortify.patch
%patch4 -p1 -b .fixtests.patch
%patch5 -p1 -b .nohome.patch
%patch6 -p1 -b .suggestmgr.patch
%patch10 -p1 -b .solaris.compile
# Filter unwanted Requires for the "use explicitely" string in ispellaff2myspell
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(explicitely)/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
aclocal -I m4
libtoolize --force --copy
automake --add-missing --copy
autoconf

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc"
CXX="CC"
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -liconv -R/usr/local/lib" \
CFLAGS="-g -xs -I/usr/local/include -I/usr/local/include/ncurses "
CPPFLAGS="-g -xs -I/usr/local/include -I/usr/local/include/ncurses "
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure --disable-static  --with-ui --with-readline --cache-file=FILE

for i in AUTHORS.myspell; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
gmake %{?_smp_mflags}

%check
gmake -C tests check-TESTS

%install
rm -rf $RPM_BUILD_ROOT
gmake DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_bindir}/example
mkdir $RPM_BUILD_ROOT/%{_datadir}/myspell
mv $RPM_BUILD_ROOT/%{_includedir}/*munch* $RPM_BUILD_ROOT/%{_includedir}/%{name}
install -p -m 755 src/tools/affixcompress $RPM_BUILD_ROOT/%{_bindir}/affixcompress
install -p -m 755 src/tools/makealias $RPM_BUILD_ROOT/%{_bindir}/makealias
install -p -m 755 src/tools/wordforms $RPM_BUILD_ROOT/%{_bindir}/wordforms
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/ispellaff2myspell
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}/wordlist2hunspell
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README README.myspell COPYING COPYING.LGPL COPYING.MPL AUTHORS AUTHORS.myspell license.hunspell license.myspell THANKS
%{_libdir}/*.so.*
%{_datadir}/myspell
%{_bindir}/hunspell
%{_mandir}/man1/hunspell.1
%{_mandir}/man4/hunspell.4
%dir %{_mandir}/hu
%dir %{_mandir}/hu/man1
%dir %{_mandir}/hu/man4
%lang(hu) %{_mandir}/hu/man1/hunspell.1
%lang(hu) %{_mandir}/hu/man4/hunspell.4

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_bindir}/affixcompress
%{_bindir}/makealias
%{_bindir}/munch
%{_bindir}/unmunch
%{_bindir}/analyze
%{_bindir}/chmorph
%{_bindir}/hzip
%{_bindir}/hunzip
%{_bindir}/ispellaff2myspell
%{_bindir}/wordlist2hunspell
%{_bindir}/wordforms
%{_libdir}/pkgconfig/hunspell.pc
%{_mandir}/man1/hunzip.1
%{_mandir}/man1/hzip.1
%{_mandir}/man3/hunspell.3

%changelog
* Thu Jan 28 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.2.8-18
- Rebuild without gettext dependency

* Fri Jan 22 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.2.8-17
- Solaris port

* Mon Jan 18 2010 Caolan McNamara <caolanm@redhat.com> - 1.2.8-16
- Resolves: rhbz#554876 fix suggestmgr crash

* Tue Jan 05 2010 Caolan McNamara <caolanm@redhat.com> - 1.2.8-15
- Remove bad const warnings

* Mon Dec 21 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-14
- Preserve timestamps

* Tue Dec 08 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-13
- Resolves: rhbz#544372 survive having no HOME

* Thu Jul 30 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-12
- handle some other interesting edge-cases

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-10
- run tests in check

* Thu Jul 09 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-9
- Resolves: rhbz#510360 unowned dirs
- fix up rpmlint warnings

* Tue Jul 07 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-8
- Resolves: rhbz#509882 ignore an empty LANGUAGE variable

* Fri Jun 26 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-7
- Related: rhbz#498556 default to something sensible in "C" locale
  for language

* Wed Jun 24 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-6
- Resolves: rhbz#507829 fortify fixes

* Fri May 01 2009 Caolan McNamara <caolanm@redhat.com> - 1.2.8-5
- Resolves: rhbz#498556 fix default language detection

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.8-3
- tweak summary

* Wed Nov 19 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.8-2
- Resolves: rhbz#471085 in ispell compatible mode (-a), ignore
  -m option which means something different to ispell

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.8-1
- latest version

* Sat Oct 18 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.7-5
- sort as per "C" locale

* Fri Oct 17 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.7-4
- make wordlist2hunspell remove blank lines 

* Mon Sep 15 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.7-3
- Workaround rhbz#462184 uniq/sort problems with viramas

* Tue Sep 09 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.7-2
- add wordlist2hunspell

* Sat Aug 23 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.7-1
- latest version

* Tue Jul 29 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.6-1
- latest version

* Sun Jul 27 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.5-1
- latest version

* Tue Jul 22 2008 Kristian Høgsberg <krh@redhat.com> - 1.2.4.2-2
- Drop ABI breaking hunspell-1.2.2-xulrunner.pita.patch and fix the
  hunspell include in xulrunner.

* Fri Jun 18 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.4.2-1
- latest version

* Thu Jun 17 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.4-1
- latest version

* Fri May 16 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.2-3
- Resolves: rhbz#446821 fix crash

* Wed May 14 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.2-2
- give xulrunner what it needs so we can get on with it

* Fri Apr 18 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.2-1
- latest version
- drop integrated hunspell-1.2.1-1863239.badstructs.patch

* Wed Mar 05 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.1-6
- add ispellaff2myspell to devel

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-5
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Caolan McNamara <caolanm@redhat.com> - 1.2.1-4
- add hunspell-1.2.1-1863239.badstructs.patch

* Fri Nov 09 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.1-2
- pkg-config cockup

* Mon Nov 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Mon Oct 08 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.12.2-2
- lang fix for man pages from Ville Skyttä

* Wed Sep 05 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.12.2-1
- next version

* Tue Aug 28 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.11.2-1
- next version

* Fri Aug 24 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.10-1
- next version

* Thu Aug 02 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.9-2
- clarify license

* Wed Jul 25 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.9-1
- latest version

* Wed Jul 18 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.8.2-1
- latest version

* Tue Jul 17 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.8-1
- latest version

* Sat Jul 07 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.7-1
- latest version
- drop integrated hunspell-1.1.5.freem.patch

* Fri Jun 29 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.6-1
- latest version
- drop integrated hunspell-1.1.4-defaultdictfromlang.patch
- drop integrated hunspell-1.1.5-badheader.patch
- drop integrated hunspell-1.1.5.encoding.patch

* Fri Jun 29 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-5
- fix memory leak
  http://sourceforge.net/tracker/index.php?func=detail&aid=1745263&group_id=143754&atid=756395

* Wed Jun 06 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-4
- Resolves: rhbz#212984 discovered problem with missing wordchars

* Tue May 22 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-3
- Resolves: rhbz#240696 extend encoding patch to promote and add
  dictionary 8bit WORDCHARS to the ucs-2 word char list

* Mon May 21 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-2
- Resolves: rhbz#240696 add hunspell-1.1.5.encoding.patch

* Mon May 21 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5.3-1
- patchlevel release

* Tue Mar 20 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5-2
- some junk in delivered headers

* Tue Mar 20 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.5-1
- next version

* Fri Feb 09 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.4-6
- some spec cleanups

* Fri Jan 19 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.4-5
- .pc

* Thu Jan 11 2007 Caolan McNamara <caolanm@redhat.com> - 1.1.4-4
- fix out of range

* Fri Dec 15 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-3
- hunspell#1616353 simple c api for hunspell

* Wed Nov 29 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-2
- add hunspell-1.1.4-defaultdictfromlang.patch to take locale as default
  dictionary

* Wed Oct 25 2006 Caolan McNamara <caolanm@redhat.com> - 1.1.4-1
- initial version
