Summary: Lightweight Directory Access Protocol
Name: openldap
Version: 2.1.22
<<<<<<< openldap.spec
Release: 2
=======
Release: 4
>>>>>>> 1.18
Group: Applications/Internet
License: OpenLDAP Public License
Source: %{name}-%{version}.tgz
Source1: openldap-init.d-slapd
%ifnos solaris2.7
Patch0: openldap-2.1.21-enigma.patch
%endif
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl cyrus-sasl vpkg-SPROcc db4-devel db4
BuildRequires: heimdal-devel tcp_wrappers gmp-devel make
# FUTURE: require versions of packages with the 64 bit stuff...
# FUTURE: figure out what userland packages actually are instead of guessing
Requires: openssl cyrus-sasl db4 tcp_wrappers gmp

%description
    The OpenLDAP Project is pleased to announce the availability
    of OpenLDAP 2.0, a suite of the Lightweight Directory Access
    Protocol servers, clients, utilities, and development tools.

    This release contains the following major enhancements:

        * LDAPv3 support
            + RFC 2251-2256
            + Language Tags (RFC 2596)
            + SASL (RFC2829)
            + TLS (RFC2830) and SSL (ldaps://)
            + named references
            + DNS SRV location
        * IPv6 support
        * LDAP over IPC support
        * Updated C API
        * LDIFv1 (RFC2849)
        * Enhanced Standalone LDAP Server:
            + Updated Access Control System
            + Thread Pooling
            + DNS SRV referral backend (experimental)
            + LDAP backend (experimental)
            + SQL backend (experimental)
            + Better tools

    This release includes the following major components:

        * slapd - a stand-alone LDAP directory server
        * slurpd - a stand-alone LDAP replication server
        * -lldap - a LDAP client library
        * -llber - a lightweight BER/DER encoding/decoding library
        * LDIF tools - data conversion tools for use with slapd
        * LDAP gateways - finger, gopher, email to LDAP gateways
        * LDAP mailer - sendmail-compatible mail delivery agents
        * LDAP tools - A collection of command line LDAP utility programs

    In addition, there are some contributed components:

        * ldapTCL - the NeoSoft TCL LDAP SDK
        * gtk-tool - a demonstration ldap interface written gtk
        * php3-tool - a demonstration ldap interface written php3
        * saucer - a simple command-line oriented client program
        * whois++d - a WHOIS++-to-LDAP gateway

    This release contains a number of major code changes.  It
    might be a bit rough around the edges.  Use with appropriate
    caution.

  (from ANNOUNCEMENT)

%ifnos solaris2.7
This package contains support for the Rutgers rval "Enigma" protocol.
%endif

%package devel
Group: Development/Headers
Summary: includes for openldap

%description devel
includes for openldap

%prep
%setup -q
%ifnos solaris2.7
%patch -p1
%endif

%build
PATH="/usr/ccs/bin:$PATH" # use sun's ar
export PATH

%ifarch sparc64
LD_RUN_PATH=/usr/local/lib/sparcv9
export LD_RUN_PATH
CC="/opt/SUNWspro/bin/cc" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/sparcv9/lib -L/usr/local/lib/sparcv9/sasl" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/db4 -I/usr/local/include -I/usr/local/include/heimdal -DSLAPD_EPASSWD" \
CFLAGS="-xarch=v9" ./configure --enable-wrappers --disable-static --enable-kpasswd --enable-rlookups --enable-ldap --enable-meta --enable-rewrite --enable-monitor --enable-null
gmake depend

### Quadruple evil because of libtool ultra-badness.

gmake AUTH_LIBS='-lmp' && exit 0
# never do that
cd servers/slapd/back-bdb
# *.lo symlink -> *.o
for i in *.lo;do ln -s $i `echo $i | cut -d. -f1`.o;done
cd ../../..

### Damn it, we need to do it again.

gmake AUTH_LIBS='-lmp' && exit 0
# never do that
cd servers/slapd/back-ldap
# *.lo symlink -> *.o
for i in *.lo;do ln -s $i `echo $i | cut -d. -f1`.o;done
cd ../../..

gmake AUTH_LIBS='-lmp' && exit 0
# never do that
cd servers/slapd/back-meta
# *.lo symlink -> *.o
for i in *.lo;do ln -s $i `echo $i | cut -d. -f1`.o;done
cd ../../..

gmake AUTH_LIBS='-lmp' && exit 0
# never do that
cd servers/slapd/back-monitor
# *.lo symlink -> *.o
for i in *.lo;do ln -s $i `echo $i | cut -d. -f1`.o;done
cd ../../..

gmake AUTH_LIBS='-lmp' && exit 0
# never do that
cd servers/slapd/back-null
# *.lo symlink -> *.o
for i in *.lo;do ln -s $i `echo $i | cut -d. -f1`.o;done
cd ../../..

### End quadruple evil.

gmake AUTH_LIBS='-lmp'
umask 022

### can't do it this way, make install will fail
mkdir -p sparcv9/lib
for i in liblber libldap libldap_r 
do
    cp libraries/$i/.libs/*.so* sparcv9/lib
# sun doesn't support statics anymore
#    mv libraries/$i/.libs/$i.a sparcv9/lib
done

mkdir -p sparcv9/libexec
cp servers/slapd/slapd sparcv9/libexec/slapd
cp servers/slurpd/slurpd sparcv9/libexec/slurpd

mkdir -p sparcv9/bin
for i in compare delete modify modrdn passwd search whoami
do
    cp clients/tools/ldap$i sparcv9/bin
done

mkdir -p sparcv9/sbin
for i in add cat index passwd
do
    cp servers/slapd/tools/slap$i sparcv9/sbin
done

gmake distclean

#%else
%endif

### 32bit
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
#CC="gcc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CC="cc" LDFLAGS="-L/usr/local/heimdal/lib -R/usr/local/heimdal/lib -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/db4 -I/usr/local/include -I/usr/local/include/heimdal -DSLAPD_EPASSWD" \
./configure --enable-wrappers --enable-kpasswd --enable-rlookups --enable-ldap --enable-meta --enable-rewrite --enable-monitor --enable-null
gmake depend
gmake AUTH_LIBS='-lmp'

#%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
gmake install DESTDIR=%{buildroot}

# unfortunately the above glob includes *.la and *.lai which hurt babies.
rm -f %{buildroot}/usr/local/lib/*.la %{buildroot}/usr/local/lib/*.lai

%ifarch sparc64
### 64-bit bins belong in sparcv9 directory. hope this works.
cd sparcv9
for i in bin lib libexec sbin; do

	mkdir -p %{buildroot}/usr/local/$i/sparcv9
	mv $i/* %{buildroot}/usr/local/$i/sparcv9

done

# stupid hard link
cd %{buildroot}/usr/local/bin/sparcv9
ln -sf ldapmodify ldapadd
%endif

cd %{buildroot}/usr/local/bin
ln -sf ldapmodify ldapadd

cd %{buildroot}/usr/local/etc/openldap/schema
rm *schema

mkdir -p %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/slapd
chmod 744 %{buildroot}/etc/init.d/slapd

%clean
rm -rf %{buildroot}

%post
cat <<EOF
Edit and copy /usr/local/etc/openldap/*default and 
/usr/local/etc/openldap/schema/*default.
EOF

%files
%defattr(-, root, bin)
%doc ANNOUNCEMENT CHANGES COPYRIGHT INSTALL LICENSE README
%doc doc

%ifarch sparc64
/usr/local/bin/sparcv9/*
/usr/local/lib/sparcv9/*
/usr/local/libexec/sparcv9/*
/usr/local/sbin/sparcv9/*
%endif
#%else uncomment for 64-only package (why?)
/usr/local/bin/*
/usr/local/lib/*
/usr/local/libexec/*
/usr/local/sbin/*
#%endif

%config(noreplace) /usr/local/etc/openldap/*
/usr/local/etc/openldap/schema/*default
/usr/local/etc/openldap/schema/README
/usr/local/share/openldap
/usr/local/var/openldap-slurp
/usr/local/man/*/*

%config(noreplace) /etc/init.d/slapd

%files devel
%defattr(-, root, bin)
/usr/local/include/*
