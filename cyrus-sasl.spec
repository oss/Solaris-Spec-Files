Name:		cyrus-sasl
Version:	2.1.23
Release:	1
Group:		Applications/Internet
License:	BSD
URL:		http://cyrusimap.web.cmu.edu/downloads.html#sasl
Source:		ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/cyrus-sasl-%{version}.tar.gz
Source1:	SASL.tar.gz
Patch0:		sasl-rukrb5-support.patch
Patch1:		sasl-rukrb5-source.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	openssl >= 0.9.8 heimdal-devel >= 0.6.2
BuildConflicts:	kerberos-base 

Requires:	openssl >= 0.9.8 heimdal-lib >= 0.6.2

Summary:        SASL implementation

%description
This is the Cyrus SASL API implentation. It can be used on the client
or server side to provide authentication. See RFC 2222 for more
information.

%prep
%setup -c -n cyrus-sasl -T
%setup -q -D -n cyrus-sasl -T -a 0
%setup -q -D -n cyrus-sasl -T -a 1

cd cyrus-sasl-%{version}
%patch0 -p1
%patch1 -p1
%{__sed} -i 's:-lcrypto:-lcrypto -ldes:g' configure
cd ..

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" 
CPPFLAGS="-I/usr/local/include -I/usr/local/include/heimdal -I/usr/local/ssl/include"
export PATH CC CXX CPPFLAGS

%ifarch sparc64
CFLAGS="-xarch=v9"
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9"
export CFLAGS LDFLAGS

cd cyrus-sasl-%{version}

./configure \
	--with-dblib=ndbm 				\
	--enable-gssapi 				\
	--disable-krb4 					\
	--with-pam=/usr/lib 				\
	--with-saslauthd=%{_sbindir}	 		\
	--enable-alwaystrue				\
	--enable-plain 					\
	--enable-login 					\
	--with-plugindir=%{_libdir}/sasl2/sparcv9 	\
	--with-gss_impl=heimdal

gmake saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'

umask 022

mkdir -p sparcv9/sasl
mkdir -p sparcv9/sbin
mv lib/.libs/libsasl2.so* sparcv9/
# NOTE: later on we switch these to sasl/sparcv9!
mv plugins/.libs/*.so* sparcv9/sasl/
mv saslauthd/saslauthd sparcv9/sbin/
mv utils/.libs/* sparcv9/sbin/

## test program
cd saslauthd
gmake testsaslauthd saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'
cd ..
mv saslauthd/testsaslauthd sparcv9/sbin/

gmake clean
rm config.cache

CFLAGS=
export CFLAGS

cd ..
%endif

cd cyrus-sasl-%{version}

LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export LDFLAGS

./configure \
	--with-dblib=ndbm 			\
	--enable-gssapi 			\
	--disable-krb4 				\
	--with-pam=/usr/lib			\
	--with-saslauthd=%{_sbindir} 		\
	--enable-alwaystrue 			\
	--enable-plain				\
	--enable-login 				\
	--with-plugindir=%{_libdir}/sasl2 	\
	--with-gss_impl=heimdal

gmake saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'

cd saslauthd
gmake all saslauthd_LDADD='-lgssapi -lkrb5 -lasn1 -lroken -ldes -lcom_err -lresolv -lsocket -lnsl -lpam'

gmake testsaslauthd 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}/usr/lib %{buildroot}/etc/init.d

cd cyrus-sasl-%{version}
gmake install DESTDIR=%{buildroot}
cd saslauthd
gmake install DESTDIR=%{buildroot}

%{__install} -m 0755 testsaslauthd %{buildroot}%{_sbindir}
ln -sf ../local/lib/sasl2 %{buildroot}/usr/lib/sasl2
cp ../../SASL/usr/local/lib/sasl/smtpd.conf %{buildroot}%{_libdir}/sasl2/
cp ../../SASL/etc/pam.conf.SASL %{buildroot}/etc/
cp ../../SASL/etc/init.d/saslauthd %{buildroot}/etc/init.d/

%ifarch sparc64
umask 022
mkdir -p %{buildroot}%{_libdir}/sparcv9
mkdir -p %{buildroot}%{_libdir}/sasl2/sparcv9
mkdir -p %{buildroot}%{_sbindir}/sparcv9

cd ..

%{__install} -m 0755 sparcv9/sbin/* %{buildroot}%{_sbindir}/sparcv9/
%{__install} -m 0644 sparcv9/libsasl2.so* %{buildroot}%{_libdir}/sparcv9/
# switcheroo!
install -m 0644 sparcv9/sasl/*.so* %{buildroot}%{_libdir}/sasl2/sparcv9/
%endif

find %{buildroot} -name '*.la' -exec rm -f '{}' \;

rm -rf %{buildroot}/usr/lib/

%post

cat<<EOF
You must add the contents of /etc/pam.conf.SASL to /etc/pam.conf, ex:
  cat /etc/pam.conf.SASL >> /etc/pam.conf
You must make a symlink so saslauthd starts up in your favorite run-level, ex:
  ln -s /etc/init.d/saslauthd /etc/rc2.d/S60saslauthd
EOF

%preun
rm -f /usr/lib/sasl2

%postun
cat<<EOF
You should remove the sasl lines from /etc/pam.conf
You should remove the rc symlink that pointed to /etc/init.d/saslauthd
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc cyrus-sasl-%{version}/doc/*txt cyrus-sasl-%{version}/doc/*html
%doc cyrus-sasl-%{version}/INSTALL cyrus-sasl-%{version}/AUTHORS
%doc cyrus-sasl-%{version}/COPYING cyrus-sasl-%{version}/ChangeLog 
%doc cyrus-sasl-%{version}/NEWS cyrus-sasl-%{version}/README
%{_sbindir}/*
%{_libdir}/*.so*
%{_libdir}/sasl2/
%{_libdir}/sparcv9/*
%{_includedir}/*
%{_mandir}/man*/*
/etc/init.d/saslauthd
/etc/pam.conf.SASL

%changelog
* Fri Jun 05 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.1.23-1
- Updated to version 2.1.23 and cleaned up spec file somewhat

* Tue Jul 08 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.1.22-1
- Added changelog and updated to version 2.1.22
- I divided sasl-rukrb5.patch into two patches: 
  sasl-rukrb5-source.patch adds auth_rukrb5.c and auth_rukrb5.h
  sasl-rukrb5-support.patch patches the upstream code to support rukrb5
