Name:		libgcrypt
Version:	1.2.4
Release:	1
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
License:	LGPL
Summary:	A general-purpose cryptography library.
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libgpg-error-devel pkgconfig
Group:		System Environment/Libraries

%package devel
Summary: Development files for the %{name} package.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This is a development version.

%description devel
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This package contains files needed to develop
applications using libgcrypt.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--prefix="/usr/local" \
	--disable-asm \
	--disable-nls

gmake -j3
#gmake check

%install
rm -fr $RPM_BUILD_ROOT

gmake DESTDIR=%{buildroot} install

rm -f ${RPM_BUILD_ROOT}/usr/local/share/info/dir ${RPM_BUILD_ROOT}/%{_libdir}/*.la

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*
/usr/local/share/info/gcrypt.info*

%changelog
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.2.4-1
- Bump to 1.2.4
