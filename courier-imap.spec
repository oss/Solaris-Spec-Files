%define version 4.4.1
%define initdir /etc/init.d

Summary:	Courier-IMAP server
Name:		courier-imap
Version:	%{version}
Release:	2
Copyright:	GPL
Group:		Applications/Mail
Source:		%{name}-%{version}.tar.bz2
Patch:	        courier-imap-setenv.patch
Packager:	Rutgers University
BuildRoot:	/var/tmp/%{name}-root
BuildRequires:	openssl coreutils rpm >= 4.0.2 sed perl gdbm openldap-devel
BuildRequires:	courier-authlib >= 0.61.0
Requires:	openldap-lib courier-authlib >= 0.61.0
Conflicts:	maildrop < 2.0.4

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package
contains the standalone version of the IMAP server that's included in the
Courier mail server package.

%prep
%setup -q
%patch -p0

%build

PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include"
LDFLAGS="-L/usr/local/ssl/lib -L/usr/local/lib \
-R/usr/local/ssl/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LDFLAGS CFLAGS CXXFLAGS

COURIERAUTHCONFIG="/usr/local/bin/courierauthconfig" \
./configure --localstatedir=/var/run \
--without-authdaemon --with-db=gdbm --without-ipv6 \
--prefix=/usr/local \
--bindir=/usr/local/courier-imap/bin \
--sbindir=/usr/local/courier-imap/sbin \
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

cp imap/BUGS BUGS.imap
cp imap/BUGS.html BUGS.imap.html
cp imap/ChangeLog ChangeLog
cp imap/README README.imap
cp imap/README.html README.imap.html
cp imap/README.proxy README.imap.proxy
cp imap/README.proxy.html README.imap.proxy.html
cp maildir/AUTHORS AUTHORS.maildir
cp maildir/INSTALL INSTALL.maildir
cp maildir/README.imapkeywords.html README.imapkeywords.html
cp maildir/README.maildirfilter.html README.maildirfilter.html
cp maildir/README.maildirquota.html README.maildirquota.html
cp maildir/README.maildirquota.txt README.maildirquota.txt
cp maildir/README.sharedfolders.html README.sharedfolders.html
cp maildir/README.sharedfolders.txt README.sharedfolders.txt
cp tcpd/README.couriertls README.couriertls
cp unicode/README README.unicode


%clean
rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

  >>> READ ME! <<<
  If your using Maildir format you might need to added this line
  to your old /usr/local/etc/[imapd|popsd] configs:
  MAILDIRPATH=Maildir

EOF

%files
%defattr(-,root,root)
%doc 00README.NOW.OR.SUFFER AUTHORS COPYING COPYING.GPL ChangeLog INSTALL INSTALL.html.in NEWS NEWS.html README README.cygwin BUGS.imap BUGS.imap.html README.imap README.imap.html README.imap.proxy README.imap.proxy.html AUTHORS.maildir INSTALL.maildir README.imapkeywords.html README.maildirfilter.html README.maildirquota.html README.maildirquota.txt README.sharedfolders.html README.sharedfolders.txt README.couriertls README.unicode  
%config(noreplace) /usr/local/etc/imapd-ssl
%config(noreplace) /usr/local/etc/imapd
%config(noreplace) /usr/local/etc/pop3d
%config(noreplace) /usr/local/etc/pop3d-ssl
%config(noreplace) /usr/local/etc/pop3d.cnf
%config(noreplace) /usr/local/etc/imapd.cnf
%config(noreplace) /etc/pam.d/imap
%config(noreplace) /etc/pam.d/pop3
/usr/local/etc/imapd.dist
/usr/local/etc/imapd-ssl.dist
/usr/local/etc/pop3d.dist
/usr/local/etc/pop3d-ssl.dist
/usr/local/etc/quotawarnmsg.example
/usr/local/courier-imap/bin/*
/usr/local/libexec/*
/usr/local/courier-imap/sbin/*
/usr/local/share/*
%defattr(0755,root,root)
/etc/init.d/courier-imap

%changelog
* Wed Jul 23 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> -4.4.1-2
- fixed patch
* Mon Jul 21 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.4.1-1
- bumped to 4.4.1
- patched to use putenv instead of setenv for solaris 9
- switched to sun studio from gcc
* Tue Jul 1 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.3.1-3
- added doc section
* Tue Jun 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.3.1-1
- bump to 4.3.1
* Mon Dec 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.3.0-1
- Bump to 4.3.0
* Wed Nov 07 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.2.1-1
- Bump to 4.2.1
* Tue Aug 28 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 4.1.3-5
- Added maildrop conflicts
* Thu Aug 09 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 4.1.3-2
- Correct paths.
* Thu Aug 09 2007 Eric Rivas <kc2hmv@nbcs.rutgers.edu> - 4.1.3-1
- Update to 4.1.3
