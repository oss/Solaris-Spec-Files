Name: openssl
Version: 0.9.7c
Release: 2
Summary: Secure communications toolkit
Group: Cryptography
License: BSD
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: vpkg-SPROcc 

%description
 The OpenSSL Project is a collaborative effort to develop a robust,
 commercial-grade, fully featured, and Open Source toolkit implementing the
 Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
 protocols as well as a full-strength general purpose cryptography library.
 The project is managed by a worldwide community of volunteers that use the
 Internet to communicate, plan, and develop the OpenSSL toolkit and its
 related documentation. (from README)


%prep
%setup -q

%build
#OpenSSL doesn't seem to honor these.
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
# Huh? These are LDFLAGS, not CFLAGS?
#CFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
# make Configure find sun's cc and ld, seems to like it
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" 
CC="/opt/SUNWspro/bin/cc"
export LDFLAGS CFLAGS PATH CC

%ifarch sparc64

./Configure shared solaris64-sparcv9-cc

#sed "s/-lc )/-lc -R\/usr\/local\/lib\/sparcv9)/" Makefile.ssl > Makefile.ssl2
#mv Makefile.ssl2 Makefile.ssl
LIBCRYPTO="-R/usr/local/lib/sparcv9 -L.. -lcrypto"
LIBSSL="-R/usr/local/lib/sparcv9 -L.. -lssl"
export LIBCRYPTO LIBSSL
make -e 
make -e test
umask 022
mkdir -p sparcv9/include/openssl
mv libssl.a sparcv9/libssl.a
mv libcrypto.a sparcv9/libcrypto.a
mv libssl.so* libcrypto.so* sparcv9/
set +e; cp include/openssl/* sparcv9/include/openssl; set -e
# rm sparcv9/include/openssl/rsaref.h
make clean
#sed "s/-lc -R\/usr\/local\/lib\/sparcv9)/-lc )/" Makefile.ssl > Makefile.ssl2
#mv Makefile.ssl2 Makefile.ssl
%endif

./Configure shared solaris-sparcv8-cc
#sed "s/-lc )/-lc -R\/usr\/local\/lib)/" Makefile.ssl > Makefile.ssl2
#mv Makefile.ssl2 Makefile.ssl
LIBCRYPTO="-R/usr/local/lib -L.. -lcrypto"
LIBSSL="-R/usr/local/lib -L.. -lssl"
export LIBCRYPTO LIBSSL
make -e
make -e test

%install
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
CFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
# make Configure find sun's cc and ld, seems to like it
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" 
CC="/opt/SUNWspro/bin/cc"
export LDFLAGS CFLAGS PATH CC
# weird can't write this by default
chmod 755 %{buildroot}/usr/local/ssl/lib/pkgconfig && true
rm -fr %{buildroot}
make install INSTALL_PREFIX=%{buildroot}
chmod 755 %{buildroot}/usr/local/ssl/lib/pkgconfig && true

%ifarch sparc64
umask 022
mkdir -p %{buildroot}/usr/local/ssl/sparcv9/lib
mkdir -p %{buildroot}/usr/local/ssl/sparcv9/include/openssl
mkdir -p %{buildroot}/usr/local/lib/sparcv9/
install -m 0644 sparcv9/*.a %{buildroot}/usr/local/ssl/sparcv9/lib
install -m 0644 sparcv9/include/openssl/* \
    %{buildroot}/usr/local/ssl/sparcv9/include/openssl
install -m 0644 sparcv9/*.so* %{buildroot}/usr/local/lib/sparcv9/
%endif

mkdir -p %{buildroot}/usr/local/lib
mv %{buildroot}/usr/local/ssl/lib/*so* %{buildroot}/usr/local/lib
mv -f libcrypto*so* %{buildroot}/usr/local/lib
%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
/usr/local/ssl/*
/usr/local/lib/*
