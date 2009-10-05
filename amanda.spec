%define version 2.6.1p1

Summary: amanda Backup Package
Name: amanda
Version: %{version}
Release: 1
Group: System/Backup
#Copyright: Univ. of Maryland, see COPYRIGHT
License: Copyright Univ. of Maryland, see COPYRIGHT
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

%package perl-module
Summary: AMANDA perl modules
Group: System/Backup
Requires: amanda-core = %{version} 

%description perl-module
New perl modules link directly to Amanda, to support writing Amanda applications in Perl

%package perl-module-static
Summary: AMANDA perl-module static libraries
Group: System/Backup
Requires: amanda-core = %{version} amanda-perl-module = %{version}

%description perl-module-static
statically linked libraries for amanda-perl-module

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin/:/usr/local/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/include/glib-2.0/ \
-I/usr/local/lib/glib-2.0/include/" \
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

# amtapetype is gone as of 2.6.1p1 --Jarek
#cd tape-src
#gmake amtapetype CFLAGS='-R/usr/local/lib' -j3
#cd ..

%install
/usr/local/bin/slide rm -Rf $RPM_BUILD_ROOT
/usr/local/bin/slide mkdir -p $RPM_BUILD_ROOT/usr/local
# strange, strange stuff. libtool still needs the -R.
# mildly melty
/usr/local/bin/slide gmake install DESTDIR=$RPM_BUILD_ROOT CFLAGS='-R/usr/local/lib' BINARY_OWNER=$USER SETUID_GROUP=studsys
#slide mkdir -p $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#slide cp example/amanda.conf $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1/amanda.conf.rpmnew
#slide cp example/chg-scsi-solaris.conf $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1/chg-scsi-solaris.conf.rpmnew
#slide cp example/disklist $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1/disklist.rpmnew
#slide cp example/*.ps $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#chown amanda $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#chgrp ops $RPM_BUILD_ROOT/usr/local/etc/amanda/DailySet1
#slide cp tape-src/tapetype $RPM_BUILD_ROOT/usr/local/sbin

%clean
/usr/local/bin/slide rm -Rf $RPM_BUILD_ROOT

%post
cat <<EOF
Please note that Amanda may require adding an "amanda" account, "ops" group,
editing crontab, /etc/services (and its NIS map), inetd.conf, and setting up
an e-mail alias. This package does NOT support backup via GNU tar. 
Documentation and examples are in /usr/local/share/amanda and 
/usr/local/var/lib/amanda/example.
EOF

