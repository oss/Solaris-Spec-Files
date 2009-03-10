Summary:	Command line utility to retrieve URLs
Name:		curl
Version:	7.19.4
Release:	1
Group:		Applications/Internet
License:	MIT/X derivate license
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	openssl zlib cyrus-sasl openldap-lib >= 2.4
BuildRequires:	openssl zlib-devel cyrus-sasl openldap-devel >= 2.4

%description
cURL (or simply just 'curl') is a command line tool for getting or sending
files using URL syntax. The name is a play on 'Client for URLs', originally
with URL spelled in uppercase to make it obvious it deals with URLs. The
fact it can also be pronounced 'see URL' also helped, it works as an
abbreviation for "Client URL Request Library" or why not the recursive
version: "Curl is a URL Request Library".
 
Curl supports a range of common Internet protocols, currently including
HTTP, HTTPS, FTP, FTPS, GOPHER, LDAP, DICT, TELNET and FILE.

%package devel
Summary:	curl header files and static libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files and static libraries for
curl. Install this package if you want to write or compile a
program that needs curl.
 
%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -Bdirect -zdefs"
PKG_CONFIG_PATH="/usr/local/ssl/lib/pkgconfig/"
export PATH CC CXX CPPFLAGS LD LDFLAGS PKG_CONFIG_PATH

./configure \
	--prefix=%{_prefix}	\
	--mandir=%{_mandir}	\
	--with-ssl		\
	--disable-nls

gmake -j3

%install 
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,bin)
%{_bindir}/*
%{_libdir}/*.so*
%{_mandir}/man1/*
%doc README CHANGES docs/SSLCERTS COPYING

%files devel
%defattr(-,root,root)
%{_includedir}/curl
%{_libdir}/*.a
%{_libdir}/pkgconfig/libcurl.pc
%{_mandir}/man3/*

%changelog
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
