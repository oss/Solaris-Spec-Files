Summary:	Command line utility to retrieve URLs (lite version)
Name:		curllite
Version:	7.19.4
Release:	1
Group:		Applications/Internet
License:	MIT/X derivate license
Source:		curl-%{version}.tar.gz
BuildRequires:	openssl
BuildConflicts:	heimdal-lib
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Provides:	curl

%description
This is a stripped-down version of cURL, a command line tool for 
getting or sending files using URL syntax.
 
%package devel
Summary:	curllite header files and developer documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files and develper documentation 
for curllite. Install this package if you want to write or compile a
program that needs curllite.
 
%prep
%setup -q -n curl-%{version}

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
	--disable-static	\
	--with-pic		\
	--with-ssl		\
	--without-krb5		\
	--without-gssapi	\
	--without-zlib		\
	--without-libssh2	\
	--without-sasl		\
	--without-gnutls	\
	--without-libidn	\
	--without-nss		\
	--disable-ldap		\
	--disable-ldaps		\
	--disable-nls		

gmake -j3

%install 
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES docs/SSLCERTS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/curl/
%{_libdir}/libcurl.so
%{_libdir}/pkgconfig/libcurl.pc
%{_mandir}/man3/*

%changelog
* Mon May 11 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 7.19.4-2
- Initial build of curllite
