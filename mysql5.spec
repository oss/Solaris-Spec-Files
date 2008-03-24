%define mysql_ver 5.0.51a
%define mysql_pfx /usr/local/mysql-%{mysql_ver}
%define source_file mysql-%{mysql_ver}.tar.gz

Name:		mysql5
Version:	%{mysql_ver}
License:	MySQL Free Public License
Group:		Applications/Databases
Summary:	MySQL database server
Release:	1
Source:		%{source_file}
BuildRequires:	zlib
BuildRoot:	%{_tmppath}/%{name}-root
Provides:	mysql
Requires:	mysql5-common = %{version}-%{release} mysql5-server = %{version}-%{release} mysql5-client = %{version}-%{release} zlib

%description
The MySQL(TM) software delivers a very fast, multi-threaded, multi-user,
and robust SQL (Structured Query Language) database server. MySQL Server
is intended for mission-critical, heavy-load production systems as well
as for embedding into mass-deployed software. MySQL is a trademark of
MySQL AB.

The MySQL software has Dual Licensing, which means you can use the MySQL
software free of charge under the GNU General Public License
(http://www.gnu.org/licenses/). You can also purchase commercial MySQL
licenses from MySQL AB if you do not wish to be bound by the terms of
the GPL. See the chapter "Licensing and Support" in the manual for
further info.

The MySQL web site (http://www.mysql.com/) provides the latest
news and information about the MySQL software. Also please see the
documentation and the manual for more information.

The official way to pronounce *MySQL* is "My Ess Que Ell" (Not
MY-SEQUEL).

    [from the MySQL manual]

%package common
Summary: common libraries for MySQL
Group: Applications/Databases
%description common
This RPM contains the common libraries for MySQL.

%package server
Summary: MySQL server
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description server
MySQL Server


%package bench
Summary: benchmark results for MySQL
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description bench
This RPM contains the sql-bench portion of MySQL.


%package devel
Summary: include files, static libraries for MySQL
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description devel
This RPM contains the header files and static libraries for MySQL.


%package client
Summary: Client for mysql
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description client
Client for mysql

%package ndb-storage
Release: %{release}
Summary: mysql - ndbcluster storage engine
Requires: mysql5-common = %{version}-%{release}
Group: Applications/Databases
%description ndb-storage
This package contains the ndbcluster storage engine.
It is necessary to have this package installed on all
computers that should store ndbcluster table data.
Note that this storage engine can only be used in conjunction
with the MySQL Max server.


%package ndb-management
Release: %{release}
Summary: mysql - ndbcluster storage engine management
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description ndb-management
This package contains ndbcluster storage engine management.
It is necessary to have this package installed on at least
one computer in the cluster.


%package ndb-tools
Release: %{release}
Summary: mysql - ndbcluster storage engine basic tools
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description ndb-tools
This package contains ndbcluster storage engine basic tools.


%package ndb-extra
Release: %{release}
Summary: mysql - ndbcluster storage engine extra tools
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release}
%description ndb-extra
This package contains some extra ndbcluster storage engine tools for the 
advanced user. They should be used with caution.

%package max
Release: %{release}
Summary: mysql - server with extended functionality
Group: Applications/Databases
Requires: mysql5-common = %{version}-%{release} mysql5-server = %{version}-%{release} 
%description max
Optional MySQL server binary that supports additional features like:
 - Berkeley DB Storage Engine
 - Ndbcluster Storage Engine interface
 - Archive Storage Engine
To activate this binary, just install this package in addition to
the standard MySQL package.
Please note that this is a dynamically linked binary!


%prep
# We need to use GNU tar, as the filenames are too long for Sun tar:
PATH="/opt/SUNWspro/bin:/usr/local/lib:/usr/ccs/bin:/usr/local/gnu/bin:/usr/local/bin"
export PATH

%setup -q -n mysql-%{version}

%build
# I can't imagine that "cc" is looked at.
cc=/opt/SUNWspro/bin/cc
CC=/opt/SUNWspro/bin/cc
CFLAGS='-g -xs -Xa -xarch=v8plus -mt -xstrconst -D_FORTEC_'
ASFLAGS='-xarch=v8plus'
CXXFLAGS='-g -xs -xarch=v8plus -noex -mt  -D_FORTEC_'
CXX=/opt/SUNWspro/bin/CC
export cc
export CXX
export CC
export ASFLAGS
export CFLAGS
export CXXFLAGS
LD="/usr/ccs/bin/ld" 
export LD
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/sfw/lib -R/usr/sfw/lib -L%{mysql_pfx}/lib -R/usr/local/mysql5/lib -L/usr/lib -R/usr/lib" 
export LDFLAGS

RBR=%{buildroot}
MBD=$RPM_BUILD_DIR/mysql-%{mysql_ver}

# Clean up the BuildRoot first
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot};

