Summary: Cryptokit library for OCaml
Name: ocaml-cryptokit
Version: 1.3
Release: 1
Group: Programming/Languages
License: LGPL
Requires: ocaml >= 3.08 zlib
BuildRequires: ocaml >= 3.08 zlib-devel sed
Source: cryptokit-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Description: cryptographic algorithm library for OCaml - runtime
 The Cryptokit library for Objective Caml provides a variety of
 cryptographic primitives that can be used to implement cryptographic
 protocols in security-sensitive applications.  The primitives provided
 include:

   - Symmetric-key ciphers: AES, DES, Triple-DES, ARCfour,
     in ECB, CBC, CFB and OFB modes.
   - Public-key cryptography: RSA encryption, Diffie-Hellman key agreement.
   - Hash functions and MACs: SHA-1, MD5, and MACs based on AES and DES.
   - Random number generation.
   - Encodings and compression: base 64, hexadecimal, Zlib compression.

 Additional ciphers and hashes can easily be used in conjunction with
 the library.  In particular, basic mechanisms such as chaining modes,
 output buffering, and padding are provided by generic classes that can
 easily be composed with user-provided ciphers.  More generally, the library
 promotes a "Lego"-like style of constructing and composing
 transformations over character streams.

%prep
%setup -q -n cryptokit-%{version}

%build
sed -e 's#^ZLIB_LIBDIR=/usr/lib$#ZLIB_LIBDIR=/usr/local/lib#' Makefile > Makefile.ru
mv Makefile Makefile.orig
mv Makefile.ru Makefile

sed -e 's#^ZLIB_INCLUDE=/usr/include$#ZLIB_INCLUDE=/usr/local/include#' Makefile > Makefile.ru
mv Makefile.ru Makefile

sed -e 's#^INSTALLDIR=\(.*\)$#INSTALLDIR=$(RPM_BUILD_ROOT)/\1#' Makefile > Makefile.ru
mv Makefile.ru Makefile

sed -e 's#\(.*\)stublibs\(.*\)#\1stublibs/\2#' Makefile > Makefile.ru
mv Makefile.ru Makefile

make all

%install
# This is gross, I'd like to get the value from INSTALLDIR in the Makefile but
#  I can't figure out a clean way to do it, or to insert this into the Makefil
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/ocaml
mkdir $RPM_BUILD_ROOT/usr/local/lib/ocaml/stublibs
make install

%clean
rm -rf $RPM_BUILDROOT

%files
%defattr(-,root,root)
/usr/local/lib/ocaml/cryptokit.*
/usr/local/lib/ocaml/libcryptokit.a
/usr/local/lib/ocaml/stublibs/dllcryptokit.so
