%define source_file mysql-3.23.39.tar.gz
Name: mysql
Version: 3.23.39
Copyright: MySQL Free Public License
Group: Applications/Databases
Summary: MySQL database server
Release: 2
Source: %{source_file}
BuildRoot: /var/tmp/%{name}-root
BuildRequires: zlib
Requires: zlib

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

%package bench
Summary: benchmark results for MySQL
Group: Applications/Databases

%description bench
This RPM contains the sql-bench portion of MySQL.

%package devel
Summary: include files, static libraries for MySQL
Group: Applications/Databases

%description devel
This RPM contains the header files and static libraries for MySQL.

%prep
%setup -q

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql/lib -R/usr/local/mysql/lib" LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql/lib -R/usr/local/mysql/lib" ./configure --prefix=/usr/local/mysql --enable-large-files
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local/mysql

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/mysql/info/mysql.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/mysql/info/mysql.info
fi

%files
%defattr(-,bin,bin)
%doc Docs/*
/usr/local/mysql/info/mysql.info
/usr/local/mysql/lib/mysql/lib*.so*
/usr/local/mysql/bin/*
/usr/local/mysql/share/mysql
/usr/local/mysql/libexec/mysqld
/usr/local/mysql/man/man1/mysql.1

%files bench
%defattr(-,bin,bin)
/usr/local/mysql/sql-bench

%files devel
%defattr(-,bin,bin)
/usr/local/mysql/lib/mysql/*a
/usr/local/mysql/include/mysql
