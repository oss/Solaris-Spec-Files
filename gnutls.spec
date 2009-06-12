Name:		gnutls
Version:	2.8.0
Release: 	1
Group:          System Environment/Libraries
URL:		http://www.gnu.org/software/gnutls
Summary:        Development headers and documentation for GNU TLS
Source:		ftp://ftp.gnu.org/pub/gnu/gnutls/gnutls-%{version}.tar.bz2
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes:	libgnutls
Provides:	libgnutls

BuildRequires:	libgcrypt-devel libgpg-error-devel zlib-devel

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

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}" 
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
LIBS="-lgpg-error -lnsl"
export PATH CC CXX CPPFLAGS LDFLAGS LIBS

./configure \
	--prefix=%{_prefix} 	\
	--mandir=%{_mandir}	\
	--infodir=%{_infodir}	\
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
if [ -x %{_bindir}/install-info ]; then%defattr(-, root, root)

	%{_bindir}/install-info --info-dir=%{_infodir} %{_infodir}/gnutls.info
fi

%preun
if [ -x %{_bindir}/install-info ]; then
        %{_bindir}/install-info --delete --info-dir=%{_infodir} %{_infodir}/gnutls.info
fi

%files
%defattr(-, root, root)
%doc README AUTHORS COPYING 
%doc NEWS THANKS ChangeLog
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%changelog
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
