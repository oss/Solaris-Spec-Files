Summary: neon the HTTP and WebDAV client library
Name: neon
Version: 0.24.7
Release: 3
License: LGPL
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
Requires: expat, openssl, libxml2
BuildRequires: make, expat, openssl, libxml2
BuildRoot: /var/tmp/%{name}-%{version}

%description
neon is an HTTP and WebDAV client library, with a C interface. Featuring:
-High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc)
-RFC2617 basic and digest authentication (including auth-int, md5-sess)
-Proxy support (including basic/digest authentication)
-SSL/TLS support (including client certificate support)
-WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL
-WebDAV metadata support: set and remove properties, query any set of properties (PROPPATCH/PROPFIND)

%prep
%setup -q

%build
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH
CC="cc"
LD="ld"
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib"
export PATH CC LD CPPFLAGS LDFLAGS
./configure --with-expat --with-libxml2 --with-ssl --enable-shared
gmake

%install
gmake install DESTDIR=%buildroot
rm %{buildroot}/usr/local/lib/libneon.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/neon-config
/usr/local/include/neon/*.h
/usr/local/lib/libneon*
/usr/local/lib/pkgconfig/neon.pc
/usr/local/man/man1/*.1
/usr/local/man/man3/*.3
/usr/local/share/doc/*
