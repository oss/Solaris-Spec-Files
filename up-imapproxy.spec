Summary: IMAP Proxy
Name: up-imapproxy 
Version: 1.1.3
Release: 1 
Group: Applications/Internet 
Copyright: GPL
Source0: up-imapproxy-1.1.3.tar.gz 
Patch0: up-imapproxy-1.1.3-Makefile.patch
Patch1: up-imapproxy-1.1.3-imapproxy.patch
Patch2: up-imapproxy-1.1.3-imapcommon.c.patch
Patch3: up-imapproxy-1.1.3-imapproxy.h.patch
BuildRoot: /var/tmp/%{name}-root
Requires: openssl

%description
The IMAP Proxy server is a caching IMAP proxy server. It was written to reduce the load
that Webmail clients put on an IMAP server by keeping server connections alive for reuse
thus avoiding a new server connection for each Webmail transaction. 

%prep
%setup -q   
cd /usr/local/src/rpm-packages/BUILD
%patch
%patch1
%patch2
%patch3
%build
make
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/sbin
mkdir -p %{buildroot}/usr/local/etc
mkdir -p %{buildroot}/usr/local/var/run 
mkdir -p %{buildroot}/etc/init.d/
cp bin/in.imapproxyd %{buildroot}/usr/local/sbin
cp bin/pimpstat %{buildroot}/usr/local/var/run
cp scripts/imapproxy %{buildroot}/etc/init.d
cp scripts/imapproxy.conf %{buildroot}/usr/local/etc
%clean
rm -rf %{buildroot}

%post


%files
%defattr(-,root,nobody)
/usr/local/sbin/in.imapproxyd
/usr/local/var/run/pimpstat
/etc/init.d/imapproxy
/usr/local/etc/imapproxy.conf
%changelog

* Fri Feb 21 2003 Christopher Wawak <cwawak@nbcs.rutgers.edu>
  - Initial package creation.
