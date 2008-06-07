Name:		openssl
Version:	0.9.8h
Release:	1
Summary:	Secure communications toolkit
Group:		Cryptography
License:	BSD
Source0:	%{name}-%{version}.tar.gz
Source1:	malloc.mapfile
URL:		http://www.openssl.org
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Diffenbaugh <davediff@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-%{version}-root
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
Requires: %{name} = %{version}
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
#sed s/-xO5/"-g -xs -xO5"/g Configure.old > Configure
sed s/xdepend/xdepend=no/g Configure.old > Configure.old2
sed -e s/-xO5/'-O -Wl,-Bdirect -Wl,-zdefs -g -xs'/g Configure.old2 > Configure
chmod u+x Configure

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" 
CC="/opt/SUNWspro/bin/cc"
MAKE="gmake"
export PATH CC MAKE

%ifarch sparc64
LDFLAGS="$LDFLAGS -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9 -rpath/usr/local/ssl/lib/sparcv9 -M%{SOURCE1} -L.. -lcrypto -lssl -lnsl -lsocket -lc"
export LDFLAGS

./Configure -L/usr/local/ssl/lib/sparcv9 -R/usr/local/ssl/lib/sparcv9 -M%{SOURCE1} -lcrypto -lc shared solaris64-sparcv9-cc

cd apps
cd ..
LIBCRYPTO="-R/usr/local/ssl/lib/sparcv9 -L.. -lcrypto -lnsl -lsocket -lc"
LIBSSL="-R/usr/local/ssl/lib/sparcv9 -L.. -lssl -lnsl -lsocket -lc"
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

LDFLAGS="$LDFLAGS -L/usr/local/ssl/lib -R/usr/local/ssl/lib -rpath/usr/local/ssl/lib -M%{SOURCE1} -L.. -lcrypto -lssl -lnsl -lsocket -lc"
export LDFLAGS

./Configure -L/usr/local/ssl/lib -R/usr/local/ssl/lib -M%{SOURCE1} -lcrypto -lc shared solaris-sparcv9-cc

cd apps
cd ..
LIBCRYPTO="-R/usr/local/ssl/lib -L.. -lcrypto -lnsl -lsocket -lc"
LIBSSL="-R/usr/local/ssl/lib -L.. -lssl -lnsl -lsocket -lc"
export LIBCRYPTO LIBSSL
gmake -e
gmake -e test

%install
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -rpath/usr/local/lib -lcrypto -lssl -lnsl -lsocket -Bdirect -zdefs -lc"
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

%pre
if [ -L /usr/local/ssl/certs ] ; then
cat <<EOF
Warning: We noticed that /usr/local/ssl/certs is a symbolic link, if it
is linking to a read only file system this installation will fail, if
you are using RPM version 4.02-6ru the link will be deleted. You will
need to run the installation again and then manually add the link
after completion. If your /usr/local/ssl/certs is not linking to a
read only file system then ignore this message, your installation will
not be affected.
EOF
fi

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
* Fri Jun 06 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.8h-1
- bumped to latest version
* Fri Jan 25 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.8g-11
- changed formatting of message in %pre to a column width of < 80
* Wed Jan 23 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.8g-10
- fixed %pre
* Tue Jan 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.8g-9
- added malloc.mapfile and changed CFLAGS
* Tue Jan 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.8g-8
- removed %config(noreplace) and added warning about links in pre
* Tue Jan 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 0.9.8g-7
- added %config(noreplace) to /usr/local/ssl/certs 
* Fri Oct 19 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 0.9.8g-1
- Bump to g
* Wed May 23 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 0.9.8d-2
- We're not speed demons
* Fri Nov 17 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.8d-1
- Updated to 0.9.8d
* Fri Feb 17 2006 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 0.9.7i-1
- Updated to 0.9.7i, switched to GCC from Sun CC.
