Summary: Program that wraps normal socket connections with SSL/TLS
Name: stunnel
Version: 4.04
Release: 0
Copyright: GPL
Group: Applications/Communications
Source0: stunnel-%{version}.tar.gz
Requires: tcp_wrappers openssl >= 0.9.6g
BuildRequires: openssl >= 0.9.6g tcp_wrappers
BuildRoot: /var/tmp/%{name}-root

%description 
The stunnel program is designed to work as SSL encryption wrapper between
remote clients and local (inetd-startable) or remote servers. The concept
is that having non-SSL aware daemons running on your system you can easily
set them up to communicate with clients over secure SSL channels. stunnel
can be used to add SSL functionality to commonly used inetd daemons like
POP-2, POP-3, and IMAP servers, to standalone daemons like NNTP, SMTP and
HTTP, and in tunneling PPP over network sockets without changes to the
source code.

%prep
%setup -q

%build
LDFLAGS='-L/usr/ssl/lib -R/usr/ssl/lib -L/usr/local/lib -R/usr/local/lib' \
%ifnos solaris2.9
./configure --with-tcp-wrappers --with-random=/var/run/urandom --localstatedir=/var
%else
./configure --with-tcp-wrappers --localstatedir=/var
%endif
touch tools/stunnel.pem
make
touch tools/stunnel.pem

%install
#make install DESTDIR=$RPM_BUILD_ROOT prefix=$RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local
# prefix=$RPM_BUILD_ROOT/usr/local
# since it's only a 0-byte file anyway
rm $RPM_BUILD_ROOT/usr/local/etc/stunnel/stunnel.pem

%clean
make distclean

%files
%defattr(-,root,root)
/usr/local/*

