Summary: Mozilla FireFox
Name: mozilla-firefox
Version: 0.9.3
Release: 2
Copyright: GPL
Group: Applications/Internet
# <<<<<<< firefox.spec
Source: firefox-0.9.3-source.tar.bz2
# =======
# Source: firefox-%{version}-source.tar.bz2
# >>>>>>> 1.4
URL: http://www.mozilla.org/projects/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Jonatahan Kaczynski <jmkacz@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: make

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

CC="gcc"
CFLAGS="-O2 -pipe -s -fforce-addr"
CXX="g++"
CPPFLAGS="-I/usr/sfw/include/glib-1.2 -I/usr/sfw/lib/glib/include -I/usr/local/include"
LDFLAGS="-L/usr/sfw/lib -R/usr/sfw/lib -L/usr/local/lib/ -R/usr/local/lib -lglib"
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib"
PATH="/usr/ccs/bin:/usr/local/lib:/usr/sfw/bin:$PATH"
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export CPPFLAGS LDFLAGS LD_LIBRARY_PATH LD_RUN_PATH CC PATH LIBIDL_CONFIG CFLAGS CXX

MOZ_PHOENIX=1
MOZ_FIREBIRD=1 # Don't know if this is/will be in use
MOZ_CALENDAR=0
MOZ_ENABLE_XFT=1
export MOZ_PHOENIX MOZ_CALENDAR MOZ_ENABLE_XFT MOZ_FIREBIRD

# added the --enable-single-profile option to "fix"
# Bugzilla Bug 247847 (libprofile.so fails compile/install)

./configure \
      --enable-single-profile \
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

gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
# <<<<<<< firefox.spec
gmake install DESTDIR=%{buildroot}
# =======
# make install DESTDIR=%{buildroot} | make install DESTDIR=%{buildroot}
# >>>>>>> 1.4


%clean
#%{__rm} -rf %{buildroot}

%files
%defattr(0755,root,root)
/usr/local/bin/*

%files devel
%defattr(0755,root,root)
/usr/local/lib/pkgconfig/*
/usr/local/share/*

%changelog
* Mon Aug 23 2004 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 0.9.3-X
- Updated to latest Mozilla source tree (as of 8/20/2004).
- Changed CC line from -03 (zero 3) to -O2 (o 2)

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
