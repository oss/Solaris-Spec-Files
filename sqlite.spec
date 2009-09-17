Name:		sqlite
Version:	3.6.17
Release:	1
Group:          System Environment/Libraries
License:	LGPL
URL:		http://www.sqlite.org
Source:		http://www.sqlite.org/sqlite-%{version}.tar.gz 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	sqlite-lib = %{version}-%{release}

BuildRequires:	ncurses-devel, readline5-devel

BuildConflicts:	sqlite-devel

Summary:	Embedded SQL database engine

%description 
SQLite is a small C library that implements a self-contained, 
embeddable, zero-configuration SQL database engine. The SQLite
distribution comes with a standalone command-line access program 
(sqlite) that can be used to administer an SQLite database and
which serves as an example of how to use the SQLite library.

%package lib
Group:		System Environment/Libraries
Summary:	SQLite shared library

%description lib
This package contains the shared SQLite library.

%package devel 
Group:		System Environment/Libraries 
Requires:	sqlite-lib = %{version}-%{release}
Summary:	SQLite development files

%description devel
This package contains files needed to build applications that use SQLite.

%prep
%setup -q
 
%build 
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
CFLAGS="-g -xs" CXXFLAGS="${CFLAGS}"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS CFLAGS CXXFLAGS LDFLAGS

./configure \
	--enable-threadsafe	\
	--enable-debug		\
	--disable-static	\
	--disable-tcl

gmake -j3

%install 
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

%clean 
rm -rf %{buildroot}
 
%files 
%defattr(-, root, root)
%doc README VERSION
%{_bindir}/*
 
%files devel 
%defattr (-, root, root) 
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/sqlite3.pc

%files lib
%defattr (-, root, root)
%{_libdir}/lib*.so.*

%changelog
* Wed Sep 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.6.17-1
- Updated to version 3.6.17
- Cleaned things up somewhat
* Wed Aug 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 3.6.1-1
- Updated to version 3.6.1
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
