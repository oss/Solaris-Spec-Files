Name: openssl
Version: 0.9.7d
Release: 0
Summary: Secure communications toolkit
Group: Cryptography
License: BSD
Source0: %{name}-%{version}.tar.gz
# I hope these bugs aren't still outstanding in 7d?
#Patch0: openssl-0.9.7c-bugid770.patch
#Patch1: openssl-0.9.7c-bugid771.patch
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


%package static
Group: Cryptography
Summary: evil .a files
Requires: openssl = %{version}
%description static
This package contains OpenSSL's static libraries. OpenSSL static libraries have 
been proven by scientists to eat babies. Never install these unless you need 
them, in which case you still, in reality, do not need them.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
#OpenSSL doesn't seem to honor these.
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
# Huh? These are LDFLAGS, not CFLAGS?
#CFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
# make Configure find sun's cc and ld, seems to like it
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" 
CC="/opt/SUNWspro/bin/cc"
MAKE="gmake"
export LDFLAGS CFLAGS PATH CC MAKE

%ifarch sparc64

./Configure shared solaris64-sparcv9-cc

#sed "s/-lc )/-lc -R\/usr\/local\/lib\/sparcv9)/" Makefile.ssl > Makefile.ssl2
cd apps
sed "s/-L.. /-L.. -R\/usr\/local\/lib\/sparcv9 /" Makefile.ssl > Makefile.ssl2
mv Makefile.ssl2 Makefile.ssl
cd ..
LIBCRYPTO="-R/usr/local/lib/sparcv9 -L.. -lcrypto"
LIBSSL="-R/usr/local/lib/sparcv9 -L.. -lssl"
export LIBCRYPTO LIBSSL
#gmake -e -j 8 && exit 0
gmake -e 
gmake -e test
ls -l libssl.a libcrypto.a *.so*
mkdir -p sparcv9/include/openssl
mv libssl.a sparcv9/libssl.a
mv libcrypto.a sparcv9/libcrypto.a
mv libssl.so* libcrypto.so* sparcv9/
set +e; cp include/openssl/* sparcv9/include/openssl; set -e
# rm sparcv9/include/openssl/rsaref.h
gmake clean
#sed "s/-lc -R\/usr\/local\/lib\/sparcv9)/-lc )/" Makefile.ssl > Makefile.ssl2
rm -f test/dummytest
cd apps
sed "s/-L.. -R\/usr\/local\/lib\/sparcv9/-L.. /" Makefile.ssl > Makefile.ssl3
mv Makefile.ssl3 Makefile.ssl
cd ..
%endif

./Configure shared solaris-sparcv8-cc
#sed "s/-lc )/-lc -R\/usr\/local\/lib)/" Makefile.ssl > Makefile.ssl2
cd apps
sed "s/-L.. /-L.. -R\/usr\/local\/lib /" Makefile.ssl > Makefile.ssl4
mv Makefile.ssl4 Makefile.ssl
cd ..
LIBCRYPTO="-R/usr/local/lib -L.. -lcrypto"
LIBSSL="-R/usr/local/lib -L.. -lssl"
export LIBCRYPTO LIBSSL
#gmake -e -j 9 && exit 0
gmake -e
gmake -e test

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
gmake install INSTALL_PREFIX=%{buildroot}
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
# make links from the /usr/local/ssl/lib/sparcv9 directory back to 
# /usr/local/lib/sparcv9
mkdir -p %{buildroot}/usr/local/ssl/lib/sparcv9
for i in `(cd %{buildroot}/usr/local/lib/sparcv9/; ls *so*)` ; do
    ln -s ../../../lib/sparcv9/$i %{buildroot}/usr/local/ssl/lib/sparcv9/$i
done;
%endif

mkdir -p %{buildroot}/usr/local/lib
mv %{buildroot}/usr/local/ssl/lib/*so* %{buildroot}/usr/local/lib
mv -f libcrypto*so* %{buildroot}/usr/local/lib
# /usr/local/ssl/lib/$i.so -> /usr/local/lib/$i.so
mkdir -p %{buildroot}/usr/local/ssl/lib
for i in `(cd %{buildroot}/usr/local/lib/; ls *so*)` ; do
    ln -s ../../lib/$i %{buildroot}/usr/local/ssl/lib/$i
done;
%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
/usr/local/ssl/bin
/usr/local/ssl/certs
/usr/local/ssl/include
/usr/local/ssl/lib
/usr/local/ssl/lib/pkgconfig
/usr/local/ssl/man
/usr/local/ssl/misc
/usr/local/ssl/openssl.cnf
/usr/local/ssl/private
%ifarch sparc64
/usr/local/ssl/sparcv9/include
%dir /usr/local/ssl/sparcv9
/usr/local/ssl/lib/sparcv9
%endif
/usr/local/lib/*

%files static
%defattr(-,root,root)
%ifarch sparc64
/usr/local/ssl/sparcv9/lib/*.a
%endif
/usr/local/ssl/lib/*.a
