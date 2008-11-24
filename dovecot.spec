Summary:	DOVECOT - Secure IMAP Servers
Name:		dovecot
Version:	1.1.7
Release:        1
License:	GPL
Group:		Applications/Multimedia
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Packager:       Brian Schubert <schubert@nbcs.rutgers.edu>
Url:		http://www.dovecot.org/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}-root
BuildRequires:  openldap-devel >= 2.4
Requires: 	openssl openldap-lib >= 2.4

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
LD='/usr/ccs/bin/ld' CFLAGS='-g -xs' \
SSL_BASE='/usr/local/ssl' \
SSL_CFLAGS='-I/usr/local/ssl/include' \
SSL_LIBS='-R/usr/local/lib -L/usr/local/ssl/lib'
export CC CXX CPPFLAGS LDFLAGS LD CFLAGS SSL_BASE
#%{site_perl_arch}/auto/URITH="/opt/SUNWspro/bin:${PATH}" \

./configure --prefix=/usr/local --with-ssl=openssl --disable-static

gmake

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
gmake install DESTDIR=$RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
#find . > /var/local/tmp/dovecot_file_list
#for i in `find . -name '*.a'`; do rm $i; done
for i in `find . -name '*.la'`; do rm $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README NEWS COPYING* AUTHORS ChangeLog 
/usr/local/share/doc/dovecot
/usr/local/libexec/dovecot
/usr/local/sbin/dovecot
/usr/local/sbin/dovecotpw
/usr/local/lib/dovecot
/usr/local/etc/dovecot-ldap-example.conf
/usr/local/etc/dovecot-sql-example.conf
/usr/local/etc/dovecot-example.conf
/usr/local/etc/dovecot-db-example.conf

%changelog
* Mon Nov 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.7-1
- Updated to version 1.1.7
* Tue Oct 21 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.4-1
- Built against openldap 2.4, updated to version 1.1.4
- Static libraries are no longer built (they were just deleted anyway)
* Fri Sep 12 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.3-1
- updated to 1.1.3
* Tue Aug 5 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.2-1
- bumped to latest
* Tue Jul 15 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.1-2
- Added CFLAGS for debugging, added %doc directive
* Tue Jun 24 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.1.1-1
- Updated to version 1.1.1
* Thu Jun 19 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.rc11-1
- updated to 1.1.rc11
* Fri Jan 4 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.10-1
- Updated to 1.0.10-1
* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.7-1
- Updated to 1.0.7-1
