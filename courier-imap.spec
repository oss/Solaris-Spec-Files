Summary: Courier-IMAP 1.3.9 IMAP server
Name: courier-imap
Version: 1.3.9
Release: 1
Copyright: GPL
Group: Applications/Mail
Source: courier-imap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: fileutils textutils sh-utils openssl openldap gdbm expect
BuildRequires: textutils fileutils perl gdbm openldap openssl
BuildRequires: vpkg-SPROcc expect

%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package
contains the standalone version of the IMAP server that's included in
the Courier mail server package.  This package is a standalone version
for use with other mail servers.  Do not install this package if you
intend to install the full Courier mail server.  Install the Courier
package instead.

%prep
%setup -q

%build
CC="/opt/SUNWspro/bin/cc" CXX="/opt/SUNWspro/bin/CC" \
LDFLAGS="-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include" \
 OPENSSL="/usr/local/ssl/bin/openssl" \
./configure --localstatedir=/var/run --prefix=/usr/local/courier-imap \
--with-authdaemonvar=/var/run/authdaemon.courier-imap --with-db=gdbm \
--with-waitfunc=wait3
make
# make check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}
make install-configure DESTDIR=%{buildroot}
for i in %{buildroot}/usr/local/courier-imap/etc/*; do
    mv $i $i.rpm
done

%post
cat <<EOF
Edit and move the files in /usr/local/courier-imap/etc.
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
/usr/local/courier-imap
/var/run/*

