%define mysql_ver 4.0.13
%define mysql_pfx /usr/local/mysql-%{mysql_ver}

%define source_file mysql-%{mysql_ver}.tar.gz
Name: mysql
Version: %{mysql_ver}
Copyright: MySQL Free Public License
Group: Applications/Databases
Summary: MySQL database server
Release: 0
Source: %{source_file}
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: zlib
Requires: zlib
Requires: mysql-common mysql-server mysql-client mysql-bench mysql-test

%description
*MySQL* is a true multi-user, multi-threaded SQL database server. SQL
(Structured Query Language) is the most popular and standardized
database language in the world. *MySQL* is a client/server
implementation that consists of a server daemon `mysqld' and many
different client programs and libraries.

SQL is a standardized language that makes it easy to store, update and
access information. For example, you can use SQL to retrieve product
information and store customer information for a web site.  *MySQL* is
also fast and flexible enough to allow you to store logs and pictures
in it.

The main goals of *MySQL* are speed, robustness and ease of use.
*MySQL* was originally developed because we needed a SQL server that
could handle very large databases an order of magnitude faster than
what any database vendor could offer to us on inexpensive hardware. We
have now been using *MySQL* since 1996 in an environment with more than
40 databases containing 10,000 tables, of which more than 500 have more
than 7 million rows. This is about 100 gigabytes of mission-critical
data.

The base upon which *MySQL* is built is a set of routines that have
been used in a highly demanding production environment for many years.
Although *MySQL* is still under development, it already offers a rich
and highly useful function set.

The official way to pronounce *MySQL* is "My Ess Que Ell" (Not
MY-SEQUEL).

    [from the MySQL manual]

%package common
Summary: common libraries for MySQL
Group: Applications/Databases
%description common
This RPM contains the common libraries for MySQL.


%package bench
Summary: benchmark results for MySQL
Group: Applications/Databases
Requires: mysql-common
%description bench
This RPM contains the sql-bench portion of MySQL.


%package devel
Summary: include files, static libraries for MySQL
Group: Applications/Databases
Requires: mysql-common
%description devel
This RPM contains the header files and static libraries for MySQL.


%package client
Summary: CLI for MySQL
Group: Applications/Databases
Requires: mysql-common
%description client
CLI for MySql

%package server
Summary: MySQL server
Group: Applications/Databases
Requires: mysql-common
%description server
MySQL Server


%prep
# We need to use GNU tar, as the filenames are too long for Sun tar:
PATH="/usr/local/gnu/bin:$PATH"
export PATH
%setup -q

%build
#CC='/opt/SUNWspro/bin/cc CXX='/opt/SUNWspro/bin/CC' \
#CC='/opt/SUNWspro/bin/cc'
#CXX='/opt/SUNWspro/bin/CC'
#export CC
#export CXX
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -L%{mysql_pfx}/lib -R%{mysql_pfx}/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_pfx}/lib -R%{mysql_pfx}/lib" \
./configure --prefix=%{mysql_pfx} --enable-large-files --disable-nls

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}%{mysql_pfx}

mv %{buildroot}/usr/local/mysql-*/man %{buildroot}/usr/local
mv %{buildroot}/usr/local/mysql-*/info %{buildroot}/usr/local



%post common
if [ ! -e /usr/local/mysql ]; then
    rm -f /usr/local/mysql
    ln -s /usr/local/mysql-%{version} /usr/local/mysql
    echo creating symlink: /usr/local/mysql
fi
if [ ! -e /usr/local/lib/mysql ]; then
    rm -f /usr/local/lib/mysql
    ln -s /usr/local/mysql-%{version}/lib/mysql /usr/local/lib/mysql
    echo creating symlink: /usr/local/lib/mysql
fi


%post devel
if [ ! -e /usr/local/include/mysql ]; then
    rm -f /usr/local/include/mysql
    ln -s /usr/local/mysql-%{version}/include/mysql /usr/local/include/mysql
    echo creating symlink: /usr/local/include/mysql
fi


%post client
if [ ! -e /usr/local/bin/mysql ]; then
    rm -f /usr/local/bin/mysql
    ln -s /usr/local/mysql-%{version}/bin/mysql /usr/local/bin/mysql
    echo creating symlink: /usr/local/bin/mysql
fi

%postun common
SYM_CHECK="/usr/local/mysql /usr/local/lib/mysql"
for i in $SYM_CHECK; do
    if [ ! -e $i ]; then
	echo removing broken symlink: $i
	rm $i
    fi
done


%postun devel
SYM_CHECK="/usr/local/include/mysql"
for i in $SYM_CHECK; do
    if [ ! -e $i ]; then
	echo removing broken symlink: $i
	rm $i
    fi
done


%postun client
SYM_CHECK="/usr/local/bin/mysql"
for i in $SYM_CHECK; do
    if [ ! -e $i ]; then
	echo removing broken symlink: $i
	rm $i
    fi
done


%clean
rm -rf %{buildroot}

%files
#none in meta-package

%files common
%defattr(-,bin,bin)
%doc Docs/*
/usr/local/info/mysql.info
%{mysql_pfx}/lib/mysql/lib*.so*
%{mysql_pfx}/share/mysql

%files client
%defattr(-,bin,bin)
/usr/local/mysql-*/bin/comp_err
/usr/local/mysql-*/bin/isamchk
/usr/local/mysql-*/bin/isamlog
/usr/local/mysql-*/bin/msql2mysql
/usr/local/mysql-*/bin/my_print_defaults
/usr/local/mysql-*/bin/myisamchk
/usr/local/mysql-*/bin/myisamlog
/usr/local/mysql-*/bin/myisampack
/usr/local/mysql-*/bin/mysql_explain_log
/usr/local/mysql-*/bin/mysql_fix_extensions
/usr/local/mysql-*/bin/mysql_install
/usr/local/mysql-*/bin/mysql_secure_installation
/usr/local/mysql-*/bin/mysql_tableinfo
/usr/local/mysql-*/bin/mysql_waitpid
/usr/local/mysql-*/bin/mysqlmanager-pwgen
/usr/local/mysql-*/bin/mysqlmanagerc
/usr/local/mysql-*/bin/mysql
/usr/local/mysql-*/bin/mysql_config
/usr/local/mysql-*/bin/mysql_convert_table_format
/usr/local/mysql-*/bin/mysql_find_rows
/usr/local/mysql-*/bin/mysql_fix_privilege_tables
/usr/local/mysql-*/bin/mysql_install_db
/usr/local/mysql-*/bin/mysql_setpermission
/usr/local/mysql-*/bin/mysql_zap
/usr/local/mysql-*/bin/mysqlaccess
/usr/local/mysql-*/bin/mysqlbinlog
/usr/local/mysql-*/bin/mysqlbug
/usr/local/mysql-*/bin/mysqlcheck
/usr/local/mysql-*/bin/mysqld_multi
/usr/local/mysql-*/bin/mysqldump
/usr/local/mysql-*/bin/mysqldumpslow
/usr/local/mysql-*/bin/mysqlhotcopy
/usr/local/mysql-*/bin/mysqlimport
/usr/local/mysql-*/bin/mysqlshow
/usr/local/mysql-*/bin/mysqltest
/usr/local/mysql-*/bin/pack_isam
/usr/local/mysql-*/bin/perror
/usr/local/mysql-*/bin/replace
/usr/local/mysql-*/bin/resolve_stack_dump
/usr/local/mysql-*/bin/resolveip
%{mysql_pfx}/mysql-test
/usr/local/man/man1/*

%files server
%defattr(-,bin,bin)
/usr/local/mysql-*/bin/mysqladmin
/usr/local/mysql-*/bin/mysqld_safe*
%{mysql_pfx}/libexec/mysqld

#%files test
#%defattr(-,bin,bin)
#%{mysql_pfx}/mysql-test

%files bench
%defattr(-,bin,bin)
%{mysql_pfx}/sql-bench

%files devel
%defattr(-,bin,bin)
%{mysql_pfx}/lib/mysql/*.a
%{mysql_pfx}/include/mysql

%changelog
* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to MySQL 3.23.46
- Moved prefix to %{mysql_pfx}
