%define version 2.2.1
%define initdir /etc/init.d

Summary: Courier-IMAP server
Name: courier-imap
Version: %{version}
Release: 0
Copyright: GPL
Group: Applications/Mail
Source: courier-imap-%{version}.tar.bz2
Packager: Rutgers University
BuildRoot: /var/tmp/courier-imap-install
BuildPreReq: textutils openssl fileutils rpm >= 4.0.2 sed perl gdbm 
Patch0: patch-courier-pam-rhost
Patch1: courier-imap-cplusplus.patch

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package
contains the standalone version of the IMAP server that's included in the
Courier mail server package.

%prep
%setup -q

%patch
%patch1 -p1

%build

CC='cc' CXX='CC' \
CFLAGS='' CXXFLAGS='' \
LDFLAGS='-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH \
./configure --localstatedir=/var/run \
--without-authdaemon --with-db=gdbm --without-ipv6 \
--prefix=/usr/local/lib/courier-imap --enable-workarounds-for-imap-client-bugs
# --with-authdaemonvar=/var/run/authdaemon.courier-imap 
# above commented for no authdaemon

make 

%install

%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/etc/pam.d
make install DESTDIR=$RPM_BUILD_ROOT
make install-configure DESTDIR=$RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{initdir}
sed s/'touch \/var\/lock\/subsys\/courier-imap'/'\[ -d \"\/var\/run\/authdaemon.courier-imap\" \] \|\| \/usr\/bin\/mkdir -p \/var\/run\/authdaemon.courier-imap'/g courier-imap.sysvinit > courier-imap.sysvinit.ru
%{__cp} courier-imap.sysvinit.ru $RPM_BUILD_ROOT%{initdir}/courier-imap

%files
%defattr(-,root,root)
%config /usr/local/lib/courier-imap/etc/imapd-ssl
%config /usr/local/lib/courier-imap/etc/imapd
%config /usr/local/lib/courier-imap/etc/pop3d
%config /usr/local/lib/courier-imap/etc/pop3d-ssl
%config /usr/local/lib/courier-imap/etc/pop3d.cnf
%config /usr/local/lib/courier-imap/etc/imapd.cnf
/usr/local/lib/courier-imap/etc/quotawarnmsg.example
/usr/local/lib/courier-imap/bin
/usr/local/lib/courier-imap/libexec
/usr/local/lib/courier-imap/man
/usr/local/lib/courier-imap/sbin
/usr/local/lib/courier-imap/share
%defattr(0755,root,root)
/etc/init.d/courier-imap

%clean
rm -rf $RPM_BUILD_ROOT
