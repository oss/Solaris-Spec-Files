Summary: Inetd replacement
Name: xinetd
Version: 2.3.3
Release: 1
Group: Applications/Internet
Copyright: BSD-like
Source: xinetd-2.3.3.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tcp_wrappers

%description
Xinetd is a replacement for inetd.  It has access control, extensive
logging capabilities, a different config grammar, and other features.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  DFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" ./configure --with-libwrap=/usr/local/lib
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
mkdir $RPM_BUILD_ROOT/usr/local/man/man5
mkdir $RPM_BUILD_ROOT/usr/local/sbin
mkdir $RPM_BUILD_ROOT/etc
install -c -m 0755 xinetd/xinetd $RPM_BUILD_ROOT/usr/local/sbin/xinetd
install -c -m 0755 xinetd/itox   $RPM_BUILD_ROOT/usr/local/sbin/itox
install -c -m 0644 xinetd/xinetd.conf.man \
   $RPM_BUILD_ROOT/usr/local/man/man5/xinetd.conf.5
install -c -m 0644 xinetd/xinetd.log.man \
   $RPM_BUILD_ROOT/usr/local/man/man8/xinetd.log.8
install -c -m 0644 xinetd/xinetd.man \
    $RPM_BUILD_ROOT/usr/local/man/man8/xinetd.8
install -c -m 0644 xinetd/itox.8 $RPM_BUILD_ROOT/usr/local/man/man8/itox.8
install -c -m 0644 xinetd/xconv.pl $RPM_BUILD_ROOT/usr/local/sbin/xconv.pl
install -c -m 0644 xinetd/sample.conf $RPM_BUILD_ROOT/etc/sample.conf.rpm

%post
cat <<EOF
You must put your xinetd.conf in /etc/xinetd.conf; there is a sample
config file in /etc/sample.conf.rpm.  You can use xconv.pl to convert
your old inetd.conf to to the xinetd format.
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/man/man8/*
/usr/local/man/man5/*
/usr/local/sbin/*
/etc/sample.conf.rpm
