Summary:	DOVECOT - Secure IMAP Servers
Name:		dovecot
Version:	1.0.7
Release:        1
Copyright:	GPL
Group:		Applications/Multimedia
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Naveen Gavini <ngavini@nbcs.rutgers.edu>
Url:		http://www.dovecot.org/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root
BuildRequires:  openldap-devel
Requires: 	openssl openldap-lib

%description
Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like 
systems, written with security primarily in mind. Dovecot is an 
excellent choice for both small and large installations. It's fast, 
simple to set up, requires no special administration and it uses very 
little memory

%prep
%setup -q

%build
CC='/opt/SUNWspro/bin/cc' CXX='/opt/SUNWspro/bin/CC' \
CPPFLAGS='-I/usr/local/include -I/usr/local/ssl/include' \
LDFLAGS='-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib' \
LD='/usr/ccs/bin/ld' \
SSL_BASE='/usr/local/ssl' \
SSL_CFLAGS='-I/usr/local/ssl/include' \
SSL_LIBS='-R/usr/local/lib -L/usr/local/ssl/lib'
export CC CXX CPPFLAGS LDFLAGS LD SSL_BASE
./configure --prefix=/usr/local --with-ssl=openssl

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install DESTDIR=$RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
#find . > /var/local/tmp/dovecot_file_list
for i in `find . -name '*.a'`; do rm $i; done
for i in `find . -name '*.la'`; do rm $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/share/doc/dovecot
/usr/local/libexec/dovecot
/usr/local/sbin/dovecot
/usr/local/sbin/dovecotpw
/usr/local/lib/dovecot
/usr/local/etc/dovecot-ldap-example.conf
/usr/local/etc/dovecot-sql-example.conf
/usr/local/etc/dovecot-example.conf

%changelog
* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.7-1
- Updated to 1.0.7-1

