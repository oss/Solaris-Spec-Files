%define ver    1.1.11
%define patchl na

Summary: Secure sendmail replacement
Name: postfix-tls
Version: %{ver}
Release: 0.6ru
Group: Applications/Internet
License: IBM Public License
Source: postfix-%{ver}.tar.gz
Source1: pfixtls-0.8.11a-1.1.11-0.9.6g.tar.gz
Source2: PFIX-TLS.tar
#Patch: postfix-%{ver}-%{patchl}.patch
BuildRoot: /var/tmp/%{name}-root
#Conflicts: qmail
Obsoletes: postfix
Provides: postfix
Requires: openssl >= 0.9.6g cyrus-sasl >= 1.5.28
BuildRequires: cyrus-sasl

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

/usr/local/gnu/bin/patch -p1 < ../pfixtls-0.8.11a-1.1.11-0.9.6g/pfixtls.diff

/usr/ccs/bin/make tidy

# use the system ndbm.h not /usr/local/include's one

##/usr/ccs/bin/make makefiles CCARGS='-DUSE_SASL_AUTH -I/usr/local/include' AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl" 

##/usr/ccs/bin/make makefiles CCARGS=-DPATH_NDBM_H=\\\\\\\"/usr/include/ndbm.h\\\\\\\"

#last good one:
#/usr/ccs/bin/make makefiles CCARGS="-DUSE_SASL_AUTH -I/usr/local/include -DPATH_NDBM_H=\\\\\\\"/usr/include/ndbm.h\\\\\\\"" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl" 

##/usr/ccs/bin/make makefiles CCARGS='-DUSE_SASL_AUTH -I/usr/local/include' AUXLIBS="-L/usr/lib -R/usr/lib -lc -L/usr/local/lib -R/usr/local/lib -lsasl" 

%ifarch sparc64
/usr/ccs/bin/make makefiles CCARGS="-DHAS_SSL -DUSE_SASL_AUTH -I/usr/local/include -I/usr/local/ssl/sparcv9/include -DPATH_NDBM_H=\\\\\\\"/usr/include/ndbm.h\\\\\\\"" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl -L/usr/local/lib -lcrypto -lssl"
%else
/usr/ccs/bin/make makefiles CCARGS="-DHAS_SSL -DUSE_SASL_AUTH -I/usr/local/include -I/usr/local/ssl/include -DPATH_NDBM_H=\\\\\\\"/usr/include/ndbm.h\\\\\\\"" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl -L/usr/local/lib -lcrypto -lssl"
%endif

gmake


%install
cd postfix-%{ver}
rm -rf %{buildroot}
mkdir -p %{buildroot} %{buildroot}/etc/init.d/ %{buildroot}/usr/local/lib/sasl/
sh ./postfix-install -non-interactive install_root=%{buildroot}/ \
tempdir=/tmp/wherever config_directory=/etc/postfix \
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

#/usr/ccs/bin/make install </dev/null
#for i in access aliases canonical main.cf master.cf \
#         relocated transport virtual; do
#    mv %{buildroot}/etc/postfix/$i %{buildroot}/etc/postfix/$i.rpm
#done

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
%doc *README README-RU varspoolpostfixPerms COMPATIBILITY TODO RELEASE_NOTES PORTING HISTORY INSTALL LICENSE
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
%attr(0700,postfix,maildrop) /var/spool/postfix/saved
%attr(1730, postfix,maildrop) /var/spool/postfix/maildrop
