Name: 		subversion
Version: 	1.6.15
Release: 	1
License: 	ASL 1.1
Group:          Development/Applications
URL:		http://subversion.apache.org/
Source: 	http://subversion.tigris.org/downloads/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: 	openssl >= 0.9.8l, cyrus-sasl >= 2.1.18-3
Requires:	openldap-lib >= 2.4, db4 >= 4.8
Requires:	apr apr-util python

BuildRequires:	autoconf, libtool, apr-devel, apr-util-devel, zlib-devel
BuildRequires:	db4-devel >= 4.8, openldap-devel >= 2.4, openssl >= 0.9.8l
BuildRequires:	neon-devel, expat-devel, sqlite-devel
BuildRequires:	cyrus-sasl >= 2.1.18-3, gdbm, python

BuildConflicts:	subversion-devel

Summary:	An open source version control system

%description
Subversion is a version control system that is a compelling replacement for CVS.

%package devel  
Group:		Development/Applications
Requires:	subversion = %{version}-%{release}
Summary:	Subversion development files

%description devel
This package contains the development files needed to build applications that
use subversion.

%prep
%setup -q -n subversion-%{version}

%build
%configure \
	--with-neon=%{_prefix}		\
	--disable-nls 			\
	--disable-static		

gmake -j3

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

# Kill .la files
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README CHANGES BUGS COPYING COMMITTERS
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man*/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Thu Jan 04 2011 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.6.15-1
- Updated to 1.6.15
* Thu Apr 08 2010 Steve Lu <sjlu@nbcs.rutgers.edu> - 1.6.9-1
- Updated to version 1.6.9 and is also now known as Apache Subversion
* Fri Jan 08 2010 Russ Frank <rfranknj@nbcs.rutgers.edu> - 1.6.5-2
- Respin against BDB4.8
* Wed Sep 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.5-1
- Updated to version 1.6.5
- Added apr, apr-util to Requires (otherwise apt pulls down apache2 with subversion)
* Tue Aug 11 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.4-1
- Updated to version 1.6.4
* Mon Jul 01 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.3-1
- Updated to version 1.6.3
* Tue Jun 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.6.2-1
- Updated to version 1.6.2
- No longer build static libraries
- Put *.la files in devel package
- Moved *.so symlinks to devel package
* Tue Nov 11 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.5.3-2
- Added db4-devel >= 4.7 to BuildRequires, db4 >= 4.7 to Requires
* Tue Oct 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> 1.5.3-1
- Fixed a few things, built against openldap 2.4, updated to version 1.5.3
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.5.0-2
- Added cyrus-sasl >= 2.1.18-3 requirement
* Tue Jun 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.5.0-1
- Updated to version 1.5.0
* Mon Jan 14 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.4.6-1
- Updated to 1.4.6
* Fri Sep 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.5-1
- Bump to 1.4.5
- Built against neon and got rid of the neon255 require
* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.4.4-1
- Bump to 1.4.4
- Cleaned up spec, set proper requires.
- Turned off db4 since it wasn't using it anyways
* Thu Feb 15 2007 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.3-1
- Updated to 1.4.3
* Fri Dec 08 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.2-2
- Updated for OpenSSL 0.9.8
* Fri Nov 24 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.2-1
- Updated to 1.4.2
* Thu Oct 12 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.4.0-1
- Updated to 1.4.0
- Made subversion depend on seperate apr, apr-util and neon packages
* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.3.1-1
- Updated to 1.3.1, switched to Sun CC, cleaned up spec file, switched to internal neon
