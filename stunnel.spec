Summary: Program that wraps normal socket connections with SSL/TLS
Name: stunnel
Version: 4.24
Release: 1
Copyright: GPL
Group: Applications/Communications
Source0: stunnel-%{version}.tar.gz
Packager: Brian Schubert <schubert@nbcs.rutgers.edu>
Requires: tcp_wrappers openssl >= 0.9.8
BuildRequires: openssl >= 0.9.8 tcp_wrappers
BuildRoot: %{_tmppath}/%{name}-root

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
./configure --with-tcp-wrappers --with-random=/var/run/urandom --localstatedir=/var --prefix=/usr/local
%else
./configure --with-tcp-wrappers --localstatedir=/var --prefix=/usr/local
%endif

gmake

%install
rm -rf %{buildroot}
slide gmake install DESTDIR=%{buildroot}
slide chown -R schubert:studsys %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/bin/stunnel*
/usr/local/etc/stunnel/*
/usr/local/lib/stunnel/*
/usr/local/share/doc/stunnel/*
/usr/local/share/man/man8/stunnel*

%changelog
* Fri May 30 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.24-1
- Updated to version 4.24
* Thu Jan 10 2008 Dave Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.21-1
- Updated to latest version
