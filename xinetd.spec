Summary: inetd replacement
Name: xinetd
Version: 2.3.13
Release: 0
Group: Applications/Internet
Copyright: BSD-like
Source: xinetd-%{version}.tar.gz
Source1: xinetd-init.d
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tcp_wrappers >= 7.6 vpkg-SPROcc
ExcludeOS: solaris2.7
#buggy build on Solaris 7

%description
xinetd is a replacement for inetd.  It has access control, extensive
logging capabilities, a different config grammar, and other features.

%prep
%setup -q

%build

LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" \
  CC="/opt/SUNWspro/bin/cc" ./configure --with-libwrap=/usr/local/lib

### There is a "libportable" library that ships with xinetd. It consists
### (at least on Solaris 8/9) entirely of ifdef'd out code. In other words,
### cc -c /dev/null -o stupid.o. It does this (essentially) for five files
### and makes libportable.a (with nothing in it except the five filenames!)
### Apparently all NULLs is a choke situation for the linker. Not sure if this
### is a linker bug or not. I am, however, sure that it's pretty dumb.
### This makes the bug invisible, even if it's not a fix.
cd xinetd
sed s/"-lportable"/""/g Makefile > Makefile.new
cp Makefile.new Makefile
cd ..

make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/local/
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/ $RPM_BUILD_ROOT/etc/init.d/
install -c -m 0644 xinetd/sample.conf $RPM_BUILD_ROOT/usr/local/etc/xinetd.conf
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/xinetd
chmod 750 $RPM_BUILD_ROOT/etc/init.d/xinetd

%post
cat <<EOF
If this is a new install, a sample /usr/local/etc/xinetd.conf was put
down. You can use xconv.pl to convert your old inetd.conf to to the
xinetd format.

*** NOTE: xinetd historically has had many parser issues. This release
is no exception; there are many changes. Experience has shown fixes often
tighten config syntax subtly. Be careful when using old config files. ***
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/man/man8/*
/usr/local/man/man5/*
/usr/local/sbin/*
%config(noreplace) /usr/local/etc/xinetd.conf
%config(noreplace) /etc/init.d/xinetd
