Name: uwash
Version: 4.44
Release: 2
Summary: UWash Pine email daemons
Copyright: UWash
Group: Applications/Email
#Source0: %{name}%{version}.tar.gz
Source0: pine%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildRequires: openssl

%description 
Pine comes with various pop/imap daemons; this package contains them. This
package has SSL support. This version does NOT include support for the
"mbox" driver, nor for LDAP. This release uses the PAM libraries.

%prep
%setup -q -n pine4.44

%build
cd imap
sed s/'EXTRADRIVERS=mbox'/'EXTRADRIVERS='/g Makefile > Makefile.ru
mv Makefile.ru Makefile
cd ..
./build NOLDAP gs5 PASSWDTYPE=pmb

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/

install -m0755 imapd/imapd $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 ipopd/ipop2d $RPM_BUILD_ROOT/usr/local/sbin/
install -m0755 ipopd/ipop3d $RPM_BUILD_ROOT/usr/local/sbin/

mkdir -p $RPM_BUILD_ROOT/usr/local/man/man8/
install -m0644 imap/src/imapd/imapd.8c $RPM_BUILD_ROOT/usr/local/man/man8/imapd.8
install -m0644 imap/src/ipopd/ipopd.8c $RPM_BUILD_ROOT/usr/local/man/man8/ipopd.8

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
#%doc *.8
%{_mandir}/man8/*
/usr/local/sbin/i*
