%include machine-header.spec

Name: openssl
Version: 0.9.6d
Release: 1
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
 related documentation.· (from README)


%prep
%setup -q

%build

%ifarch sparc64
./Configure solaris64-sparcv9-cc
make
make test
umask 022
mkdir -p sparcv9/include/openssl
mv libssl.a sparcv9/libssl.a
mv libcrypto.a sparcv9/libcrypto.a
set +e; cp include/openssl/* sparcv9/include/openssl; set -e
rm sparcv9/include/openssl/rsaref.h
make clean
%endif

./Configure solaris-sparcv8-cc
make
make test

%install
rm -fr %{buildroot}
make install INSTALL_PREFIX=%{buildroot}

%ifarch sparc64
umask 022
mkdir -p %{buildroot}/usr/local/ssl/sparcv9/lib
mkdir -p %{buildroot}/usr/local/ssl/sparcv9/include/openssl
install -m 0644 sparcv9/*.a %{buildroot}/usr/local/ssl/sparcv9/lib
install -m 0644 sparcv9/include/openssl/* \
    %{buildroot}/usr/local/ssl/sparcv9/include/openssl
%endif

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
/usr/local/ssl
