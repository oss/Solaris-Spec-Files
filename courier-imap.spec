%define initdir /etc/init.d

Name:		courier-imap
Version:	4.5.1
Release:	1
Group:		Applications/Mail
License:	GPL
URL:		http://www.courier-mta.org/imap
Source:		http://sourceforge.net/projects/courier/files/courier-imap/courier-imap-%{version}.tar.bz2
Patch:	        courier-imap-setenv.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:       courier-authlib >= 0.61.0

Conflicts:      maildrop < 2.0.4

BuildRequires:	openssl sed gdbm openldap-devel
BuildRequires:	courier-authlib >= 0.61.0

Summary:	The Courier IMAP server

%description
The Courier IMAP server is a fast, scalable, enterprise IMAP server that 
uses Maildirs. This is the same IMAP  server that's included in the Courier 
mail server, but configured as a standalone IMAP server that can be used 
with other mail servers - such as Qmail, Exim, or Postfix - that deliver to 
maildirs.

%prep
%setup -q
%patch -p0

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC"
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include"
LDFLAGS="-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/ssl/lib -R/usr/local/lib"
COURIERAUTHCONFIG="/usr/local/bin/courierauthconfig"
export PATH CC CXX CPPFLAGS LDFLAGS COURIERAUTHCONFIG

./configure \
	--localstatedir=/var/run 					\
	--without-authdaemon --with-db=gdbm --without-ipv6 		\
	--prefix=/usr/local 						\
	--bindir=/usr/local/courier-imap/bin 				\
	--sbindir=/usr/local/courier-imap/sbin 				\
	--enable-workarounds-for-imap-client-bugs 			\
	--with-waitfunc=wait3  # Workaround for broken wait in Solaris

gmake -j3
# This (correctly) fails with the imap-client-bugs option
#gmake check  

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/pam.d

gmake install DESTDIR=%{buildroot}
gmake install-configure DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{initdir}
%{__sed} \
's:touch /var/lock/subsys/courier-imap:[ -d "/var/run/authdaemon.courier-imap" ] || /usr/bin/mkdir -p /var/run/authdaemon.courier-imap:g' \
courier-imap.sysvinit > %{buildroot}%{initdir}/courier-imap

cp imap/BUGS BUGS.imap
cp imap/BUGS.html BUGS.imap.html
cp imap/ChangeLog ChangeLog
cp imap/README README.imap
cp imap/README.html README.imap.html
cp imap/README.proxy README.imap.proxy
cp imap/README.proxy.html README.imap.proxy.html
cp maildir/AUTHORS AUTHORS.maildir
cp maildir/README.imapkeywords.html README.imapkeywords.html
cp maildir/README.maildirfilter.html README.maildirfilter.html
cp maildir/README.maildirquota.html README.maildirquota.html
cp maildir/README.maildirquota.txt README.maildirquota.txt
cp maildir/README.sharedfolders.html README.sharedfolders.html
cp maildir/README.sharedfolders.txt README.sharedfolders.txt
cp tcpd/README.couriertls README.couriertls
cp unicode/README README.unicode

%clean
rm -rf %{buildroot}

%post
cat << EOF

  >>> READ ME! <<<
  If you are using Maildir format you might need to add this line
  to your old /usr/local/etc/[imapd|popsd] configs:
  MAILDIRPATH=Maildir

EOF

%files
%defattr(-, root, root)

%doc 00README.NOW.OR.SUFFER AUTHORS COPYING 
%doc COPYING.GPL ChangeLog NEWS NEWS.html 
%doc README BUGS.imap BUGS.imap.html README.imap 
%doc README.imap.html README.imap.proxy 
%doc README.imap.proxy.html AUTHORS.maildir 
%doc README.imapkeywords.html 
%doc README.maildirfilter.html 
%doc README.maildirquota.html 
%doc README.maildirquota.txt 
%doc README.sharedfolders.html 
%doc README.sharedfolders.txt 
%doc README.couriertls README.unicode

%config(noreplace) %{_sysconfdir}/imapd-ssl
%config(noreplace) %{_sysconfdir}/imapd
%config(noreplace) %{_sysconfdir}/pop3d
%config(noreplace) %{_sysconfdir}/pop3d-ssl
%config(noreplace) %{_sysconfdir}/pop3d.cnf
%config(noreplace) %{_sysconfdir}/imapd.cnf
%config(noreplace) /etc/pam.d/imap
%config(noreplace) /etc/pam.d/pop3
%{_sysconfdir}/imapd.dist
%{_sysconfdir}/imapd-ssl.dist
%{_sysconfdir}/pop3d.dist
%{_sysconfdir}/pop3d-ssl.dist
%{_sysconfdir}/quotawarnmsg.example
%attr(0755, root, root) %{initdir}/courier-imap

%{_prefix}/courier-imap/
%{_libexecdir}/*
%{_datadir}/*

%changelog
* Fri Aug 07 2009 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.5.1-1
- Updated to version 4.5.1
- Cleaned things up somewhat
* Wed Oct 29 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.4.1-3
- built against openldap-2.4.12-0 
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
