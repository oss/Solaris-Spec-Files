Summary:	Perl Compatible Regexp Library
Name:	 	pcre
Version:	7.7
Release:	1
Copyright:	GPL
Group:		Applications/Productivity
URL:		http://www.pcre.org
Vendor:		pcre
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-root

%description
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h. The official POSIX name is
regex.h, but I didn't want to risk possible problems with existing files of
that name by distributing it that way. To use it with an existing program that
uses the POSIX API, it will have to be renamed or pointed at by a link.

%package devel
Summary:	Development headers, documentation, and libraries for PCRE
Group:		Applications/Productivity
Requires:	%{name} = %{version}
Requires:	pkgconfig

%description devel
Development headers, documentation, and libraries for PCRE

%prep
%setup -q 

%build
CC='cc' CXX='CC' \
CFLAGS='' CXXFLAGS='' \
LDFLAGS='-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
export CC CXX CFLAGS CXXFLAGS LDFLAGS CPPFLAGS PATH

./configure --prefix="/usr/local"

gmake -j3

%install
rm -rf %{buildroot}

gmake DESTDIR=%{buildroot} install
gmake test

rm -rf %{buildroot}/usr/local/lib/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/bin/*
/usr/local/lib/*.so*

%files devel
/usr/local/include/*
/usr/local/lib/libpcre.a
/usr/local/lib/libpcrecpp.a
/usr/local/lib/libpcreposix.a
/usr/local/lib/pkgconfig/libpcre.pc
/usr/local/lib/pkgconfig/libpcrecpp.pc
/usr/local/share/doc/*
/usr/local/share/man/man1/*
/usr/local/share/man/man3/*

%changelog
* Wed Jun 18 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.7-1
- Updated to version 7.7
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.4-1
- Bump to 7.4
* Mon Jan 16 2006 Eric Rivas <kc2hmv@nbcs.rutgers.edu>
- Upgraded to version 6.4
* Fri May 16 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
- Initial Rutgers RPM