#Build Max
./configure \
	--prefix=%{mysql_pfx} \
	--enable-assembler \
	--enable-thread-safe-client \
	--with-innodb \
	--with-ndbcluster \
	--with-archive-storage-engine \
	--with-vio \
	--with-named-curses-libs=-lcurses \
	--enable-local-infile \
	--with-named-z-libs=no ;
gmake -j8

# Save mysqld-max
# if you are wondering why mysqld is hiding in .libs, it's because libtool
# needs to obfuscutate the installation process. Yes Virgina, libtool
# sucks. 
#mv sql/.libs/mysqld sql/mysqld-max
#maybe it doesn't hide in libs anymore 
mv sql/mysqld sql/mysqld-max


# Save the perror binary so it supports the NDB error codes (BUG#13740)
mv extra/perror extra/perror.ndb

# Install the ndb binaries
(cd ndb; make install DESTDIR=$RBR)

#save man pages for ndb stuff
(cd man; tar cf $RBR/man.tar ndb*\.1)


# Save libraries
(cd libmysql/.libs; tar cf $RBR/shared-libs.tar *.so*)
(cd libmysql_r/.libs; tar rf $RBR/shared-libs.tar *.so*)
(cd ndb/src/.libs; tar rf $RBR/shared-libs.tar *.so*)
make clean

#build vanilla
./configure \
	--disable-shared \
	--prefix=%{mysql_pfx} \
	--enable-assembler \
	--enable-thread-safe-client \
	--with-named-curses-libs=-lcurses \
	--enable-local-infile \
	--with-named-z-libs=no ;
gmake -j8

%install
RBR=%{buildroot}
MBD=$RPM_BUILD_DIR/mysql-%{mysql_ver}

# install all binaries 
make install DESTDIR=$RBR 

# Install shared libraries 
(cd $RBR%{mysql_pfx}/lib; tar xf $RBR/shared-libs.tar; rm -f $RBR/shared-libs.tar)

#install ndb man pages
(cd $RBR%{mysql_pfx}/man/man1; tar xf $RBR/man.tar; rm -f $RBR/man.tar)

# install saved mysqld-max
install -m755 $MBD/sql/mysqld-max $RBR%{mysql_pfx}/libexec/mysqld-max

# install saved perror binary with NDB support (BUG#13740)
install  -m 755 $MBD/extra/perror.ndb $RBR%{mysql_pfx}/bin/perror

# Touch the place where the my.cnf config file might be located
# Just to make sure it's in the file list and marked as a config file

# destroy all .la files, .a files are in devel
# libtool is stupid and so are its .la files
find $RBR -name *\.la | xargs -i rm {}

# mysql make install is dumb, it builds these no matter what, and we
# don't want to package them or have packages fail on unpacked file warnings
# rm $RBR%{mysql_pfx}/bin/make_win_binary_distribution
# rm $RBR%{mysql_pfx}/bin/make_win_src_distribution

mv $RBR%{mysql_pfx}/info $RBR/usr/local/

%post common
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
	--entry "* mysql-%{mysql_ver}: (mysql).                Mysql Database" \
		/usr/local/info/mysql.info
fi

echo
echo ATTENTION: MySQL searches for run time libraries in /usr/local/mysql5/lib
echo This installation will not function unless a symbolic link is created 
echo that points to %{mysql_pfx} from /usr/local/mysql5
echo In other words THIS INSTALLATION IS NOT COMPLETE UNTIL THE FOLLOWING 
echo COMMAND IS RUN: 
echo 
echo ln -s %{mysql_pfx} /usr/local/mysql5
echo 

#if [ ! -d /usr/local/mysql ]; then
#    rm -f /usr/local/mysql
#    ln -s /usr/local/mysql-%{mysql_ver} /usr/local/mysql
#    echo creating symlink: /usr/local/mysql
#fi

