Name:		libgcrypt
Version:	1.4.6
Release:	2
Group:          System Environment/Libraries
URL:		http://directory.fsf.org/project/libgcrypt
Source:		ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
License:	LGPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	libgpg-error-devel pkgconfig

Summary:        A general purpose cryptography library.

%description
Libgcrypt is a general purpose cryptographic library based on the code from GnuPG. 
It provides functions for all cryptograhic building blocks: symmetric ciphers (AES, 
DES, Blowfish, CAST5, Twofish, Arcfour), hash algorithms (MD4, MD5, RIPE-MD160, 
SHA-1, TIGER-192), MACs (HMAC for all hash algorithms), public key algorithms (RSA, 
ElGamal, DSA), large integer functions, random numbers and a lot of supporting 
functions. 

%package devel
Group:		System Environment/Libraries
Requires: 	libgcrypt = %{version}-%{release}
Summary: 	Development files for libgcrypt

%description devel
This package contains files needed to develop applications that use libgcrypt.

%prep
%setup -q

%build
%configure \
	--disable-static	\
	--disable-asm 		\
	--disable-nls

gmake -j3
#gmake check

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_infodir}/dir %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post devel
if [ -x %{_bindir}/install-info ]; then
	%{_bindir}/install-info --info-dir=%{_infodir} \
		%{_infodir}/gcrypt.info
fi

%preun devel
if [ -x %{_bindir}/install-info ]; then
	%{_bindir}/install-info --delete --info-dir=%{_infodir} \
		%{_infodir}/gcrypt.info
fi

%files
%defattr(-, root, root)
%doc README COPYING NEWS ChangeLog
%doc AUTHORS THANKS TODO VERSION
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/aclocal/*
%{_infodir}/*

%changelog
* Wed Aug 04 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.4.6-2
- Fix scriptlets

* Wed Aug 04 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 1.4.6-1
- Updated to version 1.4.6

* Wed Jun 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.4.4-1
- Updated to version 1.4.4
- No longer build static libraries
- Fixed info path
- Added post, preun scriptlets
- Added some docs
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 1.4.1-1
- bump
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.2.4-1
- Bump to 1.2.4
