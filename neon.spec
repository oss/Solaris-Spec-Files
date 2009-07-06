Name: 		neon
Version: 	0.28.4
Release: 	1
License: 	LGPL
Group: 		System Environment/Libraries
URL:		http://www.webdav.org/neon
Source: 	http://www.webdav.org/neon/neon-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: 	openssl >= 0.9.8

BuildRequires: 	expat-devel, openssl >= 0.9.8

Summary:	HTTP and WebDAV client library	

%description
neon is an HTTP and WebDAV client library, with a C interface. 

Features:

    * High-level wrappers for common HTTP and WebDAV operations (GET, MOVE, DELETE, etc)
    * Low-level interface to the HTTP request/response engine
    * Authentication support including Basic and Digest support, along with GSSAPI-based Negotiate
    * SSL/TLS support
    * Abstract interface to parsing XML
    * WebDAV metadata support

%package devel
Group:		System Environment/Libraries
Requires:	neon = %{version}-%{release}

Summary:	neon development files

%description devel
This package contains files need for building applications that use neon.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS

./configure \
	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--with-libs=%{_prefix}/ssl      \
	--with-expat 			\
	--with-ssl=openssl 		\
	--enable-shared 		\
	--disable-static		\
	--enable-threadsafe-ssl=posix 	\
	--disable-nls

gmake -j3

%install
gmake install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README NEWS ChangeLog
%doc BUGS TODO AUTHORS THANKS
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%doc doc/html/
%{_bindir}/neon-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/neon-config.1
%{_mandir}/man3/*

%changelog
* Mon Jul 06 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.28.4-1
- Updated to version 0.28.4
- No longer build static libraries
- Fixed some things

* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.25.5-1
- Downgraded to 0.25.5 because of subversion and bmpx requires

* Wed May 03 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.26.0-1
- Cleaned up spec file and broke into devel and binary packages
