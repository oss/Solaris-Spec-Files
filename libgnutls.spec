Name: libgnutls
Version: 0.8.6
Release:  3
Summary: GNU TLS lib
Source: gnutls-%{version}.tar.gz
Copyright: GPL
Group: System Environment/Libraries
BuildRoot: /var/tmp/%{name}-root
Conflicts: gnutls
Requires: libgcrypt

%description
TLS library with GPL license.

%prep
%setup -q -n gnutls-%{version}


%build
#PATH=/opt/SUNWspro/bin/:$PATH 
#CC=/opt/SUNWspro/bin/cc
#CC=/usr/local/gcc3/bin/gcc
export PATH CC

LDFLAGS='-L/usr/local/lib -R/usr/local/lib -lsocket -lnsl' ./configure  --prefix=/usr/local --enable-static=yes --enable-shared=yes --with-included-libtasn1
make && exit 0

%install
mkdir -p %{buildroot}/usr/local/lib %{buildroot}/usr/local/include/gnutls
install -m0644 lib/.libs/libgnutls.so %{buildroot}/usr/local/lib/libgnutls.so.5
ln -sf libgnutls.so.5 %{buildroot}/usr/local/lib/libgnutls.so
install -m0644 includes/gnutls/*.h %{buildroot}/usr/local/include/gnutls/
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/include/gnutls/*.h
/usr/local/lib/libgnutls.so*
#/usr/local/share/aclocal/libgnutls-extra.m4
#/usr/local/share/aclocal/libgnutls.m4

