Summary: Lightweight Directory Access Protocol
Name: openldap
Version: 2.1.22
Release: 12
Group: Applications/Internet
License: OpenLDAP Public License
Source: %{name}-%{version}.tgz
Source1: openldap-init.d-slapd
%ifnos solaris2.7
Patch0: openldap-2.1.21-enigma.patch
Patch1: openldap-ssl-0.9.7.patch
%endif
BuildRoot: %{_tmppath}/%{name}-root
# An existing openldap screws up find-requires
BuildConflicts: openldap openldap-lib
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

%package client
Group: System Environment/Base
Summary: client binaries for openldap
Requires: openldap
%description client
client binaries for openldap

%package devel
Group: Development/Headers
Summary: includes for openldap
Requires: openldap-lib
%description devel
includes for openldap

%package doc
Group: Documentation
Summary: Documentation for openldap
%description doc
Documentation and man pages for openldap

%package lib
Group: System Enviroment/Base
Summary: OpenLDAP libraries
Requires: openldap
%description lib
Library files for openldap

%package server
Group: Applications/Internet
Summary: Threaded version of the servers
Requires: openldap
%description server
Threaded versions of the openldap server

%package server-nothreads
Group: Applications/Internet
Summary: Non-threaded version of server
Requires: openldap-server
%description server-nothreads
This package is a crime against humanity as we disable threads
due to Solaris issues.


%prep
%setup -q
%ifnos solaris2.7
%patch0 -p1
%patch1 -p1
%endif

%build
PATH="/usr/ccs/bin:$PATH" # use sun's ar
export PATH

mkdir nothreads
for threadness in without with ; do # order matters due to distcleans
%ifarch sparc64
LD_RUN_PATH=/usr/local/lib/sparcv9
export LD_RUN_PATH
CC="/opt/SUNWspro/bin/cc" \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/sparcv9/lib -L/usr/local/lib/sparcv9/sasl" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/db4 -I/usr/local/include -I/usr/local/include/heimdal -D_REENTRANT -DSLAPD_EPASSWD" \
CFLAGS="-g -xs -xarch=v9" ./configure --enable-wrappers --disable-static --enable-kpasswd --enable-rlookups --enable-ldap --enable-meta --enable-rewrite --enable-monitor --enable-null --${threadness}-threads
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

mkdir -p sparcv9/lib
for i in liblber libldap libldap_r 
do
    cp libraries/$i/.libs/*.so* sparcv9/lib
done

mkdir -p sparcv9/libexec
if [ ${threadness} = with ]; then
cp servers/slapd/slapd sparcv9/libexec/slapd
cp servers/slurpd/slurpd sparcv9/libexec/slurpd
else
cp servers/slapd/slapd nothreads/slapd.nothreads.64
# slurpd doesn't get made when no threads
fi

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
%endif # ifarch 64

### 32bit
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
#CC="gcc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CC="cc" LDFLAGS="-L/usr/local/heimdal/lib -R/usr/local/heimdal/lib -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/db4 -I/usr/local/include -I/usr/local/include/heimdal -D_REENTRANT -DSLAPD_EPASSWD" CFLAGS='-g -xs' \
./configure --enable-wrappers --enable-kpasswd --enable-rlookups --enable-ldap --enable-meta --enable-rewrite --enable-monitor --enable-null --${threadness}-threads
gmake depend
gmake AUTH_LIBS='-lmp'
if [ ${threadness} != with ]; then 
cp servers/slapd/slapd nothreads/slapd.nothreads
gmake distclean
fi

#%endif
done ; # for threadness

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
gmake install DESTDIR=%{buildroot}

# unfortunately the above glob includes *.la and *.lai which hurt babies.
rm -f %{buildroot}/usr/local/lib/*.la %{buildroot}/usr/local/lib/*.lai

mv nothreads/slapd.nothreads %{buildroot}/usr/local/libexec/

%ifarch sparc64
cd sparcv9
for i in bin lib libexec sbin; do

	mkdir -p %{buildroot}/usr/local/$i/sparcv9
	mv $i/* %{buildroot}/usr/local/$i/sparcv9
done

mv ../nothreads/slapd.nothreads.64 %{buildroot}/usr/local/libexec/sparcv9/slapd.nothreads

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
%config(noreplace) /usr/local/etc/openldap/*
/usr/local/share/openldap

%files client
%defattr(-, root, bin)
%ifarch sparc64
/usr/local/bin/sparcv9/*
%endif
/usr/local/bin/*

%files doc
%defattr(-, root, bin)
%doc ANNOUNCEMENT CHANGES COPYRIGHT INSTALL LICENSE README
%doc doc
/usr/local/man/*/*

%files devel
%defattr(-, root, bin)
/usr/local/include/*
/usr/local/lib/*.a

%files lib
%defattr(-, root, bin)
%ifarch sparc64
/usr/local/lib/sparcv9/*.so*
%endif
/usr/local/lib/*.so*

%files server
%defattr(-, root, bin)
%ifarch sparc64
/usr/local/libexec/sparcv9/slapd
/usr/local/libexec/sparcv9/slurpd
/usr/local/sbin/sparcv9/*
%endif
/usr/local/libexec/slapd
/usr/local/libexec/slurpd
/usr/local/sbin/*
%config(noreplace) /etc/init.d/slapd
/usr/local/var/openldap-slurp

%files server-nothreads
%defattr(-, root, bin)
/usr/local/libexec/slapd.nothreads 
%ifarch sparc64
/usr/local/libexec/sparcv9/slapd.nothreads
%endif
