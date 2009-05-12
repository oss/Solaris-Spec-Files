Summary: Daily ADS Summary 
Name: ads-sum
Version: 1.1.2
Release: 1
Group: System Environment/Base
License: Rutgers
Source: ads-sum-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: php-common php-devel

%description
This is a php script that looks in a specified mailfolder, usually 
.AUTO-DELETED-SPAM, and generates a summary of the lowest 20 scoring 
messages from the past 24 hours. The output should be redirected to
a file in the user's Maildir.

%prep
%setup -q 

%install
mkdir -p %{buildroot}/usr/local/bin
cp ads-sum %{buildroot}/usr/local/bin

%clean
rm -rf %{buildroot}

%files
%defattr(755, root, bin)
%doc
/usr/local/bin/ads-sum

%changelog
* Tue May 12 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.2
- fixed issue where some messages were output on same line
- added additional comments

* Wed Apr 8 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.1
- actually took out leading . in foldername

* Wed Apr 1 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.1.0
- removed excess fields from GECOS for fullname
- replaced & with username in GECOS
- send email even when no messages 
- took out leading . in foldername

* Fri Feb 06 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.6-1
- used php_uname to get $host, fixes to formatting of $system
- changes to format of output email
- added users fullname from GECOS

* Thu Jan 29 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.5.-1
- improved command line argument handling now using PEAR:Console_Getopt
- added long options
- fixed problem with HOSTNAME for tcsh
- fixes to tiebreaker

* Fri Jan 9 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.3-1
- all non email messages return exit code 1 
- changed help@nbcs to help@$system

* Fri Jan 9 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.2-1
- fixed path to php for solaris

* Mon Jan 5 2009 David Diffenbaugh <davediff@nbcs.rutgers.edu> - 1.0.1-1
- added starttime and endtime filtering
- added tiebreaker mode
- added command line options

* Tue Jun 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.92-2
- changed permissions to 755 

* Tue Jun 10 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.92-1
- bumped to next version

* Thu Apr 17 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.91-1
- bumped to next version

* Wed Apr 16 2008 David Diffenbaugh <davediff@nbcs.rutgers.edu> 0.87-1
- first release

