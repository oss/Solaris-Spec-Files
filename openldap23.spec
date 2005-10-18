Summary: Lightweight Directory Access Protocol
Name: openldap
Version: 2.3.11
Release: 0
Group: Applications/Internet
License: OpenLDAP Public License
Source: %{name}-%{version}.tgz
Source1: default_slapd.reader 
Source2: init.d_slapd
%ifnos solaris2.7
Patch0: openldap-2.3.8-enigma.patch
%endif
BuildRoot: %{_tmppath}/%{name}-root
# An existing openldap screws up find-requires
BuildConflicts: openldap openldap-lib
BuildRequires: openssl cyrus-sasl > 2 vpkg-SPROcc tcp_wrappers gmp-devel make db4-devel > 4.2 db4 >= 4.2.52-4
# FUTURE: require versions of packages with the 64 bit stuff...
# FUTURE: figure out what userland packages actually are instead of guessing
Requires: openssl cyrus-sasl > 2 db4 >= 4.2.52-4 tcp_wrappers gmp

# define this to '1' to build openldap-server-nothreads
%define nothreads 1
# define this to the GNU make -j argument
%define dashJ -j1

%description
    The OpenLDAP Project is pleased to announce the availability
    of OpenLDAP Software 2.3, a suite of the Lightweight Directory
    Access Protocol (v3) servers, clients, utilities, and
    development tools.

    This beta release contains the following major enhancements:

        * Slapd(8) enhancements
            - Updated slapd "overlay" interface, and several
              example (and mostly experimental) overlays.
            - Updated LDAP "sync" Engine with replication support,
              provider now an "overlay"
            - Numerous access control enhancements, including
              experimental "don't disclose on error" capability
        * LDAPv3 extensions, including:
            - LDAP Component Matching (requires OpenLDAP snacc)
            - LDAP Modify Increment

    Additional functionality is expected to be added prior to
    general release.

    This release includes the following major components:

        * slapd - a stand-alone LDAP directory server
        * slurpd - a stand-alone LDAP replication server
        * -lldap - a LDAP client library
        * -llber - a lightweight BER/DER encoding/decoding library
        * LDIF tools - data conversion tools for use with slapd
        * LDAP tools - A collection of command line LDAP utilities

    In addition, there are some contributed components:

        * LDAPC++ - a LDAP C++ SDK
        * Various slapd modules and slapi plugins

  (from ANNOUNCEMENT)

%ifnos solaris2.7
This package contains support for the Rutgers rval "Enigma" protocol.
%endif

%package client
Group: System Environment/Base
Summary: client binaries for openldap
Requires: openldap = %{version}-%{release}
%description client
client binaries for openldap

%package devel
Group: Development/Headers
Summary: includes for openldap
Requires: openldap-lib = %{version}-%{release}
%description devel
includes for openldap

%package doc
Group: Documentation
Summary: Documentation for openldap
Conflicts: openldap < %{version}-%{release} openldap > %{version}-%{release}
%description doc
Documentation and man pages for openldap

%package lib
Group: System Enviroment/Base
Summary: OpenLDAP libraries
Requires: openldap = %{version}-%{release}
%description lib
Library files for openldap

%package server
Group: Applications/Internet
Summary: Threaded version of the servers
Requires: openldap = %{version}-%{release}
%description server
Threaded versions of the openldap server

%if %{nothreads}
%package server-nothreads
Group: Applications/Internet
Summary: Non-threaded version of server
Requires: openldap-server = %{version}-%{release}
%description server-nothreads
This package is a crime against humanity as we disable threads
due to Solaris issues.
%endif

%prep
%setup -q
%ifnos solaris2.7
%patch0 -p1
%endif

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH" # use sun's ar
export PATH

%if %{nothreads}
mkdir nothreads
for threadness in without with ; do # order matters due to distcleans
%else
for threadness in with ; do # nothreads == 0
%endif
%ifarch sparc64
LD_RUN_PATH=/usr/local/lib/sparcv9
export LD_RUN_PATH
CC="/opt/SUNWspro/bin/cc" STRIP='/bin/true' \
LDFLAGS="-L/usr/local/lib/sparcv9 -R/usr/local/lib/sparcv9 -L/usr/local/ssl/sparcv9/lib -L/usr/local/lib/sparcv9/sasl" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/db4 -I/usr/local/include -I/usr/local/include/heimdal -D_REENTRANT -DSLAPD_EPASSWD" \
CFLAGS="-g -xs -xarch=v9" ./configure --enable-wrappers --enable-dynamic --enable-rlookups --enable-ldap --enable-meta --enable-rewrite --enable-monitor --enable-null --enable-spasswd --${threadness}-threads --enable-bdb --enable-hdb --disable-relay --enable-overlays
gmake depend STRIP=''

