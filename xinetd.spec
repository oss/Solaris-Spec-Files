Summary: Inetd replacement
Name: xinetd
Version: 2.3.9
Release: 0ru
Group: Applications/Internet
Copyright: BSD-like
Source: xinetd-2.3.9.tar.gz
Source1: xinetd-init.d
# patches from rawhide--thanks redhat! :-)
# hopefully by now these are all upstreamed. -- richton 15-Oct-2002
#Patch0: xinetd-2002.03.26-stream_wait.patch
#Patch1: xinetd-2002.03.28-sigchld.patch
#Patch2: xinetd-2.3.5-mask.patch
#Patch3: xinetd-06-patch4.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: tcp_wrappers >= 7.6
ExcludeOS: solaris2.7
#buggy build on Solaris 7

%description
Xinetd is a replacement for inetd.  It has access control, extensive
logging capabilities, a different config grammar, and other features.

%prep
%setup -q
#%patch0 -p1
#patch1 -p1
#%patch2 -p1
#%patch3 -p1

%build

LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  DFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  CFLAGS="-I/usr/local/include" LD_RUN_PATH="/usr/local/lib" \
  CC="gcc" ./configure --with-libwrap=/usr/local/lib

make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr/local/
#mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8
#mkdir $RPM_BUILD_ROOT/usr/local/man/man5
#mkdir $RPM_BUILD_ROOT/usr/local/sbin
#mkdir $RPM_BUILD_ROOT/etc
#install -c -m 0755 xinetd/xinetd $RPM_BUILD_ROOT/usr/local/sbin/xinetd
#install -c -m 0755 xinetd/itox   $RPM_BUILD_ROOT/usr/local/sbin/itox
#install -c -m 0644 xinetd/xinetd.conf.man \
#   $RPM_BUILD_ROOT/usr/local/man/man5/xinetd.conf.5
#install -c -m 0644 xinetd/xinetd.log.man \
#   $RPM_BUILD_ROOT/usr/local/man/man8/xinetd.log.8
#install -c -m 0644 xinetd/xinetd.man \
#    $RPM_BUILD_ROOT/usr/local/man/man8/xinetd.8
#install -c -m 0644 xinetd/itox.8 $RPM_BUILD_ROOT/usr/local/man/man8/itox.8
#install -c -m 0644 xinetd/xconv.pl $RPM_BUILD_ROOT/usr/local/sbin/xconv.pl
mkdir -p $RPM_BUILD_ROOT/usr/local/etc/ $RPM_BUILD_ROOT/etc/init.d/
install -c -m 0644 xinetd/sample.conf $RPM_BUILD_ROOT/usr/local/etc/xinetd.conf
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/xinetd
chmod 750 $RPM_BUILD_ROOT/etc/init.d/xinetd

%post
cat <<EOF
If this is a new install, a sample /usr/local/etc/xinetd.conf was put
down. You can use xconv.pl to convert your old inetd.conf to to the
xinetd format.
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
