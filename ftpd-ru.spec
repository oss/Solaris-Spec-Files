Name: wu-ftpd-ru
Version: 2.6.1
Copyright: BSD, Rutgers
Group: Applications/Internet
Summary: WU-FTPD, localized for Rutgers
Release: 2
Source: wu-ftpd-2.6.1.tar.gz
Patch: ftp-new-ru.diff
BuildRoot: /var/tmp/%{name}-root

%description
Wu-ftpd is an ftp server; this rpm is patched specifically for Rutgers
systems.

To configure this package, you need to at least:
  - create /etc/ftpaccess (based on /etc/ftpaccess.rpm)
    ftpaccess is not needed if you're not using the "-a" option.
  - add ftpd to /etc/inet/inetd.conf, probably with the "-a" option
  - HUP inetd

%prep
%setup -q -n wu-ftpd-2.6.1
%patch -p1

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local

# This is, more or less, the output of make install.

rm -f bin/ftpd bin/ftpshut bin/ftpcount bin/ftpwho bin/ckconfig bin/ftprestart
ln src/ftpd bin
ln src/ftpshut bin
ln src/ftpcount bin
ln src/ftpcount bin/ftpwho
ln src/ckconfig bin
ln src/ftprestart bin
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man5
mkdir -p $RPM_BUILD_ROOT/etc
install -c -m 755 bin/ftpd \
    $RPM_BUILD_ROOT/usr/local/sbin/ftpd
install -c -m 755 bin/ftpshut \
    $RPM_BUILD_ROOT/usr/local/sbin/ftpshut
install -c -m 755 bin/ftpcount \
    $RPM_BUILD_ROOT/usr/local/sbin/ftpcount
install -c -m 755 bin/ftpwho \
    $RPM_BUILD_ROOT/usr/local/sbin/ftpwho
install -c -m 755 bin/ckconfig \
    $RPM_BUILD_ROOT/usr/local/sbin/ckconfig
install -c -m 755 bin/ftprestart \
    $RPM_BUILD_ROOT/usr/local/sbin/ftprestart
install -c -m 755 util/privatepw/privatepw \
    $RPM_BUILD_ROOT/usr/local/sbin/privatepw
install -c -m 644 doc/ftpd.8 \
    $RPM_BUILD_ROOT/usr/local/man/man8/ftpd.8
install -c -m 644 doc/ftpcount.1 \
    $RPM_BUILD_ROOT/usr/local/man/man1/ftpcount.1
install -c -m 644 doc/ftpwho.1 \
    $RPM_BUILD_ROOT/usr/local/man/man1/ftpwho.1
install -c -m 644 doc/ftpshut.8 \
    $RPM_BUILD_ROOT/usr/local/man/man8/ftpshut.8
install -c -m 644 doc/ftpaccess.5 \
    $RPM_BUILD_ROOT/usr/local/man/man5/ftpaccess.5
install -c -m 644 doc/ftphosts.5 \
    $RPM_BUILD_ROOT/usr/local/man/man5/ftphosts.5
install -c -m 644 doc/ftpconversions.5 \
    $RPM_BUILD_ROOT/usr/local/man/man5/ftpconversions.5
install -c -m 644 doc/ftpservers.5 \
    $RPM_BUILD_ROOT/usr/local/man/man5/ftpservers.5
install -c -m 644 doc/xferlog.5 \
    $RPM_BUILD_ROOT/usr/local/man/man5/xferlog.5
install -c -m 644 doc/ftprestart.8 \
    $RPM_BUILD_ROOT/usr/local/man/man8/ftprestart.8
install -c -m 644 util/privatepw/privatepw.8 \
    $RPM_BUILD_ROOT/usr/local/man/man8/privatepw.8
install -c -m 644 doc/examples/ftpaccess \
    $RPM_BUILD_ROOT/etc/ftpaccess.rpm
install -c -m 644 doc/examples/ftpconversions \
    $RPM_BUILD_ROOT/etc/ftpconversions.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc doc/*
/usr/local/sbin/ftpd
/usr/local/sbin/ftpshut
/usr/local/sbin/ckconfig
/usr/local/sbin/ftprestart
/usr/local/sbin/privatepw
/usr/local/sbin/ftpcount
/usr/local/sbin/ftpwho
/usr/local/man/man8/ftpd.8
/usr/local/man/man8/ftpshut.8
/usr/local/man/man8/ftprestart.8
/usr/local/man/man8/privatepw.8
/usr/local/man/man1/ftpcount.1
/usr/local/man/man1/ftpwho.1
/usr/local/man/man5/ftpaccess.5
/usr/local/man/man5/ftphosts.5
/usr/local/man/man5/ftpconversions.5
/usr/local/man/man5/ftpservers.5
/usr/local/man/man5/xferlog.5
/etc/ftpaccess.rpm
/etc/ftpconversions.rpm
