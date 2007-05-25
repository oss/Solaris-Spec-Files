
%define name fruity
%define tar_version 1.0
%define version 1.0rc2
%define beta rc2
%define release 2
%define fruity_dir /usr/local/%{name}-%{version}

Summary: 	Fruity: A PHP Nagios Configuration Tool
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Applications/Internet
Source: 	%{name}-%{tar_version}-%{beta}.tar.gz
URL: 		http://fruity.sourceforge.net
Distribution: 	RU-Solaris
Vendor: 	NBCS-OSS
Packager: 	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	apache, php5, mysql
Provides:	fruity

%description
Fruity is an open-source web-based configuration tool for the 
Nagios network monitoring system. It is designed to provide a 
logical process of creating and managing your network. It is 
written in PHP and uses the AdoDB database abstraction library.

%prep
%setup -q -n %{name}-%{tar_version}-%{beta}

%build
echo Nothing to see here...

%install
rm -rf %{buildroot}

mkdir -p -m0755 %{buildroot}%{fruity_dir}

cd ..

for f in %{name}-%{tar_version}-%{beta}/* ; do
    cp -rp $f %{buildroot}%{fruity_dir}
done

#for d in sqldata images sitedb modules includes style output dojo; do
#    cp -rp $d %{buildroot}%{fruity_dir}
#done

%clean
rm -rf %{buildroot}

%post
cat << END
==========================NOTICE========================
You need to create a link from your web directory to the
fruity directory.

Ex: ln -s %{fruity_dir} /usr/local/apache/htdocs/fruity

Also, you will need to import mysql data.

Please read the INSTALL file for installation and info
regarding the mysql data.

==========================NOTICE========================
END


%files
%defattr(-,www,www,755)

%doc %{fruity_dir}/INSTALL
%doc %{fruity_dir}/CHANGELOG
%doc %{fruity_dir}/LICENSE
%doc %{fruity_dir}/UPGRADING
%{fruity_dir}/TreeMenu.js
%{fruity_dir}/*.php
%{fruity_dir}/sqldata
%{fruity_dir}/images
%{fruity_dir}/sitedb
%{fruity_dir}/modules
%{fruity_dir}/includes
%{fruity_dir}/style
%{fruity_dir}/output
%{fruity_dir}/dojo

%changelog
* Wed May 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.0rc2-2
- Changed PHP5 dependancy
* Tue May 22 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 1.0rc2-1
- Initial build.

