Summary: firebird
Name: firebird
Version: 0.5.cvs.20030421
Release: 1ru
Copyright: GPL
Group: Applications/Internet
#Source: http://ftp.mozilla.org/pub/mozilla/nightly/latest/mozilla-source.tar.bz2
Source: mozilla-cvs-ru.tar
URL: http://www.mozilla.org/projects/phoenix
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Christopher J. Suleski <chrisjs@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root


%description
Phoenix. dirty ebuild -- more to follow

%prep
%setup -q -n mozilla

%build

# Most of this was stolen from the Gentoo phoenix-cvs ebuild
# So they should be credited with most of this wacky stuff

# This stuff gets done and repackaged as phoenix-ru as cvs-mirror.mozilla.org
# is flaky and often drops the connection when doing an automated build
#echo ":pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot A" > "cvspass"
#CVS_PASSFILE="`pwd`/cvspass"
#export CVS_PASSFILE
#cvs -z3 -d:pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot checkout mozilla/browser mozilla/toolkit mozilla/client.mk
#make -f mozilla/client.mk checkout

CPPFLAGS="-I/usr/sfw/include/glib-1.2 -I/usr/sfw/lib/glib/include -I/usr/local/include"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -lglib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib"
CC="gcc -03 -pipe -s -fforce-addr" 
PATH="/usr/sfw/bin:$PATH"
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH

MOZ_PHOENIX=1
MOZ_FIREBIRD=1 # Don't know if this is/will be in use
MOZ_CALENDAR=0
MOZ_ENABLE_XFT=1
export MOZ_PHOENIX MOZ_CALENDAR MOZ_ENABLE_XFT MOZ_FIREBIRD

./configure \
      --disable-composer \
      --disable-mailnews \
      --disable-calendar \
      --with-default-mozilla-five-home=/usr/local/lib/firebird \
      --with-user-appdir=.firebird \
      --disable-pedantic \
      --disable-svg \
      --enable-mathml \
      --without-system-nspr \
      --enable-nspr-autoconf \
      --enable-xsl \
      --enable-crypto \
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
      --disable-ldap \
      --disable-toolkit-qt \
      --disable-toolkit-xlib \
      --enable-toolkit-gtk \
      --enable-default-toolkit=gtk \
      --disable-toolkit-gtk2 \
      --disable-ipv6

make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/firebird $RPM_BUILD_ROOT/usr/local/bin
cp -pR dist/bin/* $RPM_BUILD_ROOT/usr/local/lib/firebird/
ln -sf ../lib/firebird/phoenix $RPM_BUILD_ROOT/usr/local/bin/firebird
chmod 755 $RPM_BUILD_ROOT/usr/local/bin/firebird

cp $RPM_BUILD_ROOT/usr/local/lib/firebird/defaults/pref/all.js all.js
sed "s/\"nglayout.initialpaint.delay\", 250/\"nglayout.initialpaint.delay\", 0/" all.js > $RPM_BUILD_ROOT/usr/local/lib/firebird/defaults/pref/all.js


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/lib/firebird/
/usr/local/bin/firebird



