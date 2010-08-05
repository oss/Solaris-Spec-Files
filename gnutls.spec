Name:		gnutls
Version:	2.8.6
Release: 	1
Group:          System Environment/Libraries
URL:		http://www.gnu.org/software/gnutls
Source:		ftp://ftp.gnu.org/pub/gnu/gnutls/gnutls-%{version}.tar.bz2
# The libgnutls library is LGPLv2+, utilities and remaining libraries are GPLv3+
License:	GPLv3+ and LGPLv2+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes:	libgnutls < 2.8.4
Provides:	libgnutls = %{version}-%{release}

BuildRequires:	libgcrypt-devel libgpg-error-devel zlib-devel
BuildRequires:	guile-devel

Summary:	The GNU Transport Layer Security Library 

%description
GnuTLS is a project that aims to develop a library which provides a secure layer, 
over a reliable transport layer. Currently the GnuTLS library implements the 
proposed standards by the IETF's TLS working group.

%package devel
Group:          System Environment/Libraries
Requires:       gnutls = %{version}-%{release}
Requires:       pkgconfig
Summary:        Development files for GnuTLS

%description devel
This package contains files needed to build applications that use GnuTLS.

%package guile
Group:		System Environment/Libraries
Requires:       gnutls = %{version}-%{release}
Summary:	GnuTLS Guile bindings

%description guile
This package contains Guile bindings for the GnuTLS library.

%prep
%setup -q

# Examples fail to compile. We are not packaging them anyways. Just skip them:
# http://mail-index.netbsd.org/pkgsrc-bugs/2009/06/17/msg032744.html
sed -i 's|examples ||' doc/Makefile.in

# Solaris doesn't have <stdint.h> but it has an almost compatible <inttypes.h>
ln -sf /usr/include/inttypes.h lib/includes/stdint.h

%build
#LIBS="-lgpg-error -lnsl"
#export LIBS

%configure \
	--disable-static	\
	--disable-nls

gmake -j3
#gmake check

%install
rm -rf %{buildroot}
gmake install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post
if [ -x %{_bindir}/install-info ]; then

	%{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/gnutls.info
fi

%preun
if [ -x %{_bindir}/install-info ]; then
        %{_bindir}/install-info --delete --info-dir=%{_infodir} %{_infodir}/gnutls.info
fi

%files
%defattr(-, root, root, -)
%doc README AUTHORS COPYING 
%doc NEWS THANKS ChangeLog
%{_bindir}/*
%{_libdir}/libgnutls*.so.*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libgnutls*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%files guile
%defattr(-, root, root)
%{_libdir}/libguile-gnutls*
%{_datadir}/guile/site/*

%changelog
* Wed Aug 04 2010 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.8.6-1
- Updated to version 2.8.6

* Wed Oct 07 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 2.8.4-1
- Updated to version 2.8.4

* Wed Aug 12 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.8.2-1
- Updated to version 2.8.2
- Created guile breakout package

* Wed Jun 10 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.8.0-1
- Updated to version 2.8.0
- No longer build static libraries
- Renamed package to 'gnutls' from 'libgnutls'
- Added 'post' and 'preun' scriptlets
- Cleaned up spec file somewhat

* Fri May 23 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.2.5
- bump to 2.2.5

* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.1.1
- Bump to 2.1.1
