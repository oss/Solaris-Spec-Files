%define _includedir /usr/local/include
%define _libdir /usr/local/lib
%define _mandir /usr/local/man
%define _bindir /usr/local/bin
%define _sharedir /usr/local/share
%define _tmppath /var/tmp

Summary: A CRT screen handling and optimization package.
Name: ncurses
Version: 5.4
Release: 3 
License: GPL
Group: System Environment/Libraries
URL: http://dickey.his.com/ncurses/ncurses.html
Source0: %{name}-%{version}.tar.gz 
BuildRequires: sharutils
BuildRoot: %{_tmppath}/%{name}-%{version} 
Provides: libncurses.so.5

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.

%package devel
Summary: The development files for applications that use ncurses.
Group: Development/Libraries
Requires: ncurses = %{PACKAGE_VERSION}
Obsoletes: ncurses-c++-devel

%description devel
The header files and libraries for developing applications that use
the ncurses CRT screen handling and optimization package.

Install the ncurses-devel package if you want to develop applications
which will use ncurses.

Use the following compiler flags to build against the ncurses library:

-lncurses
(compile and link against the regular ncurses library)

-I %{includedirw} -lncursesw
(compile and link against the wide-character, UTF-8, library)

%prep
%setup -q


%build
./configure --with-install-prefix=${RPM_BUILD_ROOT} --with-shared
gmake

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/ncurses
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}
mkdir -p ${RPM_BUILD_ROOT}%{_sharedir}
gmake install 
cd $RPM_BUILD_ROOT/usr/local
/usr/local/bin/unhardlinkify.py ./


%files
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%{_sharedir}/terminfo
%{_sharedir}/tabset
%{_libdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files devel
%defattr(-,root,root)
%doc test
%doc doc/html/hackguide.html
%doc doc/html/ncurses-intro.html
%doc c++/README*
%{_libdir}/lib*.a
%{_includedir}/ncurses
%{_mandir}/man3/*

%clean
rm -rf ${RPM_BUILD_ROOT}

%changelog
* Wed Jun 22 2005 John M. Santel <jmsl@nbcs.rutgers.edu>
- first RU build, specfile based on latest fedora 4 and latest sources
- removed fedora/redhat patches, let configure assume resonable defaults, 
  which seem to work
