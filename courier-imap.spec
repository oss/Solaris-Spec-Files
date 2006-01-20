%define version 4.0.6
%define initdir /etc/init.d

Summary: Courier-IMAP server
Name: courier-imap
Version: %{version}
Release: 1
Copyright: GPL
Group: Applications/Mail
Source: %{name}-%{version}.tar.bz2
Packager: Rutgers University
BuildRoot: /var/tmp/%{name}-root
BuildRequires: openssl coreutils rpm >= 4.0.2 sed perl gdbm openldap-devel courier-authlib
Requires: openldap-lib courier-authlib

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package
contains the standalone version of the IMAP server that's included in the
Courier mail server package.

%prep
%setup -q

%build

CC="gcc" CXX="g++" \
CFLAGS="" CXXFLAGS="" \
LDFLAGS="-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/ssl/lib \
-R/usr/local/lib -L/usr/local/lib/courier-authlib/lib/courier-authlib/ \
-R/usr/local/lib/courier-authlib/lib/courier-authlib/" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include \
-I/usr/local/lib/courier-authlib/include" \
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:$PATH" \
COURIERAUTHCONFIG="/usr/local/lib/courier-authlib/bin/courierauthconfig" \
./configure --localstatedir=/var/run \
--without-authdaemon --with-db=gdbm --without-ipv6 \
--prefix=/usr/local/lib/courier-imap \
--enable-workarounds-for-imap-client-bugs \
--with-waitfunc=wait3  # Work around for broken wait in Solaris

gmake
# This (correctly) fails with the imap-client-bugs option
#gmake check  

%install

%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/etc/pam.d
gmake install DESTDIR=$RPM_BUILD_ROOT
gmake install-configure DESTDIR=$RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{initdir}
sed s/'touch \/var\/lock\/subsys\/courier-imap'/'\[ -d \"\/var\/run\/authdaemon.courier-imap\" \] \|\| \/usr\/bin\/mkdir -p \/var\/run\/authdaemon.courier-imap'/g courier-imap.sysvinit > courier-imap.sysvinit.ru
%{__cp} courier-imap.sysvinit.ru $RPM_BUILD_ROOT%{initdir}/courier-imap

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

  >>> READ ME! <<<
  If your using Maildir format you might need to added this line
  to your old /usr/local/lib/courier-imap/etc/[imapd|popsd] configs:
  MAILDIRPATH=Maildir

EOF

%files
%defattr(-,root,root)
%config(noreplace) /usr/local/lib/courier-imap/etc/imapd-ssl
%config(noreplace) /usr/local/lib/courier-imap/etc/imapd
%config(noreplace) /usr/local/lib/courier-imap/etc/pop3d
%config(noreplace) /usr/local/lib/courier-imap/etc/pop3d-ssl
%config(noreplace) /usr/local/lib/courier-imap/etc/pop3d.cnf
%config(noreplace) /usr/local/lib/courier-imap/etc/imapd.cnf
/usr/local/lib/courier-imap/etc/quotawarnmsg.example
/usr/local/lib/courier-imap/bin
/usr/local/lib/courier-imap/libexec
/usr/local/lib/courier-imap/man
/usr/local/lib/courier-imap/sbin
/usr/local/lib/courier-imap/share
%defattr(0755,root,root)
/etc/init.d/courier-imap

