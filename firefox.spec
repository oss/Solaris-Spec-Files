%define _libdir /usr/local/lib
%define ffdir %{_libdir}/firefox-%{version}

Summary: Mozilla Firefox
Name: mozilla-firefox
Version: 2.0.0.14
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
BuildRequires: cairo-devel >= 1.4.10
BuildRequires: expat-devel >= 2.0.0
BuildRequires: fontconfig-devel >= 2.4.2
BuildRequires: gtk2-devel >= 2.11.6
BuildRequires: libIDL2 >= 0.8.9
BuildRequires: libpng3-devel >= 1.2.8
BuildRequires: make >= 3.19.1
BuildRequires: perl >= 5.6
BuildRequires: pkgconfig >= 0.22
BuildRequires: xft2-devel >= 2.1.7
BuildConflicts: nss
BuildConflicts: nspr
Requires: cairo >= 1.4.10
Requires: expat >= 2.0.0
Requires: gtk2 >= 2.11.6
Requires: libIDL2 >= 0.8.9
Requires: fontconfig >= 2.4.2
Requires: xft2 >= 2.1.7
Requires: libpng3 >= 1.2.8
Requires: hicolor-icon-theme >= 0.9
Obsoletes: mozilla-firebird FireFox phoenix mozilla-firefox-bin
Provides: webclient firefox

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%package devel
Summary: Libraries, includes to develop applications with mozilla-firefox.
Group: Applications/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The mozilla-firefox-devel package contains the header files and static
libraries for building applications which use mozilla-firefox.

%prep
%setup -q -n mozilla
%patch0 -p1

%build

cat << EOF > .mozconfig
#
# See http://www.mozilla.org/build/ for build instructions.
#

# Options for client.mk.
mk_add_options MOZ_CO_PROJECT=browser
mk_add_options MOZ_MAKE_FLAGS=-j8

# Options for 'configure' (same as command-line options).
ac_add_options --enable-application=browser
ac_add_options --enable-xft
ac_add_options --enable-svg
ac_add_options --enable-canvas
ac_add_options --enable-static
ac_add_options --enable-optimize=-xO3
ac_add_options --enable-official-branding
ac_add_options --enable-default-toolkit=gtk2
ac_add_options --enable-system-cairo
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --disable-shared
ac_add_options --disable-auto-deps
ac_add_options --disable-freetype2
ac_add_options --disable-gnomevfs
ac_add_options --disable-gnomeui
ac_add_options --disable-nls

EOF

PATH="/usr/local/gnu/bin:/usr/local/bin:/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" \
CC="cc" \
CXX="CC" \
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -lnsl" \
LIBIDL_CONFIG=/usr/local/bin/libIDL-config-2
export PATH CC CXX CPPFLAGS LDFLAGS LIBIDL_CONFIG

./configure

gmake distclean
gmake -f client.mk build


%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}

gmake install DESTDIR=%{buildroot}


# Fix something troublesome
# Hopefully we won't have to run firefox as root the first time
mkdir -p %{buildroot}%{ffdir}/extensions/talkback@mozilla.org
touch %{buildroot}%{ffdir}/extensions/talkback@mozilla.org/chrome.manifest

# Make a symlink so stupid things don't happen
cd %{buildroot}/%{_libdir}
ln -s firefox-%{version} firefox

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0755,root,root)
/usr/local/bin/*
/usr/local/lib/firefox-%{version}
/usr/local/lib/firefox

%files devel
%defattr(0755,root,root)
/usr/local/share/*
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%changelog
* Sat Mar 29 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.0.0.13-1
- Updated to latest version 2.0.0.13

* Fri Feb 08 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.0.0.12-1
- Updated to latest version 2.0.0.12

* Sun Nov 18 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0.9-2
- Respin against gettext 0.17

* Thu Nov 01 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0.9-1
- Bump to 2.0.0.9

* Fri Oct 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.0.0.8-1
- Bump to 2.0.0.8

* Tue Jul 31 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0.0.6-1
- Update to 2.0.0.6.

* Thu Jul 19 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0.0.5-1
- Update to 2.0.0.5.

* Thu Jul 12 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0.0.4-3
- Made devel package require specific release

* Wed May 16 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0.0.3-2
- Build against latest gtk
- Clean up build

* Wed Mar 21 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0.0.3-1
- Updated to 2.0.0.3

* Fri Oct 27 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 2.0-1
- Updated to 2.0

* Wed Aug 23 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.0.6-2
- Updated to 1.5.0.6

* Mon Jun 05 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.0.4-2
- Updated to 1.5.0.4

* Tue May 05 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.0.3-1
- Updated to 1.5.0.3

* Fri Apr 14 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.0.2-1
- Updated to 1.5.0.2

* Wed Apr 12 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 1.5.0.1-1
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

