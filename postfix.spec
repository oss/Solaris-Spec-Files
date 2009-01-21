%define	ver 	2.5.5

Summary: 	Secure sendmail replacement
Name: 		postfix-tls
Version: 	%{ver}
Release: 	4	
Group: 		Applications/Internet
License: 	IBM Public License
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source: 	postfix-%{ver}.tar.gz
Source1: 	PFIX-TLS.tar
BuildRoot: 	/var/tmp/%{name}-root
Obsoletes: 	postfix <= 20010228_pl04-4ru postfix <= 2.4.1 postfix-mysql postfix-tls <= 2.4.1 
Conflicts: 	postfix <= 20010228_pl04-4ru postfix <= 2.4.1
Requires: 	openssl >= 0.9.8 cyrus-sasl >= 2.1.18-2 pcre >= 7.7-1 openldap-lib >= 2.3.43
BuildRequires: 	cyrus-sasl openssl >= 0.9.8
BuildRequires:	pcre-devel >= 7.7-1
BuildRequires: openldap-devel >= 2.4.12
BuildConflicts:	gdbm 

%description
Postfix aims to be an alternative to the widely-used sendmail
program.

Although IBM supported the Postfix development, it abstains from
control over its evolution. The goal is to have Postfix installed
on as many systems as possible. To this end, the software is given
away with no strings attached to it, so that it can evolve with
input from and under control by its users.

In other words, IBM releases Postfix only once. I will be around
to guide its development for a limited time.

  (from 0README)

%prep
%setup -c -n postfix-tls -T

%setup -q -D -n postfix-tls -T -a 0
%setup -q -D -n postfix-tls -T -a 1

%build

cd postfix-%{ver}

gmake tidy

gmake makefiles CC=/opt/SUNWspro/bin/cc CCARGS="-DUSE_TLS -DHAS_SSL -DUSE_SASL_AUTH -DHAS_PCRE -DHAS_LDAP -I/usr/local/include -I/usr/local/include/sasl -I/usr/local/ssl/include" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl2 -L/usr/local/lib -lcrypto -lssl -lpcre -L/usr/local/lib -R/usr/local/lib -lldap -L/usr/local/lib -R/usr/local/lib -llber"


gmake -j3

%install
cd postfix-%{ver}
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}/etc/init.d/ %{buildroot}/usr/local/lib/sasl/
mkdir -p %{buildroot}/usr/local/share/postfix/docs
install -m 0644 COMPATIBILITY COPYRIGHT HISTORY IPv6-ChangeLog LICENSE PORTING TLS_ACKNOWLEDGEMENTS TLS_CHANGES TLS_LICENSE US_PATENT_6321267  RELEASE_NOTES-1.0 RELEASE_NOTES-1.1 RELEASE_NOTES-2.0 RELEASE_NOTES-2.1 RELEASE_NOTES-2.2 RELEASE_NOTES-2.3 RELEASE_NOTES-2.4 RELEASE_NOTES %{buildroot}/usr/local/share/postfix/docs
sh ./postfix-install -non-interactive install_root=%{buildroot}/ \
tempdir=/tmp config_directory=/etc/postfix \
daemon_directory=/usr/local/libexec/postfix \
command_directory=/usr/local/sbin \
queue_directory=/var/spool/postfix \
sendmail_path=/usr/local/lib/sendmail \
newaliases_path=/usr/local/bin/newaliases \
mailq_path=/usr/local/bin/mailq mail_owner=postfix \
setgid_group=maildrop manpage_directory=/usr/local/man \
sample_directory=/etc/postfix \
readme_directory=/usr/local/share/postfix/docs