#if [ ! -d /usr/local/lib/mysql ]; then
#    rm -f /usr/local/lib/mysql
#    ln -s /usr/local/mysql-%{mysql_ver}/lib/mysql /usr/local/lib/mysql
#    echo creating symlink: /usr/local/lib/mysql
#fi


%post devel
#if [ ! -d /usr/local/include/mysql ]; then
#    rm -f /usr/local/include/mysql
#    ln -s /usr/local/mysql-%{mysql_ver}/include/mysql /usr/local/include/mysql
#    echo creating symlink: /usr/local/include/mysql
#fi

%post max
cat << EOF
The mysql max server has support for clustering and InnoDB tables. It is 
installed in /usr/local/mysql-%{mysql_ver}/libexec as mysqld-max. It can be 
invoked in the same way as the mysqld daemon.
EOF	 

%post client
#if [ ! -d /usr/local/bin/mysql ]; then
#    rm -f /usr/local/bin/mysql
#    ln -s /usr/local/mysql-%{mysql_ver}/bin/mysql /usr/local/bin/mysql
#    echo creating symlink: /usr/local/bin/mysql
#fi

%preun common
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		/usr/local/info/mysql.info
fi

%postun common
#SYM_CHECK="/usr/local/mysql /usr/local/lib/mysql"
#for i in $SYM_CHECK; do
#    if [ ! -d $i ] && [ -L $i ]; then
#        echo removing broken symlink: $i
#        rm $i
#    fi
#done


%postun devel
#SYM_CHECK="/usr/local/include/mysql"
#for i in $SYM_CHECK; do
#    if [ ! -d $i ] && [ -L $i ]; then
#        echo removing broken symlink: $i
#        rm $i
#    fi
#done

%postun client
#SYM_CHECK="/usr/local/bin/mysql"
#for i in $SYM_CHECK; do
#    if [ ! -d $i ] && [ -L $i ]; then
#        echo removing broken symlink: $i
#        rm $i
#    fi
#done

%clean
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot};








%files
#none in meta-package

