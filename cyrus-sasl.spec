Summary: SASL implementation 
Name: cyrus-sasl
Version: 1.5.28
Release: 5ru
Group: Applications/Internet
License: BSD
Source: %{name}-%{version}.tar.gz
Source1: SASL.tar
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc openssl
BuildConflicts: heimdal heimdal-devel kerberos-base
Requires: openssl make

%description
This is the Cyrus SASL API implentation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

  (from README)

%prep
%setup -c -n cyrus-sasl -T
%setup -q -D -n cyrus-sasl -T -a 0
%setup -q -D -n cyrus-sasl -T -a 1

%build
%ifarch == sparc64
cd cyrus*
LD="/usr/ccs/bin/ld -L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" \
CPPFLAGS="-I/usr/local/include -I/usr/include/gssapi -I/usr/local/ssl/include" \
CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/c++ \
CFLAGS="-xarch=v9" \
./configure --with-dblib=ndbm --disable-gssapi --disable-krb4 \
--with-pam=/usr/lib --with-saslauthd=/usr/local/sbin \
--enable-plain --enable-login --with-plugindir=/usr/local/lib/sasl/sparcv9
gmake -j 9
umask 022
mkdir -p sparcv9/sasl
mkdir -p sparcv9/sbin
mv lib/.libs/libsasl.so* sparcv9
# NOTE: later on we switch these to sasl/sparcv9!
mv plugins/.libs/*.so* sparcv9/sasl
mv saslauthd/saslauthd sparcv9/sbin
mv utils/sasldblistusers sparcv9/sbin
#mv utils/saslpasswd sparcv9/sbin # shell script
gmake clean
rm config.cache
cd ../
%endif

cd cyrus*
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/include/gssapi -I/usr/local/ssl/include" \
CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/c++ \
./configure --with-dblib=ndbm --disable-gssapi --disable-krb4 \
--with-pam=/usr/lib --with-saslauthd=/usr/local/sbin \
--enable-plain --enable-login --with-plugindir=/usr/local/lib/sasl

gmake -j 9

cd saslauthd
gmake all -j 9


%install
cd cyrus*
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}/usr/lib %{buildroot}/etc/init.d/
gmake install DESTDIR=%{buildroot}
cd saslauthd
gmake install DESTDIR=%{buildroot}
#gmake install-sbinPROGRAMS DESTDIR=%{buildroot}
#gmake install-man DESTDIR=%{buildroot}
ln -sf ../local/lib/sasl %{buildroot}/usr/lib/sasl
#ln -sf ../../usr/local/sbin/saslauthd %{buildroot}/etc/init.d/saslauthd
cp ../../SASL/usr/local/lib/sasl/smtpd.conf %{buildroot}/usr/local/lib/sasl/
cp ../../SASL/etc/pam.conf.SASL %{buildroot}/etc/
cp ../../SASL/etc/init.d/saslauthd %{buildroot}/etc/init.d/

%ifarch sparc64
umask 022
mkdir -p %{buildroot}/usr/local/lib/sparcv9
mkdir -p %{buildroot}/usr/local/sbin/sparcv9
mkdir -p %{buildroot}/usr/local/lib/sasl/sparcv9
cd ../

install -m 0755 sparcv9/sbin/* %{buildroot}/usr/local/sbin/sparcv9
install -m 0644 sparcv9/libsasl.so* %{buildroot}/usr/local/lib/sparcv9
# switcheroo!
install -m 0644 sparcv9/sasl/*.so* %{buildroot}/usr/local/lib/sasl/sparcv9
%endif

find %{buildroot} -name *.la
find %{buildroot} -name *.la | xargs rm #exec better in case none are found?

%post

#ln -s /usr/local/lib/sasl /usr/lib/sasl
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
rm -f /usr/lib/sasl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc cyrus-sasl-%{version}/doc/*txt cyrus-sasl-%{version}/doc/*html
%doc cyrus-sasl-%{version}/INSTALL cyrus-sasl-%{version}/AUTHORS
%doc cyrus-sasl-%{version}/COPYING cyrus-sasl-%{version}/TODO 
%doc cyrus-sasl-%{version}/NEWS cyrus-sasl-%{version}/README 
/etc/init.d/saslauthd
/etc/pam.conf.SASL
/usr/local/include/*
/usr/local/lib/*
/usr/local/man/man3/*
/usr/local/man/man8/*
/usr/local/sbin/*
