%include perl-header.spec
%define mysql_version 3.23.55

Summary: Perl interface to mysql
Name: perl-module-DBD-mysql
Version: 2.9002
Release: 6
Group: System Environment/Base
Copyright: GPL/Artistic
Source: DBD-mysql-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: mysql
Requires: perl-module-DBI
Requires: perl-module-Data-ShowTable
BuildRequires: perl = %{perl_version}
BuildRequires: perl-module-DBI
BuildRequires: perl-module-Data-ShowTable
Obsoletes: perl-module-Mysql

%description
DBD::mysql and DBD::mSQL are the Perl5 Database Interface drivers for
the mysql, mSQL 1.*x* and mSQL 2.*x* databases. The drivers are part
of the *Msql-Mysql-modules* package.

In other words: DBD::mSQL and DBD::mysql are an interface between the
Perl programming language and the mSQL or mysql programming API that
come with the mSQL any mysql relational database management systems.
Most functions provided by the respective programming APIs are
supported. Some rarely used functions are missing, mainly because
noone ever requested them. :-)

%prep
%setup -q -n DBD-mysql-2.9002

%build
PATH="/usr/local/mysql-%{mysql_version}/bin:$PATH"
export PATH
perl Makefile.PL --libs="-L/usr/local/lib -R/usr/local/lib -L/usr/local/lib/mysql -R/usr/local/lib/mysql -L/usr/local/mysql-3.23.55/lib -R/usr/local/mysql-3.23.55/lib -L/usr/local/mysql-3.23.55/lib/mysql -R/usr/local/mysql-3.23.55/lib/mysql -lmysqlclient -lz -lcrypt -lgen -lsocket -lnsl -lm"
make
# make test - needs mysql -running-

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
#make install PREFIX=$RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/auto/DBD/mysql
%{site_perl_arch}/Mysql.pm
%{site_perl_arch}/Mysql
%{site_perl_arch}/Bundle/DBD/mysql.pm
%{site_perl_arch}/DBD/mysql.pm
#%{perl_prefix}/man/man3/*
#%{perl_prefix}/man/man1/*
#%{perl_prefix}/bin/*
