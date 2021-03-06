Summary:	PAM library for LDAP
Name:		pam_ldap
Version:	184
Release:	6
Source:		%{name}-%{version}.tgz
Patch0:		pam_ldap-184-failedlogin.patch
Patch1:		pam_ldap-malloc.mapfile.patch
URL:		http://www.padl.com/
License:	LGPL
Group:		System Environment/Base
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	openldap-devel >= 2.4 openssl >= 0.9.8g-3 automake >= 1.6
Requires:	openldap-lib >= 2.4 cyrus-sasl >= 2.0.18 openssl >= 0.9.8g-3
BuildConflicts:	openssl-static

%description
This package includes an open source PAM library for use as an LDAP client.

%prep

%setup -q
%patch0 -p1
%patch1 -p0

%build

%ifarch sparc64

### 64-bit

CC=/opt/SUNWspro/bin/cc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" CFLAGS="-xarch=v9 -g -xs -Kpic" \
./configure --with-ldap-conf-file=/usr/local/etc/ldap.conf \
--with-ldap-secret-file=/usr/local/etc/ldap.secret 

# brain dead thing reruns ./configure anyway!?

### richton thinks that ldap_r might be wrong. OpenSSL locking_callback's get stomped by
### OpenLDAP libldap_r. Trust The Upstream.
#sed s/-lldap/-lldap_r/g Makefile > Makefile.2
#mv Makefile.2 Makefile

gmake pam_ldap_so_LDFLAGS='-Bdirect -Bdynamic -M ./exports.solaris \
-z ignore -z text -z defs -lc \
-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -G '

%{__mv} pam_ldap.so pam_ldap_opensource.so.sparcv9
gmake distclean

%endif

### 32-bit
# --enable-debugging can be nice sometimes
CC=/opt/SUNWspro/bin/cc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CFLAGS="-g -xs -Kpic" \
./configure --with-ldap-conf-file=/usr/local/etc/ldap.conf \
--with-ldap-secret-file=/usr/local/etc/ldap.secret 

### richton thinks that ldap_r might be wrong. Trust The Upstream.
#sed s/-lldap/-lldap_r/g Makefile > Makefile.2
#mv Makefile.2 Makefile

gmake pam_ldap_so_LDFLAGS='-Bdirect -Bdynamic -M ./exports.solaris -L/usr/local/lib \
-R/usr/local/lib -z ignore -z text -z defs -lc -G'

%install
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/etc
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/lib
%{__cp} pam_ldap.so $RPM_BUILD_ROOT/usr/local/lib/pam_ldap_opensource.so.1
%{__cp} ldap.conf $RPM_BUILD_ROOT/usr/local/etc/ldap.conf.pam

%ifarch sparc64
### 64-bit
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
%{__cp} pam_ldap_opensource.so.sparcv9 $RPM_BUILD_ROOT/usr/local/lib/sparcv9/pam_ldap_opensource.so.1
%endif

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
cat << EOF

So as not to conflict with Solaris pam_ldap, we have placed the open
source module in pam_ldap_opensource.so.

Configuration lives in /usr/local/etc/ldap.{conf,secret}.
Please use /usr/local/etc/ldap.conf.pam as your basis.

******** END IMPORTANT INSTRUCTIONS
EOF

%files
%defattr(-,root,bin)

%ifarch sparc64
%attr(0755,root,bin) /usr/local/lib/sparcv9/pam_ldap_opensource.so.1
%endif

%attr(0755,root,bin) /usr/local/lib/pam_ldap_opensource.so.1
%attr(0644,root,root) %config(noreplace) /usr/local/etc/ldap.conf.pam
%doc AUTHORS COPYING COPYING.LIB CVSVersionInfo.txt ChangeLog INSTALL NEWS
%doc README

%changelog
* Thu Apr 6 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 184-6
- patched exports.solaris mapfile to add in malloc lines from openldap24 

* Wed Oct 29 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 184-5
- Respin for openldap 2.4

* Thu Jul 12 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 184-1
- Updated to 184
