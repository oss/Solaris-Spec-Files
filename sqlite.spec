%define	name	sqlite
%define	version	3.5.9
 
Name:		%{name} 
Version:	%{version} 
Release:	1
Vendor:		www.sqlite.org
License:	LGPL 
Group:		System Environment/Libraries 
Source:		http://www.sqlite.org/%{name}-%{version}.tar.gz 
BuildRoot:	%{_tmppath}/%{name}-buildroot 
Summary:	Calorie-saving SQL library
Requires:	%{name}-lib = %{version} readline5
BuildRequires:	ncurses, readline5

%description 
SQLite is a small C library that implements a self-contained, 
embeddable, zero-configuration SQL database engine. The SQLite
distribution comes with a standalone command-line access program 
(sqlite) that can be used to administer an SQLite database and
which serves as an example of how to use the SQLite library.

%package devel 
Group: Development/Libraries 
Summary: Include files needed for development with SQLite 
Requires: %{name}-lib = %{version}

%package doc
Group: Documentation
Summary: User documentation for SQLite
Conflicts: %{name} < %{version} %{name} > %{version}

%package lib
Group: System/Libraries
Summary: Shared library for SQLite

%description devel
The sqlite-devel package contains the files necessary for development with 
the SQLite libraries. 

%description doc
The sqlite-doc package contains the useguide and reference of SQLite 
and can be installed even if SQLite main package is not installed

%description lib
The sqlite-lib package contains the shared libraries for SQLite.

%prep
%setup -q
 
%build 
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CXXFLAGS="-g -xs" CFLAGS="-g -xs" LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS CXXFLAGS CFLAGS

./configure \
	--enable-threadsafe \
	--enable-debug \
	--disable-tcl

gmake -j3 \
	LIBREADLINE='-L/usr/local/lib -R/usr/local/lib -rpath /usr/local/lib -lncurses -lreadline -lrt' \
	READLINE_FLAGS='-DHAVE_READLINE=1 -I/usr/local/include/readline -I/usr/local/include' LIBPTHREAD='-lpthread -lrt'

%install 
rm -rf "$RPM_BUILD_ROOT"
PATH="/usr/sfw/bin:/usr/local/gnu/bin:/usr/local/bin:/usr/ccs/bin:/usr/bin:/opt/SUNWspro/bin:/usr/ucb:/usr/openwin/bin:/usr/sbin" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
CXXFLAGS="-g -xs" CFLAGS="-g -xs" LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS CXXFLAGS CFLAGS

gmake DESTDIR="$RPM_BUILD_ROOT" LIBREADLINE='-L/usr/local/lib -R/usr/local/lib -rpath /usr/local/lib -lncurses -lreadline -lrt' \
	READLINE_FLAGS='-DHAVE_READLINE=1 -I/usr/local/include/readline -I/usr/local/include' LIBPTHREAD='-lpthread -lrt' install
rm -rf "$RPM_BUILD_ROOT/%{_docdir}/sqlite-%{version}"
rm -rf $RPM_BUILD_ROOT/usr/local/lib/libsqlite3.la

%clean 
rm -rf $RPM_BUILD_ROOT 
 
%files 
%defattr(-,root,root) 
%{_bindir}/*
%doc doc/*
 
%files devel 
%defattr (-,root,root) 
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/sqlite3.pc

%files lib
%defattr (-,root,root)
%{_libdir}/lib*.so*

%changelog
* Fri Jun 13 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.5.9-1
- Updated to version 3.5.9
* Mon Dec 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.5.4
- Bumpt to 3.5.4
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.5.1
- Bump to 3.5.1
* Sat Sep 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.4.2
- Patched and bumped this ridiculous package 
* Fri Jan 6 2006 Aaron Richton <richton@nbcs.rutgers.edu>
- Rutgers/Solarisize
