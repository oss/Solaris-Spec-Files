%define version 1.0
%define prefix /usr/local

Name: yapas
Version: %{version}
Copyright: GPL V2 
Release: 1
Summary: A PHP application for mananging MySQL virtual Domains for Postfix 
Group: Services
Source: http://jla.rutgers.edu/~jmsl/yapas-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Provides: yapas

%description
YAPAS stands for Yet Another Postfix Administration System.
It may also stand for Yet Another Postfix Aliasing System.
It may also stand for Yet Another Postfix Aliasing Script.
It may also stand for Yet Another Postfix Annoyance Solver.
It may also stand for Yet Another Postfix Administration Script.
It may also stand for Yet Another Pathetic Acronym, Stupid.

This is a PHP script to manage Postfix virtual domains.
It is designed for use in an environment where role based  
administration is needed. It also integrates with .htaccess so 
you can use your favorite apache plugin for authentication. 
Virtual domains can be selectively mapped to local users.

%prep
%setup -q -n yapas

%build

%install
rm -rf %{buildroot}

mkdir -m 0755 -p %{buildroot}%{prefix}/%{name}-%{version}
mkdir -m 0755 %{buildroot}%{prefix}/%{name}-%{version}/template_files
mkdir -m 0755 %{buildroot}%{prefix}/%{name}-%{version}/images
mkdir -m 0755 %{buildroot}%{prefix}/%{name}-%{version}/css

install -c -m 0644 $RPM_BUILD_DIR/%{name}/*\.php %{buildroot}%{prefix}/%{name}-%{version}

chmod 640 %{buildroot}%{prefix}/%{name}-%{version}/config.php

install -c -m 0644 $RPM_BUILD_DIR/%{name}/template_files/* %{buildroot}%{prefix}/%{name}-%{version}/template_files

install -c -m 0644 $RPM_BUILD_DIR/%{name}/images/* %{buildroot}%{prefix}/%{name}-%{version}/images

install -c -m 0644 $RPM_BUILD_DIR/%{name}/css/* %{buildroot}%{prefix}/%{name}-%{version}/css

%clean
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%post
echo "README.txt is located at %{prefix}/doc/%{name}-%{version}";
echo "You must follow the directions it contains to complete the setup";

%files
%defattr(-, root, www)
%doc README.txt COPYING 
%attr(640,root,www) %{prefix}/%{name}-%{version}/config.php
%{prefix}/%{name}-%{version}/create_domain.php
%{prefix}/%{name}-%{version}/delete_catchall.php
%{prefix}/%{name}-%{version}/change_admin.php
%{prefix}/%{name}-%{version}/edit_alias.php
%{prefix}/%{name}-%{version}/create_catchall.php
%{prefix}/%{name}-%{version}/manage_admin.php
%{prefix}/%{name}-%{version}/delete_aliases.php
%{prefix}/%{name}-%{version}/index.php
%{prefix}/%{name}-%{version}/functions.php
%{prefix}/%{name}-%{version}/login.php
%{prefix}/%{name}-%{version}/logout.php
%{prefix}/%{name}-%{version}/delete_admin.php
%{prefix}/%{name}-%{version}/create_admin.php
%{prefix}/%{name}-%{version}/template.php
%{prefix}/%{name}-%{version}/delete_domains.php
%{prefix}/%{name}-%{version}/create_alias.php
%{prefix}/%{name}-%{version}/edit_domain.php
%{prefix}/%{name}-%{version}/siteadmin.php
%{prefix}/%{name}-%{version}/domainadmin.php
%{prefix}/%{name}-%{version}/edit_catchall.php
%{prefix}/%{name}-%{version}/edit_user.php
%{prefix}/%{name}-%{version}/yapas-functions.php
%{prefix}/%{name}-%{version}/template-alternate.php
%{prefix}/%{name}-%{version}/images
%{prefix}/%{name}-%{version}/template_files
%{prefix}/%{name}-%{version}/css

%changelog
* Tue May 29 2007 John Sante <jmsl@nbcs.rutgers.edu>
- version 1.0, first production release
* Wed Feb 28 2007 John Santel <jmsl@nbcs.rutgers.edu>
- second release
* Tue Jan 9 2007 John Santel <jmsl@nbcs.rutgers.edu>
- first release

