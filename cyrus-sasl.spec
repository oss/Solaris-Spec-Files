Summary: SASL implementation 
Name: cyrus-sasl
Version: 1.5.28
Release: 0.6ru
Group: Applications/Internet
License: BSD
Source: %{name}-%{version}.tar.gz
Source1: SASL.tar
BuildRoot: /var/tmp/%{name}-root
BuildRequires: vpkg-SPROcc

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
#grendel's changes:
cd cyrus*
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/include/gssapi" \
CC=/opt/SUNWspro/bin/cc CXX=/opt/SUNWspro/bin/c++ \
./configure --with-dblib=ndbm --disable-gssapi \
--with-pam=/usr/lib --with-saslauthd=/usr/local/sbin \
--enable-plain --enable-login

#LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
#LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
#CPPFLAGS="-I/usr/local/include -I/usr/include/gssapi" \
#./configure --with-dblib=ndbm

gmake

cd saslauthd
make all


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


%post
#ln -s /usr/local/lib/sasl /usr/lib/sasl
cat<<EOF
You must add the contects of /etc/pam.conf.SASL to /etc/pam.conf, ex:
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
%doc doc
%doc INSTALL AUTHORS COPYING NEWS README TODO
/
#/usr/local/include/*
#/usr/local/lib/*.so*
#/usr/local/lib/sasl
#/usr/local/lib/*a
#/usr/local/sbin/*
#/usr/local/man/*/*

