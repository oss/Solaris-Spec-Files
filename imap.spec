Name: imap
Version: 2002.RC6
Release: RU1
Summary: UWash imap daemons
Copyright: UWash
Group: Applications/Email
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl
Obsoletes: uwash mlock imap-utils
Patch0: imap-2002-DEV-RU5.patch

%description 
Uwash's various pop/imap daemons. This package has SSL support. This
version does NOT include support for the "mbox" driver, nor for LDAP. This
release uses the PAM libraries. This includes a patch for Rutgers 
strangeness. This does NOT include a patch for Maildir.

As of IMAP-2002, Mark Crispin has started including utilities formerly of 
imap-utils with the daemons. This package reflects this.

%prep
%setup -q

%patch -p1 -P 0

%build
make sol PASSWDTYPE=pmb SSLTYPE=unix

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/etc/
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/
mkdir -p %{buildroot}/usr/local/man/man1/
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8/

install -m0755 imapd/imapd $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 ipopd/ipop2d $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 ipopd/ipop3d $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 dmail/dmail %{buildroot}/usr/local/bin/
install -m0755 mailutil/mailutil %{buildroot}/usr/local/bin/
install -m0755 mlock/mlock %{buildroot}/etc/
install -m0755 mtest/mtest %{buildroot}/usr/local/bin/
install -m0755 tmail/tmail %{buildroot}/usr/local/bin/

install -m0644 src/imapd/imapd.8c $RPM_BUILD_ROOT/usr/local/man/man8/imapd.8
install -m0644 src/ipopd/ipopd.8c $RPM_BUILD_ROOT/usr/local/man/man8/ipopd.8

install -m0644 src/mailutil/mailutil.1 %{buildroot}/usr/local/man/man1/
install -m0644 src/dmail/dmail.1 %{buildroot}/usr/local/man/man1/
install -m0644 src/tmail/tmail.1 %{buildroot}/usr/local/man/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
/etc/mlock has been installed setgid mail. This is probably a bad idea if 
you don't use a mail spool that requires it; rm and/or chmod it if this is 
the case.

EOF

%files 
%defattr(-,root,root)
%doc CONTENTS CPYRIGHT README SUPPORT WARNING docs/*
%{_mandir}/man8/*
%{_mandir}/man1/*
/usr/local/sbin/*
/usr/local/bin/*
%attr(2511,root,mail) /etc/mlock
