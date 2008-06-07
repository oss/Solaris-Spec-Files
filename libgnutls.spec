Name:		libgnutls
Version:	2.2.5
Release: 	1
Summary:	GNU TLS lib
Source:		gnutls-%{version}.tar.bz2
Copyright:	GPL
Group:		System Environment/Libraries
BuildRoot:	/var/tmp/%{name}-root
Conflicts:	gnutls
Requires:	libgcrypt libgpg-error
BuildRequires:	libgcrypt-devel libgpg-error-devel

%description
TLS library with GPL license.

%package devel
Summary:        Development headers and documentation for GNU TLS
Group:          System Environment/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
Development headers and documentation for GNU TLS

%prep
%setup -q -n gnutls-%{version}


%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CFLAGS="-D__inline__=inline"
export PATH CC CXX CPPFLAGS LD LDFLAGS CFLAGS

./configure \
	--prefix="/usr/local" \
	--enable-static=yes \
	--enable-shared=yes \
	--disable-nls

gmake -j3
#gmake check

%install
rm -rf %{buildroot}

gmake DESTDIR=%{buildroot} install

rm -rf %{buildroot}/usr/local/share/info/dir
rm -rf %{buildroot}/usr/local/lib/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/*
/usr/local/lib/*.so*
/usr/local/share/info/*
/usr/local/share/man/man1/*
/usr/local/share/man/man3/*
/usr/local/share/aclocal/*

%files devel
%defattr(-,root,root)
/usr/local/include/*
/usr/local/lib/pkgconfig/gnutls-extra.pc
/usr/local/lib/pkgconfig/gnutls.pc
/usr/local/lib/*.a

%changelog
* Fri May 23 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.2.5
- bump to 2.2.5
* Sat Oct 06 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.1.1
- Bump to 2.1.1
