Name: imap
Version: 2002.RC3
Release: RU1
Summary: UWash imap daemons
Copyright: UWash
Group: Applications/Email
Source0: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl
Obsoletes: uwash
Patch0: imap-2002-Maildir.patch
Patch1: imap-2002-DEV-RU4.patch

%description 
Uwash's various pop/imap daemons. This package has SSL support. This
version does NOT include support for the "mbox" driver, nor for LDAP. This
release uses the PAM libraries. This includes a patch for Rutgers 
strangeness. This includes a patch for Maildir.

%prep
%setup -q

%patch -p1 -P 0
%patch -p1 -P 1

%build
make sol PASSWDTYPE=pmb SSLTYPE=unix

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/

install -m0755 imapd/imapd $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 ipopd/ipop2d $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 ipopd/ipop3d $RPM_BUILD_ROOT/usr/local/sbin/

mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8/
install -m0644 src/imapd/imapd.8c $RPM_BUILD_ROOT/usr/local/man/man8/imapd.8
install -m0644 src/ipopd/ipopd.8c $RPM_BUILD_ROOT/usr/local/man/man8/ipopd.8

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc CONTENTS CPYRIGHT README README.maildir SUPPORT WARNING docs/*
%{_mandir}/man8/*
/usr/local/sbin/i*