%files core
%doc README ReleaseNotes COPYRIGHT AUTHORS UPGRADING NEWS ChangeLog
%defattr(-, amanda, ops)
/usr/local/lib/amanda/libamanda*.so
#/usr/local/lib/amanda/libamtape*.so
/usr/local/lib/amanda/libamserver*.so
/usr/local/lib/amanda/libamdevice*.so
/usr/local/lib/amanda/libamclient*.so
/usr/local/libexec/amanda/amidxtaped
/usr/local/sbin/amrestore
/usr/local/lib/amanda/libamar-2.6.1p1.so                                                                 
/usr/local/lib/amanda/libamar-2.6.1p1.so                                                                 
/usr/local/lib/amanda/libamar.a                                                                          
/usr/local/lib/amanda/libamar.la                                                                         
/usr/local/lib/amanda/libamar.so                                                                         
/usr/local/lib/amanda/libamxfer-2.6.1p1.so                                                               
/usr/local/lib/amanda/libamxfer.a                                                                        
/usr/local/lib/amanda/libamxfer.la                                                                       
/usr/local/lib/amanda/libamxfer.so
/usr/local/lib/amanda/librestore*.so
#/usr/local/libexec/amanda/application/generic-dumper
/usr/local/libexec/amanda/application/amgtar
/usr/local/share/amanda
/usr/local/share/man/man5/*
/usr/local/share/man/man8/*
/usr/local/share/man/man7/amanda*
#/usr/local/var/lib/amanda/example/*
#/usr/local/var/lib/amanda/template.d/*

%files server
%defattr(-, amanda, ops)
/usr/local/libexec/amanda/amcleanupdisk
/usr/local/libexec/amanda/amindexd
/usr/local/libexec/amanda/amlogroll
/usr/local/libexec/amanda/amtrmidx
/usr/local/libexec/amanda/amtrmlog
/usr/local/libexec/amanda/chg-chio
/usr/local/libexec/amanda/chg-chs
/usr/local/libexec/amanda/chg-manual
/usr/local/libexec/amanda/chg-mtx
/usr/local/libexec/amanda/chg-multi
/usr/local/libexec/amanda/chg-rth
/usr/local/libexec/amanda/chg-scsi
/usr/local/libexec/amanda/chg-zd-mtx
/usr/local/libexec/amanda/chg-disk
/usr/local/libexec/amanda/chg-iomega
/usr/local/libexec/amanda/chg-juke
/usr/local/libexec/amanda/chg-mcutil
/usr/local/libexec/amanda/chg-null
/usr/local/libexec/amanda/chg-rait
/usr/local/libexec/amanda/chunker
/usr/local/libexec/amanda/noop
/usr/local/libexec/amanda/driver
/usr/local/libexec/amanda/dumper
/usr/local/libexec/amanda/planner
/usr/local/libexec/amanda/taper
/usr/local/libexec/amanda/amanda-sh-lib.sh
/usr/local/libexec/amanda/application/amgtar_perl                                                        
/usr/local/libexec/amanda/application/amlog-script                                                       
/usr/local/libexec/amanda/application/amsamba                                                            
/usr/local/libexec/amanda/application/amstar                                                             
/usr/local/libexec/amanda/application/amzfs-sendrecv                                                     
/usr/local/libexec/amanda/application/amzfs-snapshot                                                     
/usr/local/libexec/amanda/application/script-email                                                       
/usr/local/libexec/amanda/chg-glue                                                                       
/usr/local/libexec/amanda/teecount                                                                       
/usr/local/sbin/amarchiver                                                                               
/usr/local/sbin/amcryptsimple                                                                            
/usr/local/sbin/amservice                                                                                
/usr/local/sbin/amvault         
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
#/usr/local/sbin/amverify
/usr/local/sbin/amaespipe
/usr/local/sbin/amcrypt
/usr/local/sbin/amcrypt-ossl
/usr/local/sbin/amcrypt-ossl-asym
#/usr/local/sbin/amdd
/usr/local/sbin/amfetchdump
#/usr/local/sbin/ammt
/usr/local/sbin/amoldrecover
/usr/local/sbin/amtapetype
#/usr/local/sbin/amverifyrun
/usr/local/sbin/amaddclient
/usr/local/sbin/amserverconfig
/usr/local/sbin/amgpgcrypt
/usr/local/sbin/amdevcheck
/usr/local/sbin/amcheckdump

%files client
%defattr(-, amanda, ops)
/usr/local/lib/amanda/libamandad*.so
/usr/local/libexec/amanda/amandad
/usr/local/libexec/amanda/calcsize
/usr/local/libexec/amanda/killpgrp
/usr/local/libexec/amanda/patch-system
/usr/local/libexec/amanda/rundump
/usr/local/libexec/amanda/runtar
/usr/local/libexec/amanda/selfcheck
/usr/local/libexec/amanda/sendbackup
/usr/local/libexec/amanda/sendsize
/usr/local/libexec/amanda/versionsuffix
/usr/local/sbin/amrecover
#/usr/local/sbin/amplot
#/usr/local/libexec/amcat.awk
#/usr/local/libexec/amplot.awk
#/usr/local/libexec/amplot.g
#/usr/local/libexec/amplot.gp
/usr/local/libexec/amanda/chg-lib.sh

%files static
%defattr(-, amanda, ops)
/usr/local/lib/amanda/libamanda.a
/usr/local/lib/amanda/libamanda.la
/usr/local/lib/amanda/libamandad.a
/usr/local/lib/amanda/libamandad.la
/usr/local/lib/amanda/libamclient.a
/usr/local/lib/amanda/libamclient.la
/usr/local/lib/amanda/libamserver.a
/usr/local/lib/amanda/libamserver.la
#/usr/local/lib/amanda/libamtape.a
#/usr/local/lib/amanda/libamtape.la
/usr/local/lib/amanda/librestore.a
/usr/local/lib/amanda/librestore.la
/usr/local/lib/amanda/libamdevice.la
/usr/local/lib/amanda/libamdevice.a
/usr/local/lib/amanda/libamglue.a
/usr/local/lib/amanda/libamglue.la

%files perl-module
%defattr(-,amanda,op)
/usr/local/lib/amanda/libamglue.so
/usr/perl5/site_perl/5.6.1/Amanda/Changer.pm
/usr/perl5/site_perl/5.6.1/Amanda/Cmdline.pm
/usr/perl5/site_perl/5.6.1/Amanda/Config.pm
/usr/perl5/site_perl/5.6.1/Amanda/Debug.pm
/usr/perl5/site_perl/5.6.1/Amanda/Device.pm
/usr/perl5/site_perl/5.6.1/Amanda/Logfile.pm
/usr/perl5/site_perl/5.6.1/Amanda/Paths.pm
#/usr/perl5/site_perl/5.6.1/Amanda/Tapefile.pm
/usr/perl5/site_perl/5.6.1/Amanda/Types.pm
/usr/perl5/site_perl/5.6.1/Amanda/Util.pm
/usr/perl5/site_perl/5.6.1/Amanda/Application.pm                                                         
/usr/perl5/site_perl/5.6.1/Amanda/Application/Zfs.pm                                                     
/usr/perl5/site_perl/5.6.1/Amanda/Archive.pm                                                             
/usr/perl5/site_perl/5.6.1/Amanda/BigIntCompat.pm                                                        
/usr/perl5/site_perl/5.6.1/Amanda/Changer/compat.pm                                                      
/usr/perl5/site_perl/5.6.1/Amanda/Changer/disk.pm                                                        
/usr/perl5/site_perl/5.6.1/Amanda/Changer/single.pm                                                      
/usr/perl5/site_perl/5.6.1/Amanda/Constants.pm                                                           
/usr/perl5/site_perl/5.6.1/Amanda/DB/Catalog.pm                                                          
/usr/perl5/site_perl/5.6.1/Amanda/MainLoop.pm                                                            
/usr/perl5/site_perl/5.6.1/Amanda/Process.pm                                                             
/usr/perl5/site_perl/5.6.1/Amanda/Script.pm                                                              
/usr/perl5/site_perl/5.6.1/Amanda/Script_App.pm                                                          
/usr/perl5/site_perl/5.6.1/Amanda/Tapelist.pm                                                            
/usr/perl5/site_perl/5.6.1/Amanda/Tests.pm
/usr/perl5/site_perl/5.6.1/Amanda/Xfer.pm
/usr/perl5/site_perl/5.6.1/auto/Amanda/Cmdline/libCmdline.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Config/libConfig.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Debug/libDebug.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Device/libDevice.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Logfile/libLogfile.so
#/usr/perl5/site_perl/5.6.1/auto/Amanda/Tapefile/libTapefile.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Types/libTypes.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Util/libUtil.so

%files perl-module-static
/usr/perl5/site_perl/5.6.1/auto/Amanda/Cmdline/libCmdline.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Cmdline/libCmdline.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Config/libConfig.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Config/libConfig.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Debug/libDebug.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Debug/libDebug.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Device/libDevice.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Device/libDevice.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Logfile/libLogfile.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Logfile/libLogfile.la
#/usr/perl5/site_perl/5.6.1/auto/Amanda/Tapefile/libTapefile.a
#/usr/perl5/site_perl/5.6.1/auto/Amanda/Tapefile/libTapefile.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Types/libTypes.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Types/libTypes.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Util/libUtil.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Util/libUtil.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Application/libApplication.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Application/libApplication.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Application/libApplication.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Archive/libArchive.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Archive/libArchive.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Archive/libArchive.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/MainLoop/libMainLoop.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/MainLoop/libMainLoop.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/MainLoop/libMainLoop.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Tapelist/libTapelist.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Tapelist/libTapelist.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Tapelist/libTapelist.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Tests/libTests.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Tests/libTests.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Tests/libTests.so
/usr/perl5/site_perl/5.6.1/auto/Amanda/Xfer/libXfer.a
/usr/perl5/site_perl/5.6.1/auto/Amanda/Xfer/libXfer.la
/usr/perl5/site_perl/5.6.1/auto/Amanda/Xfer/libXfer.so
%changelog
* Thu Oct 01 2009 Jarek Sedlacek <jarek@nbcs.rutgers.edu> - 2.6.1p1
- bumped to 2.6.1p1
- added/removed many files

* Fri Jun 06 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 2.6.0p1
- bumped to 2.6.0p1
- added new files
- added perl-module and perl-module-static packages

* Sat Nov 16 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 2.5.2p1
- Disable NLS
- Bump to 2.5.2p1
