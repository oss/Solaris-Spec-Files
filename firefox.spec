Summary: Mozilla FireFox
Name: mozilla-firefox
Version: 0.9.3
Release: 1
Copyright: GPL
Group: Applications/Internet
Source: firefox-%{version}-source.tar.bz2
URL: http://www.mozilla.org/projects/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root

%description
Mozill Firefox is an open-source web browser, designed for standards
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


CPPFLAGS="-I/usr/sfw/include/glib-1.2 -I/usr/sfw/lib/glib/include -I/usr/local/include"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib/ -R/usr/local/lib -L/usr/local/lib/mozilla-1.6 -R/usr/local/lib/mozilla-1.6 -lglib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib:/usr/local/lib/mozilla-1.6"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib:/usr/local/lib/mozilla-1.6"
CC="gcc -03 -pipe -s -fforce-addr"
PATH="/usr/local/lib:/usr/sfw/bin:$PATH"
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH LIBIDL_CONFIG

MOZ_PHOENIX=1
MOZ_FIREBIRD=1 # Don't know if this is/will be in use
MOZ_CALENDAR=0
MOZ_ENABLE_XFT=1
export MOZ_PHOENIX MOZ_CALENDAR MOZ_ENABLE_XFT MOZ_FIREBIRD

./configure \
      --disable-composer \
      --disable-mailnews \
      --disable-calendar \
      --with-default-mozilla-five-home=/usr/local/lib/firefox \
      --with-user-appdir=.firefox \
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
      --disable-ipv6 \
      --with-libidl-prefix=/usr/local

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot} | make install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/local/lib/mozilla-1.6/*
/usr/local/bin/*

%files devel
%defattr(0755,root,root)
/usr/local/include/mozilla-1.6/*
/usr/local/lib/pkgconfig/*
/usr/local/share/*

%changelog
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
