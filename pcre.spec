Name:	 	pcre
Version:	7.9
Release:	1
License:	GPL
Group:		System Environment/Libraries
URL:		http://www.pcre.org
Source:		ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Summary:	Perl Compatible Regular Expressions

%description
The PCRE library is a set of functions that implement regular expression pattern matching 
using the same syntax and semantics as Perl 5. PCRE has its own native API, as well as a 
set of wrapper functions that correspond to the POSIX regular expression API. The PCRE 
library is free, even for building commercial software.

%package devel
Group:		System Environment/Libraries
Requires:	pcre = %{version}-%{release}
Requires:	pkgconfig

Summary:        Development files for PCRE

%description devel
This package contains files and documentation for devlopment with PCRE.

%prep
%setup -q 

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include"
LDFLAGS="-L/usr/local/ssl/lib -R/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure --prefix=%{_prefix} --mandir=%{_mandir} --docdir=%{_docdir}/pcre-%{version} --disable-static
gmake -j3
gmake test

%install
rm -rf %{buildroot}

gmake install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)

%docdir %{_docdir}/pcre/
%dir %{_docdir}/pcre-%{version}/
%{_docdir}/pcre-%{version}/AUTHORS
%{_docdir}/pcre-%{version}/COPYING
%{_docdir}/pcre-%{version}/ChangeLog
%{_docdir}/pcre-%{version}/LICENCE
%{_docdir}/pcre-%{version}/NEWS
%{_docdir}/pcre-%{version}/README

%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)

%docdir %{_docdir}/pcre-%{version}/
%{_docdir}/pcre-%{version}/*.txt
%{_docdir}/pcre-%{version}/html/

%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%changelog
* Tue May 19 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.9-1
- Updated to version 7.9
- No longer build static libraries
- Corrected man path
- Various minor changes to spec file
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.7-1
- Updated to version 7.7
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.4-1
- Bump to 7.4
* Mon Jan 16 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
- Upgraded to version 6.4
* Fri May 16 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
- Initial Rutgers RPM
