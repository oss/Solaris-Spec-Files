Name: openssl
Version: 0.9.8d
Release: 1
Summary: Secure communications toolkit
Group: Cryptography
License: BSD
Source0: %{name}-%{version}.tar.gz
URL: http://www.openssl.org
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leo Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: /var/tmp/%{name}-%{version}-root
#BuildRequires: vpkg-SPROcc 

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
# total BS. we should take this up with openssl guys.
# this SHOULD be ./Configure shared solaris64-sparcv9-cc::"-g -xs"
# HOWEVER THIS KILLS THE BUILD! stupid. stupid. stupid.
mv Configure Configure.old
sed s/-xO5/"-g -xs -xO5"/g Configure.old > Configure
chmod u+x Configure

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" 
CC="/opt/SUNWspro/bin/cc"
MAKE="gmake"
export PATH CC MAKE

%ifarch sparc64

./Configure shared solaris64-sparcv9-cc

cd apps
cd ..
LIBCRYPTO="-R/usr/local/lib/sparcv9 -L.. -lcrypto"
LIBSSL="-R/usr/local/lib/sparcv9 -L.. -lssl"
export LIBCRYPTO LIBSSL
gmake -e 
gmake -e test
ls -l libssl.a libcrypto.a *.so*
mkdir -p sparcv9
mv libssl.a sparcv9/libssl.a
mv libcrypto.a sparcv9/libcrypto.a
mv libssl.so* libcrypto.so* sparcv9/
gmake clean
rm -f test/dummytest
cd apps
cd ..
%endif

./Configure shared solaris-sparcv9-cc

cd apps
cd ..
LIBCRYPTO="-R/usr/local/lib -L.. -lcrypto"
LIBSSL="-R/usr/local/lib -L.. -lssl"
export LIBCRYPTO LIBSSL
gmake -e
gmake -e test

%install
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib"
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" 
CC="/opt/SUNWspro/bin/cc"
export LDFLAGS CFLAGS PATH CC
chmod 755 %{buildroot}/usr/local/ssl/lib/pkgconfig && true
rm -fr %{buildroot}
gmake install INSTALL_PREFIX=%{buildroot}
chmod 755 %{buildroot}/usr/local/ssl/lib/pkgconfig && true

%ifarch sparc64
umask 022
mkdir -p %{buildroot}/usr/local/ssl/sparcv9/lib
mkdir -p %{buildroot}/usr/local/ssl/sparcv9/
mkdir -p %{buildroot}/usr/local/lib/sparcv9/
install -m 0644 sparcv9/*.a %{buildroot}/usr/local/ssl/sparcv9/lib
install -m 0644 sparcv9/*.so* %{buildroot}/usr/local/lib/sparcv9/
mkdir -p %{buildroot}/usr/local/ssl/lib/sparcv9
for i in `(cd %{buildroot}/usr/local/lib/sparcv9/; ls *so*)` ; do
    ln -s ../../../lib/sparcv9/$i %{buildroot}/usr/local/ssl/lib/sparcv9/$i
done;
%endif

mkdir -p %{buildroot}/usr/local/lib
mv %{buildroot}/usr/local/ssl/lib/*so* %{buildroot}/usr/local/lib
mv -f libcrypto*so* %{buildroot}/usr/local/lib
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
/usr/local/ssl/lib/libcrypto.so*
/usr/local/ssl/lib/libssl.so*
/usr/local/ssl/lib/engines/*

# Apparently libfips doesn't exist
# http://mail-index.netbsd.org/pkgsrc-changes/2004/12/31/0045.html
#/usr/local/ssl/lib/libfips.so*

/usr/local/ssl/lib/pkgconfig
/usr/local/ssl/man
/usr/local/ssl/misc
/usr/local/ssl/openssl.cnf
/usr/local/ssl/private
/usr/local/lib/libcrypto.so*
/usr/local/lib/libssl.so*
%ifarch sparc64
%dir /usr/local/ssl/sparcv9
/usr/local/ssl/lib/sparcv9
/usr/local/lib/sparcv9/libcrypto.so*
/usr/local/lib/sparcv9/libssl.so*
%endif

%files static
%defattr(-,root,root)
/usr/local/ssl/lib/*.a
%ifarch sparc64
/usr/local/ssl/sparcv9/lib/*.a
%endif

%changelog
* Fri Nov 17 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.8d-1
- Updated to 0.9.8d
* Fri Feb 17 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.7i-1
- Updated to 0.9.7i, switched to GCC from Sun CC.
