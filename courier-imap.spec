%define version 1.4.4
%define initdir /etc/init.d

Summary: Courier-IMAP 1.4.4 IMAP server
Name: courier-imap
Version: %{version}
Release: 7
Copyright: GPL
Group: Applications/Mail
Source: courier-imap-1.4.4.tar.gz
Packager: Rutgers University
BuildRoot: /var/tmp/courier-imap-install
Requires: fileutils textutils sh-utils sed expect
BuildPreReq: textutils openssl fileutils rpm >= 4.0.2 sed perl gdbm pam expect openldap


%description
Courier-IMAP is an IMAP server for Maildir mailboxes.  This package
contains the standalone version of the IMAP server that's included in the
Courier mail server package.

%prep
%setup -q

%build

#CC='/usr/local/gcc-3.0.4/bin/sparcv9-sun-solaris2.8-gcc' \
#CXX='/usr/local/gcc-3.0.4/bin/sparcv9-sun-solaris2.8-g++' \
CFLAGS='' CXXFLAGS='' \
#CC='gcc' CXX='g++' \
#LDFLAGS='-L/usr/local/lib/64 -R/usr/local/lib/64 #-L/usr/local/gcc-3.0.4/lib -R/usr/local/gcc-3.0.4/lib -L/usr/local/ssl/sparcv9/lib' \
CC='cc' CXX='CC' \
LDFLAGS='-L/usr/local/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
CPPFLAGS='-I/usr/local/ssl/include -I/usr/local/include' \
./configure --localstatedir=/var/run \
--with-authdaemonvar=/var/run/authdaemon.courier-imap --with-db=gdbm \
--prefix=/usr/local/lib/courier-imap

make 

%install

%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/etc/pam.d
make install DESTDIR=$RPM_BUILD_ROOT
make install-configure DESTDIR=$RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{initdir}
%{__cp} courier-imap.sysvinit $RPM_BUILD_ROOT%{initdir}/courier-imap

%files
%defattr(-,root,root)
/usr/local/lib/courier-imap/*
/etc/init.d/courier-imap
/var/run/authdaemon.courier-imap

%clean
rm -rf $RPM_BUILD_ROOT
