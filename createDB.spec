Summary: mysql database creation script
Name: createDB
Version: 0.1
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: createDB-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: mysql
Requires: perl
Requires: perl-module-TermReadKey

%description
You have to install perl and mysql first.
 
usage: createDB.pl [-h] [-v] username db_name
where: -h Show this help
       -v Verbose output 
   
createDB.pl will create a MySQL database via two arguments.  The first
argument is the username followed by the database name.  The database
is created and stored in the user's home directory.

The database created will be readable by the world and changeable by
the owner from the database server host.

%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(700,root,other) /usr/local/sbin/createDB.pl