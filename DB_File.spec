%include perl-header.spec

Summary:		DB_File
Name: 			DB_File
Version: 		1.804
Release:		5ru
Copyright: 		GPL
Group: 			Libraries/Perl
Source: 		%{name}-%{version}.tar.gz
#Patch:			rrdtool-rrdtutorial.pod.patch
Buildroot: 		/var/tmp/dbfile-root
Prefix:	 		%{_prefix}
Requires:		db

%description
DB_File libraries for Perl

%prep
%setup -q

%build

%install
echo "INCLUDE = /usr/local/include" >> config.in
echo "LIB = /usr/local/lib" >> config.in
LD_RUN_PATH=/usr/local/lib/
export LD_RUN_PATH
perl Makefile.PL
make
#%{}            
%{pmake_install}
#mkdir -p $RPM_BUILD_ROOT/%{site_perl_arch}/auto/DB_File/
rm `find %{buildroot} -name perllocal.pod`
#mv `find . -name "DB_File.pm"` $RPM_BUILD_ROOT/%{site_perl_arch}/
#mv `find . -name "DB_File.*"` $RPM_BUILD_ROOT/%{site_perl_arch}/
%ifos solaris2.9
mkdir %{buildroot}/usr/perl5/site_perl
mv %{buildroot}/usr/perl5/5* %{buildroot}/usr/perl5/site_perl
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/
#%{site_perl_arch}
