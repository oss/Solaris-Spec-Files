%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define version 1.0.3 
%define php_version 5.1.6
%define pear_path /usr/local/php-%{php_version}/bin


Name: pecl-Fileinfo
Version: %{version}
Copyright: PHP
Release: 0
Summary: a php pecl extension for identifying file types using unix "magic"
Group: Development/Libraries
Distribution: RU-Solaris
Vendor: NBCS-OSS
Source: Fileinfo-%{version}.tgz
Requires: file-info php5 php5-common
BuildRequires: php5-devel
BuildRoot: %{_tmppath}/%{name}-root
Provides: pecl-Fileinfo


%description
The functions in this module try to guess the content type and encoding of a 
file by looking for certain magic byte sequences at specific positions within 
the file. While this is not a bullet proof approach the heuristics used do a 
very good job.


%prep 
%setup -c -T

%build

%install
rm -rf %{buildroot}
CC="cc"
CXX="CC"
export CC CXX

%{pear_path}/pear -c /usr/local/lib/php/.filemap install --nodeps --packagingroot %{buildroot} %{SOURCE0} 

# Clean up unnecessary files
rm %{buildroot}%{peardir}/.filemap
rm %{buildroot}%{peardir}/.lock
rm -rf %{buildroot}%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock

%{pear_path}/pear bundle %SOURCE0
mkdir -p %{buildroot}%{peardir}/PEAR/Fileinfo
mv package.xml %{buildroot}%{peardir}/PEAR/Fileinfo/Fileinfo.xml

mkdir -p %{buildroot}%{peardir}/modules
mv  %{buildroot}/usr/local/php-%{php_version}/lib/php/extensions/no-debug-non-zts-20050922/fileinfo.so %{buildroot}%{peardir}/modules

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{peardir}/PEAR/Fileinfo/Fileinfo.xml
%{peardir}/doc/Fileinfo/CREDITS
%{peardir}/doc/Fileinfo/EXPERIMENTAL
%{peardir}/doc/Fileinfo/fileinfo.php
%{peardir}/modules/fileinfo.so

