Summary: Program that wraps normal socket connections with SSL/TLS
Name: stunnel
Version: 4.20
Release: 1
Copyright: GPL
Group: Applications/Communications
Source0: stunnel-%{version}.tar.gz
Requires: tcp_wrappers openssl >= 0.9.8
BuildRequires: openssl >= 0.9.8 tcp_wrappers
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

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
# UGLY HACK OF DEATH YOU HAVE BEEN WARNED
slide make install DESTDIR=$RPM_BUILD_ROOT
# prefix=$RPM_BUILD_ROOT/usr/local
# since it's only a 0-byte file anyway
# rm $RPM_BUILD_ROOT/usr/local/etc/stunnel/stunnel.pem

slide chown -R leozh:studsys $RPM_BUILD_ROOT

%clean
slide rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/sbin/*
/usr/local/lib/*.so*
/usr/local/etc/*
/usr/local/man/*
/usr/local/share/*
/usr/local/var/*
