%define mysql_ver 3.23.49
%define mysql_pfx /usr/local/mysql-%{mysql_ver}

%define source_file mysql-%{mysql_ver}.tar.gz
Name: mysql
Version: %{mysql_ver}
Copyright: MySQL Free Public License
Group: Applications/Databases
Summary: MySQL database server
Release: 1
Source: %{source_file}
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: zlib tar
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
# We need to use GNU tar, as the filenames are too long for Sun tar:
PATH="/usr/local/gnu/bin:$PATH"
export PATH
%setup -q

%build
#CC='/opt/SUNWspro/bin/cc CXX='/opt/SUNWspro/bin/CC' \
CC='/opt/SUNWspro/bin/cc'
CXX='/opt/SUNWspro/bin/CC'
export CC
export CXX
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib -L%{mysql_pfx}/lib -R%{mysql_pfx}/lib" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L%{mysql_pfx}/lib -R%{mysql_pfx}/lib" \
./configure --prefix=%{mysql_pfx} --enable-large-files

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install prefix=%{buildroot}%{mysql_pfx}

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc Docs/*
%{mysql_pfx}/info/*
%{mysql_pfx}/lib/mysql/lib*.so*
%{mysql_pfx}/bin/*
%{mysql_pfx}/share/mysql
%{mysql_pfx}/libexec/*
%{mysql_pfx}/man/man1/*
%{mysql_pfx}/mysql-test

%files bench
%defattr(-,bin,bin)
%{mysql_pfx}/sql-bench

%files devel
%defattr(-,bin,bin)
%{mysql_pfx}/lib/mysql/*a
%{mysql_pfx}/include/mysql

%changelog
* Thu Dec 20 2001 Samuel Isaacson <sbi@nbcs.rutgers.edu>
- Upgraded to MySQL 3.23.46
- Moved prefix to %{mysql_pfx}
