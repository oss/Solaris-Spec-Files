%define version 1.6.2
%define initdir /etc/init.d

Summary: Courier-IMAP server
Name: courier-imap
Version: %{version}
Release: 1ru
Copyright: GPL
Group: Applications/Mail
Source: courier-imap-%{version}.tar.bz2
Packager: Rutgers University
BuildRoot: /var/tmp/courier-imap-install
Requires: fileutils textutils sh-utils sed expect
BuildPreReq: textutils openssl fileutils rpm >= 4.0.2 sed perl gdbm expect openldap
Patch0: patch-courier-pam-rhost

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package
contains the standalone version of the IMAP server that's included in the
Courier mail server package.

%prep
%setup -q

%patch

%build

#CC='/usr/local/gcc-3.0.4/bin/sparcv9-sun-solaris2.8-gcc' \
#CXX='/usr/local/gcc-3.0.4/bin/sparcv9-sun-solaris2.8-g++' \
#CC='gcc' CXX='g++' \
#LDFLAGS='-L/usr/local/lib/64 -R/usr/local/lib/64 #-L/usr/local/gcc-3.0.4/lib -R/usr/local/gcc-3.0.4/lib -L/usr/local/ssl/sparcv9/lib' \
CFLAGS='' CXXFLAGS='' \
CC='cc' CXX='CC' \
LDFLAGS='-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:$PATH \
./configure --localstatedir=/var/run \
--without-authdaemon --with-db=gdbm \
--prefix=/usr/local/lib/courier-imap --enable-workarounds-for-imap-client-bugs
# --with-authdaemonvar=/var/run/authdaemon.courier-imap 

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
