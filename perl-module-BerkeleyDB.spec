%include perl-header.spec

Summary: Perl interface to BerkeleyDB
Name: perl-module-BerkeleyDB
Version: 0.25
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: BerkeleyDB-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: db4 >= 4.2
Requires: perl = %{perl_version}
BuildRequires: db4 >= 4.2
BuildRequires: perl = %{perl_version}

%description

%prep
%setup -n BerkeleyDB-0.25

%build
#sed  's/^INCLUDE/#INCLUDE/' config.in > config.in2
#echo "INCLUDE = /usr/local/include/db4" >> config.in2
#echo "DBNAME = -ldb-4.2" >> config.in2
#mv config.in2 config.in
rm config.in
echo "INCLUDE = /usr/local/include/db4" >> config.in
echo "LIB = /usr/local/lib" >> config.in
echo "DBNAME = -ldb-4.2" >> config.in
perl Makefile.PL 
make
make test

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
%{site_perl_arch}/auto/BerkeleyDB/*
%{site_perl_arch}/BerkeleyDB*
%{site_perl_arch}/BerkeleyDB/*
%{perl_prefix}/man/man*/*

