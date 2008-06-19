%include perl-header.spec

Summary:	Perl interface to mysql
Name:		perl-module-DBD-mysql
Version:	4.007
Release:	1
Group:		System Environment/Base
Copyright:	GPL/Artistic
Source:		DBD-mysql-%{version}.tar.gz
Packager:	Brian Schubert <schubert@nbcs.rutgers.edu>
BuildRoot:	/var/tmp/%{name}-root
Requires:	perl = %{perl_version}
Requires:	mysql >= 3, mysql < 4
Requires:	perl-module-DBI
Requires:	perl-module-Data-ShowTable
BuildRequires:	perl = %{perl_version}
BuildRequires:	perl-module-DBI
BuildRequires:	perl-module-Data-ShowTable
BuildRequires:	mysql-devel >= 3, mysql-devel < 4
Obsoletes:	perl-module-Mysql

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
%setup -q -n DBD-mysql-%{version}

%build
PATH="/opt/SUNWspro/bin:/usr/local/mysql5/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS 

perl Makefile.PL --libs="-L/usr/local/lib -R/usr/local/lib -L/usr/local/mysql5/lib -R/usr/local/mysql5/lib -L/usr/local/mysql5/lib/mysql -R/usr/local/mysql5/lib/mysql -lmysqlclient -lz -lcrypt -lgen -lsocket -lnsl -lm"
gmake

%install
rm -rf %{buildroot}
%{pmake_install}
rm %{buildroot}/%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/auto/DBD/mysql
%{site_perl_arch}/Bundle/DBD/mysql.pm
%{site_perl_arch}/DBD/mysql.pm
%{site_perl_arch}/DBD/mysql/*
%{perl_prefix}/man/man3/*

%changelog
* Thu Jun 19 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 4.007-1
- Updated to version 4.007
* Tue Jan 15 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 4.006-1
- Updated to latest version (4.006)

