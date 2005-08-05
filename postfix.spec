%define ver    2.1.3
%define patchl na

Summary: Secure sendmail replacement
Name: postfix-tls
Version: %{ver}
Release: 3
Group: Applications/Internet
License: IBM Public License
Source: postfix-%{ver}.tar.gz
Source1: pfixtls-0.8.18-2.1.3-0.9.7d.tar.gz
Source2: PFIX-TLS.tar
#Patch: postfix-%{ver}-%{patchl}.patch
BuildRoot: /var/tmp/%{name}-root
#Conflicts: qmail
Obsoletes: postfix <= 20010228_pl04-4ru
Conflicts: postfix <= 20010228_pl04-4ru
Requires: openssl >= 0.9.7d cyrus-sasl >= 1.5.28-6ru
BuildRequires: cyrus-sasl 
# I could swear this is legal syntax. Apparently not.
#BuildConflicts: /usr/local/include/ndbm.h
BuildConflicts: gdbm 

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
%setup -q -D -n postfix-tls -T -a 2

#%patch -p1

%build

cd postfix-%{ver}

/usr/local/gnu/bin/patch -p1 < ../pfixtls-0.8.18-2.1.3-0.9.7d/pfixtls.diff

gmake tidy

# use the system ndbm.h not /usr/local/include's one; hence BuildConflicts.

# - for cyrus-sasl 2.1.18-1 ... you need to change -lsasl to -lsasl2
# currently (Aug 2004) this only affects the solaris9-sparc64 machine
# - you also need to add the include directory of /usr/local/include/sasl

%ifos solaris2.9
 %ifarch sparc64
gmake makefiles CC=/opt/SUNWspro/bin/cc CCARGS="-DHAS_SSL -DUSE_SASL_AUTH -I/usr/local/include -I/usr/local/include/sasl -I/usr/local/ssl/include" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl2 -L/usr/local/lib -lcrypto -lssl"
 %else
gmake makefiles CC=/opt/SUNWspro/bin/cc CCARGS="-DHAS_SSL -DUSE_SASL_AUTH -I/usr/local/include -I/usr/local/ssl/include" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl -L/usr/local/lib -lcrypto -lssl"
 %endif
%else
gmake makefiles CC=/opt/SUNWspro/bin/cc CCARGS="-DHAS_SSL -DUSE_SASL_AUTH -I/usr/local/include -I/usr/local/ssl/include" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl -L/usr/local/lib -lcrypto -lssl"
%endif

gmake 


%install
cd postfix-%{ver}
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}/etc/init.d/ %{buildroot}/usr/local/lib/sasl/
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
%doc /usr/local/share/postfix/docs
