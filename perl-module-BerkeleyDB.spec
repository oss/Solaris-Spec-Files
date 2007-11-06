%include perl-header.spec

Summary: Perl interface to BerkeleyDB
Name: perl-module-BerkeleyDB
Version: 0.32
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: BerkeleyDB-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
Requires: db4 = 4.2
Requires: perl = %{perl_version}
BuildRequires: db4 >= 4.2 db4-devel >= 4.2
BuildRequires: perl = %{perl_version}

%description

%prep
%setup -q -n BerkeleyDB-0.32

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

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

%changelog
* Tue Nov 6 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.32-1
- Updated to 0.32

