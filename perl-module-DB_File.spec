%include perl-header.spec

Summary:		DB_File
Name: 			perl-module-DB_File
Version: 		1.815
Release:		2
Copyright: 		GPL
Group: 			Libraries/Perl
Source: 		DB_File-%{version}.tar.gz
#Patch:			rrdtool-rrdtutorial.pod.patch
Buildroot: 		/var/tmp/dbfile-root
Prefix:	 		%{_prefix}
Requires:		db
Provides:		DB_File
Obsoletes:		DB_File

%description
DB_File libraries for Perl

%prep
%setup -q -n DB_File-%{version}

%build
echo "INCLUDE = /usr/local/include" >> config.in
echo "LIB = /usr/local/lib" >> config.in
perl Makefile.PL
make
#make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{global_perl_arch}/DB_File.pm
%{global_perl_arch}/auto/DB_File/*
%{global_perl_arch}/auto/DB_File/.*
%{perl_prefix}/man/*
