%define ver    20010228
%define patchl pl04 

Summary: Secure sendmail replacement
Name: postfix
Version: %{ver}_%{patchl}
Release: 3
Group: Applications/Internet
License: IBM Public License
Source: postfix-%{ver}-%{patchl}.tar.gz
Patch: postfix-%{ver}-%{patchl}.patch
BuildRoot: /var/tmp/%{name}-root
#Conflicts: qmail
Requires: cyrus-sasl
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
%setup -q -n %{name}-%{ver}-%{patchl}
%patch -p1

%build
/usr/ccs/bin/make tidy

# use the system ndbm.h not /usr/local/include's one

#/usr/ccs/bin/make makefiles CCARGS='-DUSE_SASL_AUTH -I/usr/local/include' AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl" 

#/usr/ccs/bin/make makefiles CCARGS=-DPATH_NDBM_H=\\\\\\\"/usr/include/ndbm.h\\\\\\\"

/usr/ccs/bin/make makefiles CCARGS="-DUSE_SASL_AUTH -I/usr/local/include -DPATH_NDBM_H=\\\\\\\"/usr/include/ndbm.h\\\\\\\"" AUXLIBS="-L/usr/local/lib -R/usr/local/lib -lsasl" 

#/usr/ccs/bin/make makefiles CCARGS='-DUSE_SASL_AUTH -I/usr/local/include' AUXLIBS="-L/usr/lib -R/usr/lib -lc -L/usr/local/lib -R/usr/local/lib -lsasl" 


/usr/ccs/bin/make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
/usr/ccs/bin/make install </dev/null
for i in access aliases canonical main.cf master.cf \
         relocated transport virtual; do
    mv %{buildroot}/etc/postfix/$i %{buildroot}/etc/postfix/$i.rpm
done

%post
cat <<EOF
You must edit and move 

  access.rpm
  aliases.rpm
  canonical.rpm
  main.cf.rpm
  master.cf.rpm
  relocated.rpm
  transport.rpm
  virtual.rpm

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *README COMPATIBILITY TODO RELEASE_NOTES PORTING HISTORY INSTALL LICENSE
/etc/postfix/access.rpm
/etc/postfix/aliases.rpm
/etc/postfix/canonical.rpm
/etc/postfix/LICENSE
/etc/postfix/main.cf.rpm
/etc/postfix/main.cf.default
/etc/postfix/master.cf.rpm
/etc/postfix/pcre_table
/etc/postfix/postfix-script
/etc/postfix/postfix-script-diff
/etc/postfix/postfix-script-nosgid
/etc/postfix/postfix-script-sgid
/etc/postfix/regexp_table
/etc/postfix/relocated.rpm
/etc/postfix/sample-aliases.cf
/etc/postfix/sample-auth.cf
/etc/postfix/sample-canonical.cf
/etc/postfix/sample-compatibility.cf
/etc/postfix/sample-debug.cf
/etc/postfix/sample-filter.cf
/etc/postfix/transport.rpm
/etc/postfix/sample-flush.cf
/etc/postfix/sample-ldap.cf
/etc/postfix/sample-lmtp.cf
/etc/postfix/sample-local.cf
/etc/postfix/sample-misc.cf
/etc/postfix/sample-pcre.cf
/etc/postfix/sample-rate.cf
/etc/postfix/sample-regexp.cf
/etc/postfix/sample-relocated.cf
/etc/postfix/sample-resource.cf
/etc/postfix/sample-rewrite.cf
/etc/postfix/sample-smtp.cf
/etc/postfix/sample-smtpd.cf
/etc/postfix/sample-transport.cf
/etc/postfix/sample-virtual.cf
/etc/postfix/virtual.rpm
/etc/postfix/install.cf
/usr/local/libexec/postfix
/usr/local/sbin/postalias
/usr/local/sbin/postcat
/usr/local/sbin/postconf
%attr(2755, root, mail) /usr/local/sbin/postdrop
/usr/local/sbin/postfix
/usr/local/sbin/postkick
/usr/local/sbin/postlock
/usr/local/sbin/postlog
/usr/local/sbin/postmap
/usr/local/sbin/postsuper
/usr/local/lib/sendmail
/usr/local/bin/*
/usr/local/man/*/*
%dir /var/spool/postfix
%attr(1730, postfix, mail) /var/spool/postfix/maildrop
