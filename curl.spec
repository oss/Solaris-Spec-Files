Summary:	Command line utility to retrieve URLs
Name:		curl
Version:	7.18.2
Release:	1
Group:		Applications/Internet
License:	MIT/X derivate license
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	openssl zlib
Provides:	curl
%description
cURL (or simply just 'curl') is a command line tool for getting or sending
files using URL syntax. The name is a play on 'Client for URLs', originally
with URL spelled in uppercase to make it obvious it deals with URLs. The
fact it can also be pronounced 'see URL' also helped, it works as an
abbrivation for "Client URL Request Library" or why not the recursive
version: "Curl is a URL Request Library".
 
Curl supports a range of common Internet protocols, currently including
HTTP, HTTPS, FTP, FTPS, GOPHER, LDAP, DICT, TELNET and FILE.
 
%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -Bdirect -zdefs" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=/usr/local --with-ssl=/usr/local/ssl --disable-nls

gmake -j3

%install 
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}/usr/local/lib/libcurl.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/local/bin/curl
/usr/local/bin/curl-config
/usr/local/share/*
/usr/local/include/curl/*
%dir /usr/local/include/curl
/usr/local/lib/*

%doc README CHANGES docs/SSLCERTS COPYING

%changelog
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
