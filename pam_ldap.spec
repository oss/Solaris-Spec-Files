Summary: PAM library for LDAP
Name: pam_ldap
Version: 178
Release: 1
Source: %{name}-%{version}.tgz
URL: http://www.padl.com/
Copyright: LGPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
BuildPrereq: openldap-devel >= 2.3 openssl >= 0.9.7e automake >= 1.6
Requires: openldap-lib >= 2.3 cyrus-sasl >= 2.0.18 openssl >= 0.9.7c-7
BuildConflicts: openssl-static

%description
This package includes an open source PAM library for use as an LDAP client.

%prep

%setup

%build

%ifarch sparc64

### 64-bit

CC=/opt/SUNWspro/bin/cc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" CFLAGS="-xarch=v9" \
./configure --with-ldap-conf-file=/usr/local/etc/ldap.conf \
--with-ldap-secret-file=/usr/local/etc/ldap.secret 

# brain dead thing reruns ./configure anyway!?

sed s/-lldap/-lldap_r/g Makefile > Makefile.2
mv Makefile.2 Makefile

gmake pam_ldap_so_LDFLAGS='-Bdynamic -M ./exports.solaris \
-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -G '

%{__mv} pam_ldap.so pam_ldap_opensource.so.sparcv9
gmake distclean

%endif

### 32-bit
# --enable-debugging can be nice sometimes
CC=/opt/SUNWspro/bin/cc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --with-ldap-conf-file=/usr/local/etc/ldap.conf \
--with-ldap-secret-file=/usr/local/etc/ldap.secret \

sed s/-lldap/-lldap_r/g Makefile > Makefile.2
mv Makefile.2 Makefile

gmake pam_ldap_so_LDFLAGS='-Bdynamic -M ./exports.solaris -L/usr/local/lib \
-R/usr/local/lib -G'

%install
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/etc
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/lib
%{__cp} pam_ldap.so $RPM_BUILD_ROOT/usr/local/lib/pam_ldap_opensource.so
%{__cp} ldap.conf $RPM_BUILD_ROOT/usr/local/etc/ldap.conf.pam

%ifarch sparc64
### 64-bit
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
%{__cp} pam_ldap_opensource.so.sparcv9 $RPM_BUILD_ROOT/usr/local/lib/sparcv9/pam_ldap_opensource.so
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
%attr(0755,root,bin) /usr/local/lib/sparcv9/pam_ldap_opensource.so
%endif

%attr(0755,root,bin) /usr/local/lib/pam_ldap_opensource.so
%attr(0644,root,root) %config(noreplace) /usr/local/etc/ldap.conf.pam
%doc AUTHORS COPYING COPYING.LIB CVSVersionInfo.txt ChangeLog INSTALL NEWS
%doc README 
