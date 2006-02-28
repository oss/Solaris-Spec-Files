%define _libdir /usr/local/lib

Summary: Mozilla Firefox
Name: mozilla-firefox
Version: 1.5.0.1
Release: 1
Copyright: MPL/NPL
Group: Applications/Internet
Source: firefox-%{version}-source.tar.bz2
URL: http://www.mozilla.org/projects/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: gcc >= 3.2
BuildRequires: perl >= 5.6
BuildRequires: make >= 3.19.1
BuildRequires: gtk2-devel
# make a libIDL2 package? and split off a -devel package?
#BuildRequires: libIDL2-devel
BuildRequires: libIDL >= 0.8
#BuildRequires: freetype2-devel = 2.1.8
BuildRequires: xft2-devel
BuildRequires: fontconfig-devel
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: cairo >= 1.0.2
BuildRequires: cairo-devel >= 1.0.2
BuildRequires: libstdc++-v3-devel
# The mozilla devs don't provide a clear picture of what is really necessary
# to build firefox (http://www.mozilla.org/build/unix.html), so hopefully
# this works
Conflicts: mozilla-firefox-bin
Obsoletes: mozilla-firebird FireFox phoenix nss
Provides: webclient

%define ffdir %{_libdir}/firefox-%{version}

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries 
for building applications which use {%name}.

%prep
%setup -q -n mozilla


CPPFLAGS="-I/usr/local/include -I/usr/local/include/glib-2.0 -I/usr/local/include/gtk-2.0 -I/usr/local/include/gtk-2.0/gdk -I/usr/local/include/c++/3.*.*/ -I/usr/sfw/include"
# I added -lnsl (see BUG#: 268847)
LDFLAGS="-L/usr/local/lib/firefox-1.5 -R/usr/local/lib/firefox-1.5 -L/usr/local/lib -R/usr/local/lib -lglib-2.0 -L/usr/sfw/lib -R/usr/sfw/lib -lnsl"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
LD="/usr/local/gnu/bin/ld"
AS="/usr/local/gnu/bin/as"
AR="/usr/local/gnu/bin/ar"
RANLIB="/usr/local/gnu/bin/ranlib"
CC="gcc -g"
CXX="g++ -g"
PATH="/usr/local/gnu/bin:/usr/local/bin:/usr/sfw/bin:$PATH"
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH LD AS AR RANLIB CC CXX PATH LIBIDL_CONFIG


MOZILLA_OFFICIAL=1
BUILD_OFFICIAL=1
MOZ_PHOENIX=1
export MOZ_PHOENIX MOZILLA_OFFICIAL BUILD_OFFICIAL


# Removed --enable-nspr-autoconf \
#configure: warning: Recreating autoconf.mk with updated nspr-config output
#+ make 
#make: Fatal error in reader: ./config/autoconf.mk, line 163: Unexpected end of line seen


# First 7 lines are from the browser/config/mozconfig file
# The next one is necessary?

# Removed gnomevfs from extensions

# What exactly do we want here?

./configure \
      --disable-mailnews \
      --disable-ldap \
      --enable-extensions=cookie,xml-rpc,xmlextras,pref,transformiix,universalchardet,webservices,inspector,negotiateauth \
      --enable-crypto \
      --disable-composer \
      --enable-single-profile \
      --disable-profilesharing \
      --enable-application=browser \
      --disable-calendar \
      --with-default-mozilla-five-home=/usr/local/lib/firefox \
      --with-user-appdir=.firefox \
      --disable-pedantic \
      --disable-svg \
      --enable-mathml \
      --without-system-nspr \
      --enable-xsl \
      --disable-jsd \
      --disable-accessibility \
      --disable-tests \
      --disable-debug \
      --disable-dtd-debug \
      --disable-logging \
      --enable-reorder \
      --enable-strip \
      --enable-strip-libs \
      --enable-cpp-rtti \
      --enable-xterm-updates \
      --enable-js-ultrasparc \
      --enable-extensions \
      --enable-xft \
      --disable-freetype2 \
      --enable-canvas \
      --enable-system-cairo \
      --disable-toolkit-qt \
      --disable-toolkit-xlib \
      --enable-toolkit-gtk2 \
      --enable-default-toolkit=gtk2 \
      --disable-toolkit-gtk \
      --disable-ipv6 \
      --with-libidl-prefix=/usr/local

gmake


# This is for Bug #s {263524, 268414, 284108, 255958}
cat browser/app/Makefile.in | sed s/destdir/DESTDIR/ > browser/app/Makefile.in2
mv browser/app/Makefile.in2 browser/app/Makefile.in

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{ffdir}/extensions/talkback@mozilla.org
touch %{buildroot}%{ffdir}/extensions/talkback@mozilla.org/chrome.manifest