gmake %{dashJ} AUTH_LIBS='-lmp' STRIP='' 
umask 022

mkdir -p sparcv9/lib
for i in liblber libldap libldap_r # not in 2.3.7 librewrite
do
    cp libraries/$i/.libs/*.so* sparcv9/lib
done

mkdir -p sparcv9/libexec
if [ ${threadness} = with ]; then
#gmake test STRIP=''
cp servers/slapd/.libs/slapd sparcv9/libexec/slapd
cp servers/slurpd/.libs/slurpd sparcv9/libexec/slurpd
else
cp servers/slapd/.libs/slapd nothreads/slapd.nothreads.64
# slurpd doesn't get made when no threads
fi

mkdir -p sparcv9/bin
for i in compare delete modify modrdn passwd search whoami
do
    cp clients/tools/.libs/ldap$i sparcv9/bin
done

gmake distclean STRIP=''
%endif # ifarch 64

### 32bit
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
CC="cc" STRIP='/bin/true' \
LDFLAGS="-L/usr/local/heimdal/lib -R/usr/local/heimdal/lib -L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib" \
CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/include/db4 -I/usr/local/include -I/usr/local/include/heimdal -D_REENTRANT -DSLAPD_EPASSWD" CFLAGS='-g -xs' \
./configure --enable-wrappers --enable-rlookups --enable-dynamic --enable-ldap --enable-meta --enable-rewrite --enable-monitor --enable-null --enable-spasswd --${threadness}-threads --enable-bdb --enable-hdb --disable-relay --enable-overlays
gmake depend STRIP=''
gmake %{dashJ} AUTH_LIBS='-lmp' STRIP=''
if [ ${threadness} != with ]; then 
cp servers/slapd/.libs/slapd nothreads/slapd.nothreads
gmake distclean STRIP=''
else
#gmake test STRIP=''
/bin/true
fi

done ; # for threadness

%install
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:$PATH" # use sun's ar
export PATH

rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
LD_RUN_PATH=/usr/local/lib
export LD_RUN_PATH
gmake install DESTDIR=%{buildroot} STRIP=''

# unfortunately the above glob includes *.la and *.lai which hurt babies.
rm -f %{buildroot}/usr/local/lib/*.la %{buildroot}/usr/local/lib/*.lai

%if %{nothreads}
mkdir -p %{buildroot}/usr/local/libexec/sparcv9
mv nothreads/slapd.nothreads %{buildroot}/usr/local/libexec/
%ifarch sparc64
mkdir -p %{buildroot}/usr/local/libexec/sparcv9/sparcv9
mv nothreads/slapd.nothreads.64 %{buildroot}/usr/local/libexec/sparcv9/slapd.nothreads
%endif
%endif

%ifarch sparc64

cd sparcv9
for i in bin lib libexec; do
	mkdir -p %{buildroot}/usr/local/$i/sparcv9
	mv $i/* %{buildroot}/usr/local/$i/sparcv9
done

mkdir -p %{buildroot}/usr/local/sbin/sparcv9

cd %{buildroot}/usr/local/sbin/sparcv9
# sbin programs are all links to slapd now
for i in acl add auth cat dn index passwd test
do
	ln -s ../../libexec/sparcv9/slapd slap$i
done

# stupid hard link
cd %{buildroot}/usr/local/bin/sparcv9
ln -sf ldapmodify ldapadd
%endif

cd %{buildroot}/usr/local/bin
ln -sf ldapmodify ldapadd

# stupid soft link
cd %{buildroot}/usr/local/sbin
for i in acl add auth cat dn index passwd test;do
ln -sf ../libexec/slapd slap$i
done

mkdir -p %{buildroot}/etc/init.d
mkdir -p %{buildroot}/etc/default
cp %{SOURCE1} %{buildroot}/etc/default/slapd
cp %{SOURCE2} %{buildroot}/etc/init.d/slapd
chmod 744 %{buildroot}/etc/init.d/slapd
chmod 644 %{buildroot}/etc/default/slapd

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
#/usr/local/share/openldap

%files client
%defattr(-, root, bin)
#%ifarch sparc64
#/usr/local/bin/sparcv9/*
#%endif
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
#/usr/local/sbin/sparcv9/*
%endif
/usr/local/libexec/slapd
/usr/local/libexec/slurpd
/usr/local/sbin/*
%config(noreplace) /etc/init.d/slapd
%config(noreplace) /etc/default/slapd
/usr/local/var/openldap-slurp

%if %{nothreads}
%files server-nothreads
%defattr(-, root, bin)
/usr/local/libexec/slapd.nothreads 
%ifarch sparc64
/usr/local/libexec/sparcv9/slapd.nothreads
%endif
%endif
