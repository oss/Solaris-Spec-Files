Summary: Mozilla FireFox
Name: mozilla-firefox
Version: 1.0.4
Release: 2
Copyright: MPL/NPL
Group: Applications/Internet
Source: firefox-1.0.4-source.tar.bz2
URL: http://www.mozilla.org/projects/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
# just require gtk2-devel instead of pango-devel, glib2-devel atk-devel
BuildRequires: gtk2-devel pango-devel glib2-devel gcc >= 3.2 perl >= 5.6 make >= 3.79.1 libIDL >= 0.8
Requires: gtk2

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
LDFLAGS="-L/usr/local/lib/firefox-1.0.4 -R/usr/local/lib/firefox-1.0.4 -L/usr/local/lib -R/usr/local/lib -lglib-2.0 -L/usr/sfw/lib -R/usr/sfw/lib -lnsl"
LD_LIBRARY_PATH="/usr/local/lib:/usr/sfw/lib"
LD_RUN_PATH="/usr/local/lib:/usr/sfw/lib"
CC="gcc"
CXX="g++"
PATH="/usr/local/bin:/usr/sfw/bin:$PATH"
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC CXX PATH LIBIDL_CONFIG


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

./configure \
      --disable-mailnews \
      --disable-ldap \
      --enable-extensions=cookie,xml-rpc,xmlextras,pref,transformiix,universalchardet,webservices,inspector,gnomevfs,negotiateauth \
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
      --disable-xft \
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


rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}



%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/local/bin/*
/usr/local/lib/*
# without pkgconfig? what is pkgconfig? -- needed for upstream apps that build against this

%files devel
%defattr(0755,root,root)
/usr/local/share/*
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
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