# Borrowed from Fedora's spec file for firefox-1.0.4-4
# ghost files
#mkdir -p %{buildroot}%{ffdir}/chrome/overlayinfo/browser/content
#mkdir -p %{buildroot}%{ffdir}/chrome/overlayinfo/communicator/content
#mkdir -p %{buildroot}%{ffdir}/chrome/overlayinfo/inspector/content
#mkdir -p %{buildroot}%{ffdir}/chrome/overlayinfo/messenger/content
#mkdir -p %{buildroot}%{ffdir}/chrome/overlayinfo/navigator/content
#mkdir -p %{buildroot}%{ffdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}

#touch %{buildroot}%{ffdir}/chrome/overlayinfo/browser/content/overlays.rdf
#touch %{buildroot}%{ffdir}/chrome/overlayinfo/communicator/content/overlays.rdf
#touch %{buildroot}%{ffdir}/chrome/overlayinfo/inspector/content/overlays.rdf
#touch %{buildroot}%{ffdir}/chrome/overlayinfo/messenger/content/overlays.rdf
#touch %{buildroot}%{ffdir}/chrome/overlayinfo/navigator/content/overlays.rdf
#touch %{buildroot}%{ffdir}/chrome/chrome.rdf
# These 2 don't seem to be there. That might change next recompile
#touch %{buildroot}%{ffdir}/components/xpti.dat
#touch %{buildroot}%{ffdir}/components/compreg.dat
#touch %{buildroot}%{ffdir}/extensions/Extensions.rdf
#touch %{buildroot}%{ffdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}/install.rdf
#touch %{buildroot}%{ffdir}/extensions/installed-extensions-processed.txt
#touch %{buildroot}%{ffdir}/components.ini

#===================================================================

%clean
%{__rm} -rf %{buildroot}

#===================================================================

%files
%defattr(0755,root,root)
/usr/local/bin/*
/usr/local/lib/firefox-1.5

%ghost %{ffdir}/extensions/talkback@mozilla.org/chrome.manifest
#%ghost %{ffdir}/chrome/overlayinfo/browser/content/overlays.rdf
#%ghost %{ffdir}/chrome/overlayinfo/communicator/content/overlays.rdf
#%ghost %{ffdir}/chrome/overlayinfo/navigator/content/overlays.rdf
#%ghost %{ffdir}/chrome/overlayinfo/messenger/content/overlays.rdf
#%ghost %{ffdir}/chrome/overlayinfo/inspector/content/overlays.rdf
#%ghost %{ffdir}/chrome/chrome.rdf
#%ghost %{ffdir}/components/xpti.dat
#%ghost %{ffdir}/components/compreg.dat
#%ghost %{ffdir}/extensions/Extensions.rdf
#%ghost %{ffdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}/install.rdf
#%ghost %{ffdir}/extensions/installed-extensions-processed.txt
#%ghost %{ffdir}/components.ini

%files devel
%defattr(0755,root,root)
/usr/local/share/*
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Fri Dec 02 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5-1
- Updated to 1.5, fixed root install problem

* Fri Nov 18 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.5rc3-1
- Upgraded to newest release candidate of version 1.5

* Thu Jul 07 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.0.4-5
- forgot to quote echo text
- ??? fixed the part borrowed from fedora/ghosted files ???

* Thu Jun 30 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.0.4-4
- forgot to echo the %post text
- added %ghost files to cover firefox's post install shenanigans
- spec file tweaks

* Wed Jun 29 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.0.4-3
- Added %post message
- Fixed the %files section

* Sun Jun 26 2005 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 1.0.4-2
- Added /usr/local/lib/firefox-1.0.4 to LDFLAGS due to a few missing
- libraries when an ldd of /usr/local/lib/firefox-1.0.4/firefox-bin was run

* Fri Jun 10 2005 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.0.4-1
- Upgraded to release 1.0.4
- Built against gtk2 instead of gtk+

* Mon Mar 05 2005 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 1.0.1-1
- Upgraded to release 1.0.1
- Several changes were needed 

* Fri Apr 23 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.8.0-3
- Fixed permissions problem

* Wed Feb 25 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.8.0-2
- Renamed to mozilla-firefox
- Seperated into regular and devel packages

* Fri Feb 20 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.8.0-1
- Updated to FireFox

* Wed Dec 03 2003 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.7.0-1
- Modified for Rutgers RPM Repository

* Thu Oct 16 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Added typeaheadfind to extensionlist. (Jeroen Cranendonk)
- Updated to release 0.7.0.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Used gtk2 explicitly as the toolkit. (Duncan Mak)

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Wed Jun 25 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Initial package. (using DAR)
