Summary: Lightweight Directory Access Protocol
Name: openldap
Version: 2.0.25
Release: 2
Group: Applications/Internet
License: OpenLDAP Public License
Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl cyrus-sasl vpkg-SPROcc
Requires: openssl cyrus-sasl

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

%prep
%setup -q

%build
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
#CC="gcc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CC="cc" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
./configure
#make depend
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
make install prefix=%{buildroot}/usr/local

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
/usr/local/include/*
/usr/local/lib/*
/usr/local/etc/openldap/*default
/usr/local/etc/openldap/schema/*default
/usr/local/share/openldap
/usr/local/bin/*
/usr/local/libexec/*
/usr/local/var/openldap-ldbm
/usr/local/var/openldap-slurp
/usr/local/sbin/*
/usr/local/man/*/*
