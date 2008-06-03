Summary: 	neon the HTTP and WebDAV client library
Name: 		neon
Version: 	0.28.2
Release: 	1
License: 	LGPL
Group: 		Applications/Internet
Source: 	%{name}-%{version}.tar.gz
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
Requires: 	expat, openssl >= 0.9.8 , libxml2
BuildRequires: 	make, expat, openssl >= 0.9.8, libxml2
BuildRoot: 	/var/tmp/%{name}-%{version}

%description
neon is an HTTP and WebDAV client library, with a C interface. Featuring:
-High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc)
-RFC2617 basic and digest authentication (including auth-int, md5-sess)
-Proxy support (including basic/digest authentication)
-SSL/TLS support (including client certificate support)
-WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL
-WebDAV metadata support: set and remove properties, query any set of properties (PROPPATCH/PROPFIND)

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files for building 
applications which use %{name}.

%package static
Summary: Libraries, includes to develop applications with %{name}.
Group: Applications/Libraries
Requires: %{name}-devel = %{version}

%description static
The %{name}-static package contains the static libraries
for building applications which use %{name}.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--with-expat \
	--with-libxml2 \
	--with-ssl=openssl \
	--with-libs=/usr/local/ssl \
	--enable-shared \
	--enable-threadsafe-ssl=posix
gmake

%install
gmake install DESTDIR=%{buildroot}

# Note this is needed for various packages, like rpm
# rm %{buildroot}/usr/local/lib/libneon.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/neon-config
/usr/local/lib/libneon.so*
/usr/local/share/man/man1/neon-config.1
/usr/local/share/man/man3/*.3
/usr/local/share/doc/*
/usr/local/share/locale/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/*

%files static
/usr/local/lib/*.a
/usr/local/lib/*.la

%changelog
* Tue Jun 3 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.28.2-1
- Updated to version 0.28.2
* Sat Sep 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.27.2-1
- Bump to 0.27.2
* Mon Sep 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.27.1-1
- Bump to 0.27.1
* Wed Sep 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.27.0-2
- Broke out the static package again for rpm deps
* Wed Aug 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.27.0-1
- Upgraded to 0.27.0
* Fri May 05 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.25.5-1
- Downgraded to 0.25.5 because of subversion and bmpx requires
* Wed May 03 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.26.0-1
- Cleaned up spec file and broke into devel and binary packages
