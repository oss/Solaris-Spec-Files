%include perl-header.spec

Summary: Perl interface to mysql
Name: perl-module-Mysql
Version: 1.2214
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Msql-Mysql-modules-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: mysql >= 3.22.32
Requires: perl-module-DBI
Requires: perl-module-Data-ShowTable
BuildRequires: perl = %{perl_version}
BuildRequires: perl-module-DBI
BuildRequires: perl-module-Data-ShowTable
%if %{which_perl} == "SOLARIS"
BuildRequires: perl-module-Data-Dumper
%endif

%description
DBD::mysql and DBD::mSQL are the Perl5 Database Interface drivers for
the mysql, mSQL 1.*x* and mSQL 2.*x* databases. The drivers are part
of the *Msql-Mysql-modules* package.

In other words: DBD::mSQL and DBD::mysql are an interface between the
Perl programming language and the mSQL or mysql programming API that
come with the mSQL any mysql relational database management systems.
Most functions provided by the respective programming API's are
supported. Some rarely used functions are missing, mainly because
noone ever requested them. :-)

%prep
%setup -q -n Msql-Mysql-modules-%{version}

%build
perl Makefile.PL --noprompt --nomsql-install
make
# make test - needs mysql -running-

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
%{site_perl_arch}/auto/DBD/mysql
%{site_perl_arch}/auto/Msql-Mysql-modules
%{site_perl_arch}/Mysql.pm
%{site_perl_arch}/Mysql
%{site_perl_arch}/Bundle/DBD/mysql.pm
%{site_perl_arch}/DBD/mysql.pm
%{perl_prefix}/man/man3/*
%{perl_prefix}/man/man1/*
%{perl_prefix}/bin/*
