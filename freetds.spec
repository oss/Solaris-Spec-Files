%define	name	freetds
%define	version	0.63
 
Name: %{name} 
Version: %{version} 
Release: 4
Vendor: www.freetds.org 
License: LGPL 
Group: System Environment/Libraries 
Source: http://ibiblio.org/pub/Linux/ALPHA/freetds/stable/%{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-buildroot 
Summary: FreeTDS is a free re-implementation of the TDS (Tabular DataStream) protocol that is used by Sybase and Microsoft for their database products. 
 
%description 
FreeTDS is a project to document and implement the TDS (Tabular DataStream) 
protocol. TDS is used by Sybase and Microsoft for client to database server 
communications. FreeTDS includes call level interfaces for DB-Lib, CT-Lib, 
and ODBC.  
 
%package devel 
Group: Development/Libraries 
Summary: Include files needed for development with FreeTDS 
Requires: freetds-lib = %{version}

%package doc
Group: Documentation
Summary: User documentation for FreeTDS

%package lib
Group: System/Libraries
Summary: Shared library for FreeTDS

%description devel
The freetds-devel package contains the files necessary for development with 
the FreeTDS libraries. 

%description doc
The freetds-doc package contains the useguide and reference of FreeTDS 
and can be installed even if FreeTDS main package is not installed

%description lib
The freetds-lib package contains the shared libraries for FreeTDS.

%prep
%setup 
 
%build 
LD=/usr/ccs/bin/ld CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/CC CXXFLAGS='-g -xs' CFLAGS='-g -xs' CPPFLAGS='-I/usr/local/include' LDFLAGS='-L/usr/local/lib -R/usr/local/lib' ./configure --with-tdsver=4.2 --prefix=/usr/local --disable-odbc --disable-libiconv --enable-msdblib
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
 
%install 
rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install
rm -rf "$RPM_BUILD_ROOT/%{_docdir}/freetds-%{version}"

%clean 
rm -rf $RPM_BUILD_ROOT 
 
%files 
%defattr(-,root,root) 
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO 
%{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/*
 
%files devel 
%defattr (-,root,root) 
%{_includedir}/*
%{_libdir}/libct.a
%{_libdir}/libsybdb.a
%{_libdir}/libtds.a
%{_libdir}/libtdssrv.a

%files doc
%defattr (-,root,root)
%doc doc/doc/freetds-%{version}/userguide doc/images doc/doc/freetds-%{version}/reference
%doc /usr/local/share/doc/%{name}-%{version}/*

%files lib
%defattr (-,root,root)
%{_libdir}/lib*.so*
#%{_libdir}/libct.so*
#%{_libdir}/libsybdb.so*
#%{_libdir}/libtds.so*
#%{_libdir}/libtdssrv.so*

%changelog 
* Thu Sep 15 2005 Aaron Richton <richton@nbcs.rutgers.edu>
- Rutgers/Solarisize

* Thu Sep 09 2004 Frediano Ziglio <freddy77@angelfire.com>
- remove dependency from freetds-unixodbc
- fix field name (Copyright instead of License)
- updated URL

* Sun Mar 30 2003 Frediano Ziglio <freddy77@angelfire.com>
- add reference to doc package

* Wed Feb  5 2003 Ian Grant <Ian.Grant@cl.cam.ac.uk>
- 0.61 tweaked. Added libtdssrv libraries and tools in /usr/bin + man pages

* Sun Dec 30 2002 David Hollis <dhollis@davehollis.com>
- 0.60 tweaked.  Move .a & .la files to -devel package

* Thu Dec 20 2001 Brian Bruns <camber@ais.org> 
- Modifications for 0.53 ver and removing interfaces file

* Wed Jun 28 2001 Brian Bruns <camber@ais.org> 
- Modifications for 0.52 ver and ODBC drivers 

* Wed Feb 14 2001 David Hollis <dhollis@emagisoft.com> 
- First stab at RPM for 0.51 ver 
