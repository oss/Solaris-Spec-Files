Summary: Lightweight Directory Access Protocol
Name: openldap
Version: 2.1.5
Release: 1ru
Group: Applications/Internet
License: OpenLDAP Public License
Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl cyrus-sasl vpkg-SPROcc db4-devel db4
Requires: openssl cyrus-sasl db4

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

%package devel
Group: Development/Headers
Summary: includes for openldap

%description devel
includes for openldap


%prep
%setup -q

%build
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
#CC="gcc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CC="cc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/include/db4 -I/usr/local/ssl/include -I/usr/local/db4/include" \
./configure
#make depend
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
make install prefix=%{buildroot}/usr/local

#this is wierd:
%ifos solaris2.9
%ifarch sparc64
mv ./libraries/libldap/.libs/libldap.so.2.0.105U ./libraries/libldap/.libs/libldap.so.2.0.105
%endif
%endif

#for some reason the 2.1.5 Makefile doesn't install this file:
cp ./libraries/libldap/.libs/libldap* %{buildroot}/usr/local/lib/
#I use 'cp'... 'install' can KMA

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
/usr/local/lib/liblber*
/usr/local/lib/libldap*
/usr/local/etc/openldap/*default
/usr/local/etc/openldap/schema/*default
/usr/local/share/openldap
/usr/local/bin/*
/usr/local/libexec/*
#/usr/local/var/openldap-ldbm
/usr/local/var/openldap-slurp
/usr/local/sbin/*
/usr/local/man/*/*

%files devel
%defattr(-, root, bin)
/usr/local/include/*
