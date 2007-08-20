# This originated from the imapproxy source tarball

%define ver 1.2.5
%define rel 4
%define prefix /usr/local

Summary: Imapproxy Daemon
Name: up-imapproxy
Version: %ver
Release: %rel
License: GPL
Group: Networking/Daemons
Source0: http://www.imapproxy.org/downloads/up-imapproxy-%{ver}.tar.gz
Patch: up-imapproxy.patch
Url: http://www.imapproxy.org
#Packager: Devrim SERAL <devrim@gazi.edu.tr> # he is original packager
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-%{ver}-root
Requires: openssl

#BuildRequires: Some version of openssl.. but I am lazy

%description
This is a connection caching imapproxy daemon for proxied imap connections

%prep
%setup 
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

chmod 755 ./configure
#make clean

./configure --with-prefix=%{prefix} --with-openssl=/usr/local/ssl --with-openssl-inc=/usr/local/ssl/include --with-openssl-lib=/usr/local/ssl/lib
#make OPT_FLAGS="$RPM_OPT_FLAGS" 
gmake

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/etc/init.d
install -d $RPM_BUILD_ROOT/%{prefix}/sbin

cp bin/in.imapproxyd $RPM_BUILD_ROOT/%{prefix}/sbin/
cp bin/pimpstat $RPM_BUILD_ROOT/%{prefix}/sbin/
cp scripts/imapproxy.conf $RPM_BUILD_ROOT/etc/imapproxy.conf
cp scripts/imapproxy.init $RPM_BUILD_ROOT/etc/init.d/imapproxy

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo To configure imapproxy, edit /etc/imapproxy.conf
#/sbin/chkconfig --add imapproxy

%preun
#/sbin/chkconfig --del imapproxy 

%files
%defattr(-, root, root)
%config(noreplace) /etc/imapproxy.conf
%doc README ChangeLog
%attr(750,root,root) 		/etc/init.d/imapproxy
%attr(750,root,root) 		%{prefix}/sbin/in.imapproxyd
%attr(750,root,root) 		%{prefix}/sbin/pimpstat

%changelog
* Mon Aug 20 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.2.5-4
- Updated to the latest version.

