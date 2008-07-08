Summary:	SASL implementation 
Name:		cyrus-sasl
Version:	2.1.22
Release:	1
Group:		Applications/Internet
License:	BSD
Source:		%{name}-%{version}.tar.gz
Source1:	SASL.tar.gz
Patch0:		sasl-rukrb5-support.patch
Patch1:		sasl-rukrb5-source.patch
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	openssl >= 0.9.8 heimdal-devel >= 0.6.2
BuildConflicts:	kerberos-base 
Requires:	openssl >= 0.9.8

%description
This is the Cyrus SASL API implentation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

  (from README)

%prep
%setup -c -n cyrus-sasl -T
%setup -q -D -n cyrus-sasl -T -a 0
%setup -q -D -n cyrus-sasl -T -a 1
cd cyrus-sasl-%{version}
%patch0 -p1
%patch1 -p1
cd ..

%build
%ifarch sparc64
cd cyrus*
sed s/lcrypto/"lcrypto -ldes"/g configure > configure.ru
mv configure.ru configure
chmod 755 configure
LD="/usr/ccs/bin/ld -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
CPPFLAGS="-I/usr/local/include -I/usr/local/include/heimdal -I/usr/local/ssl/include" \
CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/c++ \
CFLAGS="-xarch=v9" \
./configure --with-dblib=ndbm --enable-gssapi --disable-krb4 \
--with-pam=/usr/lib --with-saslauthd=/usr/local/sbin --enable-alwaystrue \
--enable-plain --enable-login --with-plugindir=/usr/local/lib/sasl2/sparcv9 \
--with-gss_impl=heimdal
gmake saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'
umask 022
mkdir -p sparcv9/sasl
mkdir -p sparcv9/sbin
mv lib/.libs/libsasl2.so* sparcv9
# NOTE: later on we switch these to sasl/sparcv9!
mv plugins/.libs/*.so* sparcv9/sasl
mv saslauthd/saslauthd sparcv9/sbin
mv utils/.libs/* sparcv9/sbin

## test program
cd saslauthd
gmake testsaslauthd saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'
cd ..
mv saslauthd/testsaslauthd sparcv9/sbin

gmake clean
rm config.cache
cd ../
%endif

cd cyrus*
sed s/lcrypto/"lcrypto -ldes"/g configure > configure.ru
mv configure.ru configure
chmod 755 configure
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/include/heimdal -I/usr/local/ssl/include" \
CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/c++ \
./configure --with-dblib=ndbm --enable-gssapi --disable-krb4 \
--with-pam=/usr/lib --with-saslauthd=/usr/local/sbin --enable-alwaystrue \
--enable-plain --enable-login --with-plugindir=/usr/local/lib/sasl2 \
--with-gss_impl=heimdal
gmake saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'

cd saslauthd
gmake all saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'

gmake testsaslauthd 

%install
cd cyrus*
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}/usr/lib %{buildroot}/etc/init.d/
gmake install DESTDIR=%{buildroot}
cd saslauthd
gmake install DESTDIR=%{buildroot}
install -m 0755 testsaslauthd %{buildroot}/usr/local/sbin
ln -sf ../local/lib/sasl2 %{buildroot}/usr/lib/sasl2
cp ../../SASL/usr/local/lib/sasl/smtpd.conf %{buildroot}/usr/local/lib/sasl2/
cp ../../SASL/etc/pam.conf.SASL %{buildroot}/etc/
cp ../../SASL/etc/init.d/saslauthd %{buildroot}/etc/init.d/

%ifarch sparc64
umask 022
mkdir -p %{buildroot}/usr/local/lib/sparcv9
mkdir -p %{buildroot}/usr/local/sbin/sparcv9
mkdir -p %{buildroot}/usr/local/lib/sasl2/sparcv9
cd ../

install -m 0755 sparcv9/sbin/* %{buildroot}/usr/local/sbin/sparcv9
install -m 0644 sparcv9/libsasl2.so* %{buildroot}/usr/local/lib/sparcv9
# switcheroo!
install -m 0644 sparcv9/sasl/*.so* %{buildroot}/usr/local/lib/sasl2/sparcv9
%endif

find %{buildroot} -name *.la
find %{buildroot} -name *.la | xargs rm #exec better in case none are found?

rm -rf %{buildroot}/usr/lib

%post

cat<<EOF
You must add the contents of /etc/pam.conf.SASL to /etc/pam.conf, ex:
  cat /etc/pam.conf.SASL >> /etc/pam.conf
You must make a symlink so saslauthd starts up in your favorite run-level, ex:
  ln -s /etc/init.d/saslauthd /etc/rc2.d/S60saslauthd
EOF

%postun
cat <<EOF
You should remove the sasl lines from /etc/pam.conf
You should remove the rc symlink that pointed to /etc/init.d/saslauthd
EOF

%preun
rm -f /usr/lib/sasl2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc cyrus-sasl-%{version}/doc/*txt cyrus-sasl-%{version}/doc/*html
%doc cyrus-sasl-%{version}/INSTALL cyrus-sasl-%{version}/AUTHORS
%doc cyrus-sasl-%{version}/COPYING cyrus-sasl-%{version}/ChangeLog 
%doc cyrus-sasl-%{version}/NEWS cyrus-sasl-%{version}/README
%doc /usr/local/man
/etc/init.d/saslauthd
/etc/pam.conf.SASL
/usr/local/include/*
/usr/local/lib/*
/usr/local/sbin/*

%changelog
* Tue Jul 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.1.22-1
- Added changelog and updated to version 2.1.22
- I divided sasl-rukrb5.patch into two patches: 
  sasl-rukrb5-source.patch adds auth_rukrb5.c and auth_rukrb5.h
  sasl-rukrb5-support.patch patches the upstream code to support rukrb5
