Summary: Command line utility to retrieve URLs
Name: curl
Version: 7.10.7
Release: 1
Group: Applications/Internet
Copyright: MIT/X derivate license
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Requires: openssl zlib
#BuildRequires: zlib-devel
Provides: curl
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
#CC='/opt/SUNWspro/bin/cc' 
#CXX='/opt/SUNWSpro/bin/CC'
LDFLAGS='-L/usr/ssl/lib -R/usr/ssl/lib -L/usr/local/lib -R/usr/local/lib'
LD_LIBRARY_PATH="/usr/sfw/lib:/usr/local/lib"
LD_RUN_PATH="/usr/sfw/lib:/usr/local/lib"

#export CC
#export CXX
export LDFLAGS
export LD_LIBRARY_PATH
export LD_RUN_PATH

./configure --prefix=/usr/local --with-ssl=/usr/local/ssl
make

%install 
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/curl
/usr/local/bin/curl-config
/usr/local/man/man3/*
/usr/local/man/man1/*
/usr/local/include/curl/*
%dir /usr/local/include/curl
/usr/local/lib/*
/usr/local/share/curl/curl-ca-bundle.crt

%doc README CHANGES SSLCERTS COPYING
