# ACHTUNG: we are building this using Pear (despite being a "Pecl 
# package"). Pear expects to be run as root. It seems that while building this 
# package, Pear updates its channel information. After the package finishes 
# building, Pear tries to write this information to /usr/local/lib/php and 
# fails. This prevents the package from building. If the "pear.php.net"
# channel is reasonably up to date, this doesn't happen. So, if you want
# to be able to build this package: 

# RUN $ slide /usr/local/php-5.1.6/bin/pear channel-update pear.php.net 
# BEFORE CONTINUING 

#%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)

#where pear wants to install to 
%define peardir /usr/local/lib/php

#where we want to install to 
%define moduledir /usr/local/libexec/php
%define version 1.0.3 
%define php_version 5.1.6
%define pear_path /usr/local/php-%{php_version}/bin


Name: pecl-Fileinfo
Version: %{version}
Copyright: PHP
Release: 2
Summary: a php pecl extension for identifying file types using unix "magic"
Group: Development/Libraries
Distribution: RU-Solaris
Vendor: NBCS-OSS
Source: Fileinfo-%{version}.tgz
Requires: file php5-common
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

#make directory for documentation
%{pear_path}/pear bundle %SOURCE0
mkdir -p %{buildroot}/usr/local/share/pecl-Fileinfo/doc
mv package.xml %{buildroot}/usr/local/share/pecl-Fileinfo
mv %{buildroot}%{peardir}/doc/Fileinfo/* %{buildroot}/usr/local/share/pecl-Fileinfo/doc

#make directory for so
mkdir -p %{buildroot}%{moduledir}
mv  %{buildroot}/usr/local/php-%{php_version}/lib/php/extensions/no-debug-non-zts-20050922/fileinfo.so %{buildroot}%{moduledir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/share/pecl-Fileinfo/package.xml
/usr/local/share/pecl-Fileinfo/doc/CREDITS
/usr/local/share/pecl-Fileinfo/doc/EXPERIMENTAL
/usr/local/share/pecl-Fileinfo/doc/fileinfo.php
%{moduledir}/fileinfo.so


