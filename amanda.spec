%define version 2.5.2p1

Summary: amanda Backup Package
Name: amanda
Version: %{version}
Release: 1
Group: System/Backup
Copyright: Univ. of Maryland, see COPYRIGHT
Source: amanda-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%package core
Summary: AMANDA core libraries and documentation
Group: System/Backup

%description
AMANDA, the Advanced Maryland Automatic Network Disk Archiver, is a backup
system that allows the administrator of a LAN to set up a single master
backup server to back up multiple hosts to a single large capacity tape
drive. AMANDA users native dump and/or GNU tar facilities and can back up 
a large number of workstations running multiple versions of Unix. Recent
versions can also use SAMBA to back up Microsoft Windows 95/NT hosts. 

%description core
Core libraries and documentation required by both AMANDA client and server.

%package server
Summary: AMANDA server binaries and example configuration
Group: System/Backup
Requires: amanda-core = %{version}

%description server
Binaries for the AMANDA tape server (ie, the machine with a tape drive.)

%package client
Summary: AMANDA client binaries
Group: System/Backup
Requires: amanda-core = %{version}

%description client
Binaries for the AMANDA client, which will be backed up on the tape drive of
the AMANDA server.

%package static
Summary: AMANDA static libraries
Group: System/Backup
Requires: amanda-core = %{version}

%description static
static libraries for AMANDA

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure \
	--with-user=amanda \
	--with-group=studsys \
	--with-tape-device=/dev/null \
	--with-changer-device=/dev/null \
	--without-gnutar \
	--with-index-server=truth \
	--without-built-manpages \
	--disable-nls

for i in `find . -name Makefile`; do mv $i $i.wrong; sed -e 's/-lintl//g' $i.wrong > $i; rm $i.wrong; done

gmake CFLAGS='-R/usr/local/lib -DGETPGRP_VOID' -j3
cd tape-src
gmake amtapetype CFLAGS='-R/usr/local/lib' -j3
cd ..

%install
slide rm -Rf $RPM_BUILD_ROOT
slide mkdir -p $RPM_BUILD_ROOT/usr/local
# strange, strange stuff. libtool still needs the -R.
# mildly melty
slide gmake install DESTDIR=$RPM_BUILD_ROOT CFLAGS='-R/usr/local/lib' BINARY_OWNER=$USER SETUID_GROUP=studsys
#slide mkdir -p $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#slide cp example/amanda.conf $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1/amanda.conf.rpmnew
#slide cp example/chg-scsi-solaris.conf $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1/chg-scsi-solaris.conf.rpmnew
#slide cp example/disklist $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1/disklist.rpmnew
#slide cp example/*.ps $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#chown amanda $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#chgrp ops $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#slide cp tape-src/tapetype $RPM_BUILD_ROOT/usr/local/sbin

%clean
slide rm -Rf $RPM_BUILD_ROOT

%post
cat <<EOF
Please note that Amanda may require adding an "amanda" account, "ops" group,
editing crontab, /etc/services (and its NIS map), inetd.conf, and setting up
an e-mail alias. This package does NOT support backup via GNU tar. 
Documentation and examples are in /usr/local/share/amanda and 
/usr/local/etc/amanda.
EOF

%files core
%defattr(-, amanda, ops)
/usr/local/lib/libamanda*.so
/usr/local/lib/libamtape*.so
/usr/local/libexec/amidxtaped
/usr/local/sbin/amrestore
/usr/local/lib/librestore*.so
/usr/local/dumper/generic-dumper
/usr/local/dumper/amgtar
/usr/local/share/amanda
/usr/local/man/man5/*
/usr/local/man/man8/*

%files server
%defattr(-, amanda, ops)
/usr/local/lib/libamserver*.so
/usr/local/libexec/amcleanupdisk
/usr/local/libexec/amindexd
/usr/local/libexec/amlogroll
/usr/local/libexec/amtrmidx
/usr/local/libexec/amtrmlog
/usr/local/libexec/chg-chio
/usr/local/libexec/chg-chs
/usr/local/libexec/chg-manual
/usr/local/libexec/chg-mtx
/usr/local/libexec/chg-multi
/usr/local/libexec/chg-rth
/usr/local/libexec/chg-scsi
/usr/local/libexec/chg-zd-mtx
/usr/local/libexec/chg-disk
/usr/local/libexec/chg-iomega
/usr/local/libexec/chg-juke
/usr/local/libexec/chg-mcutil
/usr/local/libexec/chg-null
/usr/local/libexec/chg-rait
/usr/local/libexec/chunker
/usr/local/libexec/noop
/usr/local/libexec/driver
/usr/local/libexec/dumper
/usr/local/libexec/planner
/usr/local/libexec/taper
/usr/local/sbin/amadmin
/usr/local/sbin/amcheck
/usr/local/sbin/amcheckdb
/usr/local/sbin/amcleanup
/usr/local/sbin/amdump
/usr/local/sbin/amflush
/usr/local/sbin/amgetconf
/usr/local/sbin/amlabel
/usr/local/sbin/amoverview
/usr/local/sbin/amreport
/usr/local/sbin/amrmtape
/usr/local/sbin/amstatus
/usr/local/sbin/amtape
/usr/local/sbin/amtoc
/usr/local/sbin/amverify
/usr/local/sbin/amaespipe
/usr/local/sbin/amcrypt
/usr/local/sbin/amcrypt-ossl
/usr/local/sbin/amcrypt-ossl-asym
/usr/local/sbin/amdd
/usr/local/sbin/amfetchdump
/usr/local/sbin/ammt
/usr/local/sbin/amoldrecover
/usr/local/sbin/amtapetype
/usr/local/sbin/amverifyrun

%files client
%defattr(-, amanda, ops)
/usr/local/lib/libamclient*.so
/usr/local/lib/libamandad*.so
/usr/local/libexec/amandad
/usr/local/libexec/calcsize
/usr/local/libexec/killpgrp
/usr/local/libexec/patch-system
/usr/local/libexec/rundump
/usr/local/libexec/runtar
/usr/local/libexec/selfcheck
/usr/local/libexec/sendbackup
/usr/local/libexec/sendsize
/usr/local/libexec/versionsuffix
/usr/local/sbin/amrecover
/usr/local/sbin/amplot
/usr/local/libexec/amcat.awk
/usr/local/libexec/amplot.awk
/usr/local/libexec/amplot.g
/usr/local/libexec/amplot.gp
/usr/local/libexec/chg-lib.sh

%files static
%defattr(-, amanda, ops)
/usr/local/lib/libamanda.a
/usr/local/lib/libamanda.la
/usr/local/lib/libamandad.a
/usr/local/lib/libamandad.la
/usr/local/lib/libamclient.a
/usr/local/lib/libamclient.la
/usr/local/lib/libamserver.a
/usr/local/lib/libamserver.la
/usr/local/lib/libamtape.a
/usr/local/lib/libamtape.la
/usr/local/lib/librestore.a
/usr/local/lib/librestore.la


%changelog
* Sat Nov 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.2p1
- Disable NLS
- Bump to 2.5.2p1
