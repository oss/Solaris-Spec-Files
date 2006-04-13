%define _libdir /usr/local/lib
%define ffdir %{_libdir}/firefox-%{version}

Summary: Mozilla Firefox
Name: mozilla-firefox
Version: 1.5.0.1
Release: 1
Copyright: MPL/NPL
Group: Applications/Internet
Source: firefox-%{version}-source.tar.bz2
Patch0: firefox-1.5-HellNoGNOME.patch
URL: http://www.mozilla.org/projects/firefox
Distribution: RU-Solaris
Vendor: NBCS-OSS
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: autoconf213 = 2.13
BuildRequires: cairo-devel >= 1.0.2
BuildRequires: expat
BuildRequires: fontconfig-devel
BuildRequires: gtk2-devel
BuildRequires: libIDL2 >= 0.8
BuildRequires: make >= 3.19.1
BuildRequires: perl >= 5.6
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: xft2-devel
BuildRequires: libpng3-devel
Requires: cairo
Requires: expat
Requires: gtk2
Requires: fontconfig
Requires: xft2
Requires: libpng3

# The mozilla devs don't provide a clear picture of what is really necessary
# to build firefox (http://www.mozilla.org/build/unix.html), so hopefully
# this works
Conflicts: mozilla-firefox-bin
Obsoletes: mozilla-firebird FireFox phoenix nss
Provides: webclient


%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%package devel
Summary: Libraries, includes to develop applications with mozilla-firefox.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The mozilla-firefox-devel package contains the header files and static
libraries for building applications which use mozilla-firefox.

%prep
%setup -q -n mozilla
%patch0 -p1

%build

cat << EOF > .mozconfig
mk_add_options MOZ_CO_PROJECT=browser
mk_add_options MOZ_MAKE_FLAGS=-j8

ac_add_options --enable-application=browser

ac_add_options --enable-optimize="-xO3"
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --enable-xft
ac_add_options --enable-svg
ac_add_options --enable-canvas
ac_add_options --enable-static
ac_add_options --disable-shared
ac_add_options --disable-freetype2
ac_add_options --disable-auto-deps
ac_add_options --enable-official-branding
ac_add_options --enable-default-toolkit=gtk2
ac_add_options --disable-gnomevfs
ac_add_options --disable-gnomeui
ac_add_options --enable-js-ultrasparc
ac_add_options --disable-ldap
ac_add_options --enable-single-profile
ac_add_options --disable-profilesharing

EOF

PATH="/usr/local/gnu/bin:/usr/local/bin:$PATH" \
CC="cc" \
CXX="CC" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lnsl" \
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export PATH CC CXX CPPFLAGS LDFLAGS LIBIDL_CONFIG

# I think configure is dumb, so we have to tell the linker about these
LDFLAGS="${LDFLAGS} -lfontconfig -lXft"
export LDFLAGS

./configure

gmake -f client.mk build


%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}

gmake install DESTDIR=%{buildroot}


# Fix something troublesome
# Hopefully we won't have to run firefox as root the first time
mkdir -p %{buildroot}%{ffdir}/extensions/talkback@mozilla.org
touch %{buildroot}%{ffdir}/extensions/talkback@mozilla.org/chrome.manifest


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0755,root,root)
/usr/local/bin/*
/usr/local/lib/firefox-%{version}

%ghost %{ffdir}/extensions/talkback@mozilla.org/chrome.manifest

%files devel
%defattr(0755,root,root)
/usr/local/share/*
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Wed Mar 15 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.0.1-1
- Updated to 1.5.0.1
- Fixed a lot of build stuff

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

