Summary: Name change utility
Name: namechange
Version: 1.0
Release: 2
Group: System Environment/Base
Copyright: Rutgers
Source: namechange.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Written Gene Weresow (weresow@nbcs) and Jack Chen (jcc@nbcs).

Contains two modules for manipulating files in order to change usernames. 

-- The script expects the file /etc/frontend (a list of front end host 
machines) to exist.  
 
-- The script should be run on the ypmaster. 

-- This version fixes a bug.  Previously, the script did not work 
properly unless it was run from /usr/local/sbin. 


%prep
%setup -q -n files

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(0500, root, other) /usr/local/sbin/*