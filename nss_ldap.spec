Summary: NSS library for LDAP
Name: nss_ldap
Version: 215
Release: 2
Source: ftp://ftp.padl.com/pub/%{name}-%{version}.tar.gz
URL: http://www.padl.com/
Copyright: LGPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-root
BuildPrereq: openldap-devel >= 2.1.21 openssl >= 0.9.6g automake >= 1.6
Requires: openldap >= 2.1.21 cyrus-sasl >= 1.5.28-4ru openssl >= 0.9.6g

%description
This package includes a LDAP access client: nss_ldap.
Nss_ldap is a set of C library extensions which allows X.500 and LDAP
directory servers to be used as a primary source of aliases, ethers,
groups, hosts, networks, protocol, users, RPCs, services and shadow
passwords (instead of or in addition to using flat files or NIS).


Install nss_ldap if you need LDAP access clients.

%prep

%setup

%build

%ifarch sparc64

### 64-bit

# --enable-debugging can be nice sometimes too
CC=/opt/SUNWspro/bin/cc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9" CFLAGS="-xarch=v9" \
./configure --with-ldap-conf-file=/usr/local/etc/ldap.conf \
--with-ldap-secret-file=/usr/local/etc/ldap.secret \
--enable-rfc2307bis --enable-schema-mapping 

# brain dead thing reruns ./configure anyway!?

make nss_ldap_so_LDFLAGS='-Bdynamic -M ./exports.solaris \
-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -ldb-4 -G '

%{__mv} nss_ldap.so nss_ldap.so.sparcv9
make distclean

%endif

### 32-bit
# --enable-debugging can be nice sometimes
CC=/opt/SUNWspro/bin/cc CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
./configure --with-ldap-conf-file=/usr/local/etc/ldap.conf \
--with-ldap-secret-file=/usr/local/etc/ldap.secret \
--enable-rfc2307bis --enable-schema-mapping \
# brain dead thing reruns ./configure anyway!?
make nss_ldap_so_LDFLAGS='-Bdynamic -M ./exports.solaris -L/usr/local/lib \
-R/usr/local/lib -ldb-4 -G'

%install
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/etc
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/lib
%{__cp} nss_ldap.so $RPM_BUILD_ROOT/usr/local/lib/nss_ldap.so
%{__cp} ldap.conf $RPM_BUILD_ROOT/usr/local/etc/ldap.conf.nsswitch

%ifarch sparc64
### 64-bit
%{__mkdir} -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
%{__cp} nss_ldap.so.sparcv9 $RPM_BUILD_ROOT/usr/local/lib/sparcv9/nss_ldap.so
%endif

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
cat << EOF
******** IMPORTANT INSTRUCTIONS ON HOW TO BREAK YOUR SOLARIS INSTALLATION

	nss_ldap package is DISABLED BY DEFAULT. If this is your
	initial installation, you must activate the package:

# you are messing with Solaris components here!
	mv /usr/lib/nss_ldap.so.1 /usr/lib/nss_ldap.so.1.solaris
	ln -s /usr/local/lib/nss_ldap.so /usr/lib/nss_ldap.so.1
%ifarch sparc64
	mv /usr/lib/sparcv9/nss_ldap.so.1 /usr/lib/sparcv9/nss_ldap.so.1.solaris
	ln -s /usr/local/lib/sparcv9/nss_ldap.so /usr/lib/sparcv9/nss_ldap.so.1
%endif

	Think once, twice, or maybe even five times before doing this.
	
	RUTGERS RPM WILL NEVER MESS WITH YOUR /USR/LIB DIRECTORY. IF YOU
	UNINSTALL THIS PACKAGE, CLEAN UP THE PIECES YOURSELF.

	Configuration files live in /usr/local/etc/ldap.{conf,secret}.
	Please use /usr/local/etc/ldap.conf.nsswitch as your basis.

******** END IMPORTANT INSTRUCTIONS
EOF

%files
%defattr(-,root,bin)

%ifarch sparc64
%attr(0755,root,bin) /usr/local/lib/sparcv9/nss_ldap.so
%endif

%attr(0755,root,bin) /usr/local/lib/nss_ldap.so
%attr(0644,root,root) %config(noreplace) /usr/local/etc/ldap.conf.nsswitch
%doc ANNOUNCE README ChangeLog AUTHORS NEWS COPYING
%doc nsswitch.ldap doc/*