cp ../PFIX-TLS/etc/postfix/* %{buildroot}/etc/postfix/
cp ../PFIX-TLS/etc/init.d/* %{buildroot}/etc/init.d/
cp ../PFIX-TLS/etc/pam.conf.PFIX-TLS %{buildroot}/etc/

# postfix-TLS conflicts with gdbm
# gdbm is necessary for python
# python is necessary for unhardlinkify.py
#/usr/local/bin/unhardlinkify.py ./
# I'm just going to do this directly
cd %{buildroot}/usr/local/bin
rm -f mailq
ln -s ../lib/sendmail mailq
rm -f newaliases
ln -s ../lib/sendmail newaliases
cd %{buildroot}/usr/local/libexec/postfix
rm -f nqmgr
ln -s qmgr nqmgr
rm -f lmtp
ln -s smtp lmtp

 

%post
cat <<EOF
You must add the contents of /etc/pam.conf.PFIX-TLS to /etc/pam.conf, ex:
  cat /etc/pam.conf.PFIX-TLS >> /etc/pam.conf
You must make a symlink so postfix starts up in your favorite run-level, ex:
  ln -s /etc/init.d/postfix /etc/rc2.d/S60postfix
EOF

%postun
cat <<EOF
You should remove the postfix lines from /etc/pam.conf
You should remove the rc symlink that pointed to /etc/init.d/postfix
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace)/etc/postfix/*
%config(noreplace)/etc/init.d/postfix
%config(noreplace)/etc/pam.conf.PFIX-TLS
/usr/local/libexec/postfix
/usr/local/sbin/postalias
/usr/local/sbin/postcat
/usr/local/sbin/postconf
%attr(2755, root, maildrop) /usr/local/sbin/postdrop
%attr(2755, root, maildrop) /usr/local/sbin/postqueue
/usr/local/sbin/postfix
/usr/local/sbin/postkick
/usr/local/sbin/postlock
/usr/local/sbin/postlog
/usr/local/sbin/postmap
/usr/local/sbin/postsuper
/usr/local/lib/sendmail
/usr/local/bin/*
/usr/local/man/*/*
%attr(0700,postfix,maildrop) /var/spool/postfix/active
%attr(0700,postfix,maildrop) /var/spool/postfix/bounce
%attr(0700,postfix,maildrop) /var/spool/postfix/corrupt
%attr(0700,postfix,maildrop) /var/spool/postfix/defer
%attr(0700,postfix,maildrop) /var/spool/postfix/deferred
%attr(0700,postfix,maildrop) /var/spool/postfix/flush
%attr(0700,postfix,maildrop) /var/spool/postfix/incoming
%attr(0755,root,maildrop) /var/spool/postfix/pid
%attr(0700,postfix,maildrop) /var/spool/postfix/private
%attr(0710,postfix,maildrop) /var/spool/postfix/public
%attr(1730, postfix,maildrop) /var/spool/postfix/maildrop
%doc postfix-%{ver}/COMPATIBILITY postfix-%{ver}/COPYRIGHT postfix-%{ver}/HISTORY postfix-%{ver}/IPv6-ChangeLog postfix-%{ver}/LICENSE postfix-%{ver}/PORTING postfix-%{ver}/TLS_ACKNOWLEDGEMENTS postfix-%{ver}/TLS_CHANGES postfix-%{ver}/TLS_LICENSE postfix-%{ver}/US_PATENT_6321267  postfix-%{ver}/RELEASE_NOTES-1.0 postfix-%{ver}/RELEASE_NOTES-1.1 postfix-%{ver}/RELEASE_NOTES-2.0 postfix-%{ver}/RELEASE_NOTES-2.1 postfix-%{ver}/RELEASE_NOTES-2.2 postfix-%{ver}/RELEASE_NOTES-2.3 postfix-%{ver}/RELEASE_NOTES-2.4 postfix-%{ver}/README_FILES postfix-%{ver}/RELEASE_NOTES 

%changelog
* Fri Jan 16 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.5.5-4
- added more docs 
* Mon Sep 29 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.5.5-2
- added support for ldap tables
* Mon Sep 22 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.5.5-1
- updated to 2.5.5
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.4-2
- Added Requires: pcre >= 7.1-1, BuildRequires: pcre-devel >= 7.7.1
* Thu Aug 28 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 2.5.4-1
- Added pcre support and bumped to 2.5.4
* Mon Dec 17 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.4.6-1
- Bump to 2.4.6
* Tue Aug 14 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.4.5-1
- Bumped to 2.4.5
* Fri Dec 16 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.2.7-1
- Updated to 2.2.7, which has the TLS patch incorporated in it