%files common
%defattr(-, root, root)
%{mysql_pfx}/share/mysql/
%doc %{_infodir}/mysql.info*
%doc %{mysql_pfx}/man/man1/mysqlman.1*
%doc %{mysql_pfx}/man/man1/comp_err.1
%{mysql_pfx}/lib/*.so*
%{mysql_pfx}/lib/mysql/libndbclient.so.2.0.0


%files client
%defattr(-, root, root)
%{mysql_pfx}/bin/msql2mysql
%{mysql_pfx}/bin/mysql
%{mysql_pfx}/bin/mysql_find_rows
%{mysql_pfx}/bin/mysql_tableinfo
%{mysql_pfx}/bin/mysql_waitpid
%{mysql_pfx}/bin/mysqlaccess
%{mysql_pfx}/bin/mysqladmin
%{mysql_pfx}/bin/mysqlbinlog
%{mysql_pfx}/bin/mysqlcheck
%{mysql_pfx}/bin/mysqldump
%{mysql_pfx}/bin/mysqldumpslow
%{mysql_pfx}/bin/mysqlimport
%{mysql_pfx}/bin/mysqlshow

%doc %{mysql_pfx}/man/man1/mysql.1*
%doc %{mysql_pfx}/man/man1/mysqlaccess.1*
%doc %{mysql_pfx}/man/man1/mysqladmin.1*
%doc %{mysql_pfx}/man/man1/mysqldump.1*
%doc %{mysql_pfx}/man/man1/mysqlshow.1*
%doc %{mysql_pfx}/man/man1/msql2mysql.1*
%doc %{mysql_pfx}/man/man1/mysqlbinlog.1*
%doc %{mysql_pfx}/man/man1/mysqlimport.1*
%doc %{mysql_pfx}/man/man1/mysqlcheck.1*
%doc %{mysql_pfx}/man/man1/mysql_upgrade.1*

%files server
%defattr(-, root, root)
%doc COPYING README
%doc support-files/my-*.cnf
%doc support-files/ndb-*.ini
%doc %{mysql_pfx}/man/man1/resolveip.1
%doc %{mysql_pfx}/man/man1/resolve_stack_dump.1
%doc %{mysql_pfx}/man/man1/mysql_convert_table_format.1
%doc %{mysql_pfx}/man/man1/mysql_setpermission.1
%doc %{mysql_pfx}/man/man1/mysql_install_db.1
%doc %{mysql_pfx}/man/man1/my_print_defaults.1
%doc %{mysql_pfx}/man/man1/mysql_tzinfo_to_sql.1
%doc %{mysql_pfx}/man/man1/myisamchk.1*
%doc %{mysql_pfx}/man/man1/myisamlog.1*
%doc %{mysql_pfx}/man/man1/mysql_zap.1*
%doc %{mysql_pfx}/man/man1/myisampack.1*
%doc %{mysql_pfx}/man/man1/mysql.server.1*
%doc %{mysql_pfx}/man/man1/mysql_fix_privilege_tables.1*
%doc %{mysql_pfx}/man/man1/mysqld_multi.1*
%doc %{mysql_pfx}/man/man1/mysqld_safe.1*
%doc %{mysql_pfx}/man/man1/safe_mysqld.1*
%doc %{mysql_pfx}/man/man1/mysqlhotcopy.1*
%doc %{mysql_pfx}/man/man1/perror.1*
%doc %{mysql_pfx}/man/man1/replace.1*
%doc %{mysql_pfx}/man/man1/myisam_ftdump.1*
%doc %{mysql_pfx}/man/man1/mysql_explain_log.1
%doc %{mysql_pfx}/man/man8/mysqld.8
%doc %{mysql_pfx}/man/man8/mysqlmanager.8
%doc %{mysql_pfx}/man/man1/mysqltest.1
%{mysql_pfx}/bin/my_print_defaults
%{mysql_pfx}/bin/myisamchk
%{mysql_pfx}/bin/myisam_ftdump
%{mysql_pfx}/bin/myisamlog
%{mysql_pfx}/bin/myisampack
%{mysql_pfx}/bin/mysql_convert_table_format
%{mysql_pfx}/bin/mysql_explain_log
%{mysql_pfx}/bin/mysql_fix_extensions
%{mysql_pfx}/bin/mysql_fix_privilege_tables
%{mysql_pfx}/bin/mysql_install_db
%{mysql_pfx}/bin/mysql_secure_installation
%{mysql_pfx}/bin/mysql_setpermission
%{mysql_pfx}/bin/mysql_tzinfo_to_sql
%{mysql_pfx}/bin/mysql_zap
%{mysql_pfx}/bin/mysqlbug
%{mysql_pfx}/bin/mysqld_multi
%{mysql_pfx}/bin/mysqld_safe
%{mysql_pfx}/bin/mysqlhotcopy
%{mysql_pfx}/bin/mysqltest
%{mysql_pfx}/bin/mysql_upgrade
%{mysql_pfx}/bin/perror
%{mysql_pfx}/bin/replace
%{mysql_pfx}/bin/resolve_stack_dump
%{mysql_pfx}/bin/resolveip
%{mysql_pfx}/bin/innochecksum
%{mysql_pfx}/bin/mysql_upgrade_shell
%{mysql_pfx}/libexec/mysqld
%{mysql_pfx}/libexec/mysqlmanager

%files ndb-storage
%defattr(-, root, root)
%doc %{mysql_pfx}/man/man1/ndbd.1
%{mysql_pfx}/libexec/ndbd

%files ndb-management
%defattr(-, root, root)
%doc %{mysql_pfx}/man/man1/ndb_mgm.1
%doc %{mysql_pfx}/man/man1/ndb_mgmd.1
%{mysql_pfx}/libexec/ndb_mgmd



%files ndb-tools
%defattr(-, root, root)
%doc %{mysql_pfx}/man/man1/ndb_config.1
%doc %{mysql_pfx}/man/man1/ndb_desc.1
%doc %{mysql_pfx}/man/man1/ndb_restore.1
%doc %{mysql_pfx}/man/man1/ndb_select_all.1
%doc %{mysql_pfx}/man/man1/ndb_select_count.1
%doc %{mysql_pfx}/man/man1/ndb_show_tables.1
%doc %{mysql_pfx}/man/man1/ndb_size.pl.1
%doc %{mysql_pfx}/man/man1/ndb_waiter.1
%doc %{mysql_pfx}/man/man1/ndb_error_reporter.1
%doc %{mysql_pfx}/man/man1/ndb_print_backup_file.1
%doc %{mysql_pfx}/man/man1/ndb_print_schema_file.1
%doc %{mysql_pfx}/man/man1/ndb_print_sys_file.1
%{mysql_pfx}/bin/ndb_mgm
%{mysql_pfx}/bin/ndb_restore
%{mysql_pfx}/bin/ndb_waiter
%{mysql_pfx}/bin/ndb_select_all
%{mysql_pfx}/bin/ndb_select_count
%{mysql_pfx}/bin/ndb_desc
%{mysql_pfx}/bin/ndb_show_tables
%{mysql_pfx}/bin/ndb_test_platform
%{mysql_pfx}/bin/ndb_config
%{mysql_pfx}/bin/ndb_error_reporter
%{mysql_pfx}/bin/ndb_size.pl


%files ndb-extra
%defattr(-, root, root)
%doc %{mysql_pfx}/man/man1/ndb_cpcd.1
%doc %{mysql_pfx}/man/man1/ndb_delete_all.1
%doc %{mysql_pfx}/man/man1/ndb_drop_index.1
%doc %{mysql_pfx}/man/man1/ndb_drop_table.1
%{mysql_pfx}/bin/ndb_drop_index
%{mysql_pfx}/bin/ndb_drop_table
%{mysql_pfx}/bin/ndb_delete_all
%{mysql_pfx}/libexec/ndb_cpcd

%files devel
%defattr(-, root, root)
%doc EXCEPTIONS-CLIENT
%{mysql_pfx}/bin/comp_err
%{mysql_pfx}/bin/mysql_config
%dir %{mysql_pfx}/include/mysql
%dir %{mysql_pfx}/lib/mysql
%{mysql_pfx}/include/mysql/*
%{mysql_pfx}/lib/mysql/libheap.a
%{mysql_pfx}/lib/mysql/libmyisam.a
%{mysql_pfx}/lib/mysql/libmyisammrg.a
%{mysql_pfx}/lib/mysql/libmysqlclient.a
%{mysql_pfx}/lib/mysql/libmysqlclient_r.a
%{mysql_pfx}/lib/mysql/libmystrings.a
%{mysql_pfx}/lib/mysql/libmysys.a
%{mysql_pfx}/lib/mysql/libvio.a
%{mysql_pfx}/lib/mysql/libdbug.a
%{mysql_pfx}/lib/mysql/libndbclient.a
%{mysql_pfx}/lib/mysql/libz.a
%doc %{mysql_pfx}/man/man1/mysql_config.1*

%files bench
%defattr(-, root, root)
%doc %{mysql_pfx}/man/man1/mysql-stress-test.pl.1
%doc %{mysql_pfx}/man/man1/mysql-test-run.pl.1
%doc %{mysql_pfx}/man/man1/mysql_client_test.1
%{mysql_pfx}/sql-bench
%{mysql_pfx}/mysql-test
%{mysql_pfx}/bin/mysql_client_test
%{mysql_pfx}/bin/mysqltestmanager
%{mysql_pfx}/bin/mysqltestmanager-pwgen
%{mysql_pfx}/bin/mysqltestmanagerc

%files max
%defattr(-, root, root)
%doc %{mysql_pfx}/man/man1/innochecksum.1
%{mysql_pfx}/libexec/mysqld-max

%changelog
* Mon Mar 24 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.0.51a-1
- Bumped to 5.0.51a
* Fri Jul 13 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 5.0.45-1
- Bumped to 5.0.45
* Wed Aug 17 2005 John Santel <jmsl@nbcs.rutgers.edu>
- mysql still builds against zlib: added it back to dependencies
- fixed sh incompatible tests for symlinks

* Fri Jul 15 2005 John Santel <jmsl@nbcs.rutgers.edu>
- wow no one has touched this changelog in a while: lots of stuff
- based the revisions on the official spec file from the MySQL AB srpm
- added package for Max server to enable clustering and other neat stuff
like innodb
- removed the dependency on zlib, MySQL AB official binaries don't depend on it
- added find command to destroy evil .la files

* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to MySQL 3.23.46
- Moved prefix to %{mysql_pfx}
