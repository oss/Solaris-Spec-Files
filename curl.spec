# Define the _lite_edition macro to build curllite:
#    
#    rpmbuild -ba --define '_lite_edition 1' curl.spec
#

%define lite %{?_lite_edition:1}%{!?_lite_edition:0}

%if %{lite}
Name:		curllite
%else
Name:		curl
%endif

Version:	7.19.6
Release:	3
Group:		Applications/Internet
License:	MIT/X derivate license
URL:		http://curl.haxx.se
Source:		http://curl.haxx.se/download/curl-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%if %{lite}

BuildRequires:  openssl
BuildConflicts: heimdal-lib
Provides:       curl
Summary:	Command line utility to retrieve URLs (lite edition)

%description
This is a stripped-down version of cURL, a command line tool for
getting or sending files using URL syntax.

%else

Requires:	openldap-lib >= 2.4 libidn >= 1.15
BuildRequires:	openssl zlib-devel cyrus-sasl openldap-devel >= 2.4 libidn >= 1.15
Conflicts:	curllite
Summary:        Command line utility to retrieve URLs

%description
cURL (or simply just 'curl') is a command line tool for getting or sending
files using URL syntax. The name is a play on 'Client for URLs', originally
with URL spelled in uppercase to make it obvious it deals with URLs. The
fact it can also be pronounced 'see URL' also helped, it works as an
abbreviation for "Client URL Request Library" or why not the recursive
version: "Curl is a URL Request Library".

Curl supports a range of common Internet protocols, currently including
HTTP, HTTPS, FTP, FTPS, GOPHER, LDAP, DICT, TELNET and FILE.

%endif

%package devel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Summary:        %{name} development files

%description devel
This package contains files needed to build applications that use %{name}.
 
%prep
%setup -q -n curl-%{version}

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -B direct -z defs"
PKG_CONFIG_PATH="/usr/local/ssl/lib/pkgconfig"
export PATH CC CXX CPPFLAGS LDFLAGS PKG_CONFIG_PATH

%if %{lite}

./configure \
        --prefix=%{_prefix}     \
        --mandir=%{_mandir}     \
        --disable-static        \
        --with-pic              \
        --with-ssl              \
        --without-krb5          \
        --without-gssapi        \
        --without-zlib          \
        --without-libssh2       \
        --without-sasl          \
        --without-gnutls        \
        --without-libidn        \
        --without-nss           \
        --disable-ldap          \
        --disable-ldaps         \
        --disable-nls

%else

./configure \
	--prefix=%{_prefix}	\
	--mandir=%{_mandir}	\
	--disable-static	\
	--with-pic		\
	--with-ssl		\
	--disable-nls

%endif

gmake -j3

%install 
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README CHANGES docs/SSLCERTS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/curl/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcurl.pc
%{_mandir}/man3/*

%changelog
* Wed Oct 14 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.6-3
- Added '-B direct' back in
- Added libidn >= 1.15 to Requires, BuildRequires
* Wed Oct 14 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.6-2
- Removed '-B direct' from LDFLAGS (libidn symbol issue)
* Wed Sep 02 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.6-1
- Updated to version 7.19.6
- Integrated curllite into this spec file
* Mon May 11 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.4-2
- Added Conflicts: curllite
* Mon Mar 09 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.4-1
- Updated to version 7.19.4
- Added PKG_CONFIG_PATH for openssl
* Mon Oct 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.0-1
- Built against openldap 2.4, added devel package, updated to version 7.19.0
* Fri Jun 20 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.18.2-1
- Updated to version 7.18.2
* Mon Mar 17 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 7-18.0-1
- Updated to 7.18.0
* Wed Nov 14 2007 John DiMatteo <jdimatteo@nbcs.rutgers.edu> - 7-17.1-1
- Bump to 7.17.1
* Sat Sep 29 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 7.17.0-1
- Bump to 7.17.0
* Wed Aug 22 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 7.16.4-1
 - Updated to the latest version.
